import $ from "jquery";
import * as common from "./common";
import * as fetch from "./fetch";

/**
 * ユーザーに認証コードの記載されたメールを送信する.
 */
export const emailSend = () => {
    const form_data = {
        email: $("[name='email']").val(),
    };
    const url = common.get_my_domain() + "/signup/email/send/";

    fetch.fetch_api(url, form_data).then((response) => {
        if (response.try_flag === true) {
            location.href = common.get_my_domain() + "/signup/auth/check/";
        } else if (response.try_flag === false) {
            console.log(response.msg);
        } else {
            location.href = common.get_my_domain() + "/maintenance/except/";
        }
    }).catch((error) => {
        console.log("API error", error);
        // location.href = common.get_my_domain() + "/maintenance/except/";
    })
}
/**
 * 認証コードを送信する.
 */
export const authSend = () => {
    const form_data = {
        auth_code: $("[name='auth_code']").val(),
    };
    const url = common.get_my_domain() + "/signup/auth/send/";

    fetch.fetch_api(url, form_data).then((response) => {
        if (response.try_flag === true) {
            location.href = common.get_my_domain() + "/signup/new/";
        } else if (response.try_flag === false) {
            console.log(response.msg);
        } else {
            location.href = common.get_my_domain() + "/maintenance/except/";
        }
    }).catch((error) => {
        console.log("API error", error);
    })
}
/**
 * ユーザーをDBに登録する.
 */
export const signupCreate = () => {
    const form_data = {
        name: $("[name='name']").val(),
        password: $("[name='password']").val(),
    }
    const url = common.get_my_domain() + "/signup/create/";

    fetch.fetch_api(url, form_data).then((response) => {
        if (response.try_flag === true) {
            location.href = common.get_my_domain() + "/signup/fin/"
        } else if (response.try_flag === false) {
            console.log(response.msg);
        } else {
            location.href = common.get_my_domain() + "/maintenance/except/";
        }
    }).catch(() => {
        location.href = common.get_my_domain() + "/maintenance/except/";
    })
}