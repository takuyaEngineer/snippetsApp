import $ from "jquery";
import * as signup from "./signup"
import * as login from "./login"

if ($(".js_email_send").length !== 0) {
    $(".js_email_send").on("click", function () {
        signup.emailSend();
    })
}

if ($(".js_auth_send_button").length !== 0) {
    $(".js_auth_send_button").on("click", function () {
        signup.authSend();
    })
}

if ($(".js_signup_create_button").length !== 0) {
    $(".js_signup_create_button").on("click", function () {
        signup.signupCreate();
    })
}

if ($(".js_login_check_button").length !== 0) {
    $(".js_login_check_button").on("click", function () {
        login.loginCheck();
    })
}