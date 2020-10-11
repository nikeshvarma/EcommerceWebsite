document.getElementById('add-to-cart').addEventListener('click', function () {

    var pk = this.value;
    $.ajax({
        url: '/user/cart-item/',
        data: {'pk': pk},
        async: true,
        dataType: 'json',
        method: 'GET',
    });
});


function changeQuantity(id, actionType) {
    $.ajax({
        url: '/user/change-quantity/',
        data: {'pk': id, 'action': actionType},
        dataType: 'json',
        method: 'GET',
        success: function () {
            window.location.reload();
        }
    });
}

function removeCartItem(id) {
    $.ajax({
        url: '/user/remove-cart-item/',
        data: {'pk': id},
        dataType: 'json',
        method: 'GET',
        success: function () {
            window.location.reload();
        }
    });
}