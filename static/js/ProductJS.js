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

// Category Type Filter
function addProductTypes(data) {
    console.log(data);
    var select = document.getElementById('id_product_type');
    select.innerHTML = '';
    for (let i = 0; i < data.length; i++) {
        var opt = document.createElement('option');
        opt.value = `${data[i][1]}`;
        opt.innerHTML = `${data[i][0]}`;
        select.appendChild(opt);
    }
}

$('#id_product_category').on('change', function () {
    $.ajax({
        url: '/products/product-type/filter/',
        method: 'GET',
        dataType: 'json',
        data: {'pk': this.value},
        success: function (data) {
            addProductTypes(data);
        },
    })
});