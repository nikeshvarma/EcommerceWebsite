function changeImage(_src) {
    var imgDiv = document.getElementById('main-img');
    var imageElement = imgDiv.getElementsByTagName('img')[0];
    imageElement.src = _src;
}


function searchQuery(event) {
    $('#search-result').html('');
    $.ajax({
        url: '/search-items/',
        method: 'POST',
        dataType: 'json',
        data: {'query': event.target.value},
        success: function (data) {
            if (data['response'] != 'None') {
                $.each(data, function (key, value) {
                    $('#search-result').append(
                        `
                            <a id="search-anchor" class="anchor-class" href="http://localhost:8000/view-product-info/${value[0]}/">
                                <li class="list-group-item search-list">
                                    <img class="search-img" src='/media/${value[2]}' alt="${value[0]}"> <h6 class="search-h1"> ${value[1]}</h6>
                                </li>
                            </a>
                        `
                    )
                })
            } else {
                $('#search-result').html('');
            }
        }
    })
}
