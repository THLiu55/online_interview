import axios from "axios";

function sendCaptcha(){
    var email = document.getElementById('user').value;

    axios.post('/captcha', {
        email: email
    })
        .then(function (response){
            console.log(response);
        })
        .catch(function (error){
            console.log(error);
        })
}

function sendRegister(){
    var email = document.getElementById('user').value;
    var captcha = document.getElementById('captcha').value;
    var name = document.getElementById('username').value;
    var password = document.getElementById('pass').value;
    var re_password = document.getElementById('pass_re').value;

    axios.post('/register', {
        email: email,
        captcha: captcha,
        userName: name,
        password: password,
        repassword: re_password

    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}
