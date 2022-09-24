import axios from "axios";

function sendRegister(){
    var email = document.getElementById('user').value;
    var capcha = document.getElementById('captcha').value;
    var name = document.getElementById('username').value;
    var password = document.getElementById('pass').value;
    var re_password = document.getElementById('pass_re').value;

    axios.post('/register', {
        user_email: email,
        captcha: capcha,
        user_name: name,
        user_password:password
    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}
