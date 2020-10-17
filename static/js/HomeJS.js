function reload() {
    setTimeout(function () {
        location.reload();
    }, 100)
}

function changeImage(_src) {
    var imgDiv = document.getElementById('main-img');
    var imageElement = imgDiv.getElementsByTagName('img')[0];
    imageElement.src = _src;
}


function buyNow(id, action) {
    window.location = "http://localhost:8000/checkout";
    if (user != 'AnonymousUser') {
        updateUserCart(id, action);
    } else {
        updateSessionCart(id, action);
    }
}


function updateCart(id, action) {
    if (user != 'AnonymousUser') {
        updateUserCart(id, action);
    } else {
        updateSessionCart(id, action);
    }
}

function updateUserCart(id, action) {
    $.ajax({
        url: '/user/update-cart/',
        method: 'POST',
        dataType: 'json',
        data: {'id': id, 'action': action},
        success: function () {
            const cartButton = $('#add-to-cart');
            cartButton.text('Go To Cart');
            cartButton.attr('href', '/user/cart/');
        }
    })
}

function updateSessionCart(id, action) {
    $.ajax({
        url: '/user/session-cart/',
        method: 'POST',
        dataType: 'json',
        data: {'id': id, 'action': action},
        success: function () {
            const cartButton = $('#add-to-cart');
            cartButton.text('Go To Cart');
            cartButton.attr('href', '/user/cart/');
        }
    })
}

