function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// Live status
$('input[name=live_checkbox]').change(
    function () {
        if (this.checked) {
            $.ajax({
                url: '/product/product-live/',
                headers: {"X-CSRFToken": csrftoken},
                method: 'POST',
                dataType: 'json',
                data: {'pk': this.value, 'checked': true},
            })
        } else {
            $.ajax({
                url: '/product/product-live/',
                headers: {"X-CSRFToken": csrftoken},
                method: 'POST',
                dataType: 'json',
                data: {'pk': this.value, 'checked': false},
            })
        }
    }
);


// Category Type Filter
function addProductTypes(data) {
    data = JSON.parse(data);
    var select = document.getElementById('id_product_type');
    select.innerHTML = '';
    for (let i = 0; i < data.length; i++) {
        var opt = document.createElement('option');
        opt.value = `${data[i].fields.product_type}`;
        opt.innerHTML = `${data[i].fields.product_type}`;
        select.appendChild(opt);
    }
}

$('#id_product_category').on('change', function () {
    $.ajax({
        url: '/product/category-filter/',
        method: 'GET',
        dataType: 'json',
        data: {'pk': this.value},
        success: function (data) {
            addProductTypes(data);
        },
    })
});