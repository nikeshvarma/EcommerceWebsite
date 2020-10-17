from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.db.models import F

from PRODUCTS.models import Product
from USER.models import UserCart
from . import Checksum

from .models import Order, TransactionDetails, ProductOrdered
from .utils import VerifyPaytmResponse


@login_required()
def payment_request(request):
    email = request.user.email
    amount = request.POST.get('amount')
    phone_number = request.POST.get('phone')
    address = str(request.user.userprofile.address) + " " + str(request.user.userprofile.landmark) + " " + str(request.user.userprofile.city) + " " + str(request.user.userprofile.state)
    product = eval(request.POST.get('product_list'))
    customer_id = str(request.user.id)
    product_instance = {Product.objects.get(pk=key): quantity for key, quantity in product.items()}

    order = Order.objects.create(
        user=request.user,
        name=request.user.userprofile.name,
        phone_number=request.user.userprofile.phone_number,
        email=request.user.email,
        amount=amount,
        address=address,
        payment_status='Payment Initiated',
        order_status='Ordered',
    )

    for item, quantity in product_instance.items():
        order.product.add(item, through_defaults={'quantity': quantity})

    order.save()

    order_id = str(order.order_id)
    data_dict = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
        'MOBILE_NO': str(phone_number),
        'EMAIL': str(email),
        'CUST_ID': customer_id,
        'ORDER_ID': order_id,
        'TXN_AMOUNT': str(amount),
    }

    data_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, settings.PAYTM_MERCHANT_KEY)

    context = {
        'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
        'comany_name': settings.PAYTM_COMPANY_NAME,
        'data_dict': data_dict
    }

    # check is product out of stock or not
    buy_products = list(ProductOrdered.objects.filter(order_id=order.order_id).values_list('product_id', 'quantity'))
    for item in buy_products:
        item_obj = Product.objects.select_for_update().get(pk=item[0])
        quantity = item[1]
        if int(item_obj.product_stoke) >= int(quantity):
            pass
        else:
            ProductOrdered.objects.filter(order_id=order_id).delete()
            order.delete()
            UserCart.objects.filter(user_id=request.user).delete()
            messages.error(request, 'Sorry ! Product is out of stock')
            return redirect('order_page')

    return render(request, 'payment/payment-redirect.html', context=context)


@csrf_exempt
def payment_status(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:

        paytm = resp['paytm']
        order = Order.objects.get(order_id=paytm['ORDERID'])
        user = order.user

        tnx = TransactionDetails.objects.create(
            order=order,
            transaction_id=paytm['TXNID'],
            bank_transaction_id=paytm['BANKTXNID'],
            transaction_amount=paytm['TXNAMOUNT'],
            transaction_status=paytm['STATUS'],
            transaction_type=paytm['TXNTYPE'],
            gateway_name=paytm['GATEWAYNAME'],
            response_code=paytm['RESPCODE'],
            response_message=paytm['RESPMSG'],
            bank_name=paytm['BANKNAME'],
            payment_mode=paytm['PAYMENTMODE'],
            refund_amount=paytm['REFUNDAMT'],
            transaction_date=paytm['TXNDATE']
        )
        # transaction complete
        tnx.save()

        # order complete
        order.payment_status = 'Payment Complete'
        order.save()

        # Change Stock Details
        buy_products = list(ProductOrdered.objects.filter(order_id=order.order_id).values_list('product_id', 'quantity'))
        for item in buy_products:
            item_obj = Product.objects.get(pk=item[0])
            quantity = item[1]
            item_obj.product_stoke = F('product_stoke') - quantity
            item_obj.save()

        # Cart deleted after order complete
        UserCart.objects.filter(user=user).delete()

        messages.success(request, 'Order Placed Successful')

        return render(request, 'payment/payment-successful-redirect.html')

    else:
        paytm = resp['paytm']
        order = Order.objects.get(order_id=paytm['ORDERID'])

        tnx = TransactionDetails.objects.create(
            order=order,
            transaction_id=paytm['TXNID'],
            bank_transaction_id=paytm['BANKTXNID'],
            transaction_amount=paytm['TXNAMOUNT'],
            transaction_status=paytm['STATUS'],
            transaction_type=paytm['TXNTYPE'],
            gateway_name=paytm['GATEWAYNAME'],
            response_code=paytm['RESPCODE'],
            response_message=paytm['RESPMSG'],
            bank_name=paytm['BANKNAME'],
            payment_mode=paytm['PAYMENTMODE'],
            refund_amount=paytm['REFUNDAMT'],
            transaction_date=paytm['TXNDATE']
        )
        # transaction details save
        tnx.save()

        # order failed register
        order.payment_status = 'Transaction Failed'
        order.order_status = 'Failed'
        order.save()

        messages.error(request, 'Order Failed')

        # check what happened; details in resp['paytm']
        return render(request, 'payment/payment-failed redirect.html')
