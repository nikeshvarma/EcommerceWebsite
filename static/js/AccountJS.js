// calling functions
document.getElementById('id_password2').addEventListener('keyup', checkPassword);
document.getElementById('id_password1').addEventListener('keyup', checkPassword);

document.getElementById('id_email').addEventListener('change', checkEmail);


// password match function
function checkPassword() {
    pass1 = document.getElementById('id_password1').value;
    pass2 = document.getElementById('id_password2').value;
    var message = document.getElementById('massage');
    if (pass1 === pass2) {
        message.className = 'd-none';
        document.getElementById('createButton').disabled = false;
    } else {
        message.style.color = 'red';
        message.innerHTML = 'password not matched';
        message.className = '';
        document.getElementById('createButton').disabled = true;
    }
}


// register email check
function checkEmail() {
    email = document.getElementById('id_email').value;
    var http = new XMLHttpRequest();
    http.open("GET", "/account/check-email/?email=" + email, true);
    http.send();
    http.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var value = JSON.parse(http.response);
            if (value['is_registered']) {
                document.getElementById('emailcheck').className = '';
                document.getElementById('emailcheck').style.color = 'red';
                document.getElementById('emailcheck').innerHTML = `An Account is already registered with this email.<br>`;
            } else {
                document.getElementById('emailcheck').className = 'd-none';
            }
        }
    };
}

function send_otp() {
    let number = $('#id_phone_number').val();

    $.ajax({
        url: '/user/otp-verification/',
        method: 'GET',
        dataType: 'json',
        data: {'phone_number': number},
    })
}