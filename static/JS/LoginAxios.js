import axios from "axios";

function sendLogin(){
    var user_email = document.getElementById('user').value;
    var password = document.getElementById('pass').value;

    axios.post('/login', {
        email: user_email,
        password: password
    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (error) {
            console.log(error);
        });
}