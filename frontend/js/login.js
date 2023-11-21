import $ from "jquery";
import * as common from "./common";
import * as fetch from "./fetch";

/**
 * ユーザーをDBに登録する.
 */
export const loginCheck = () => {
    const form_data = {
        email: $("[name='email']").val(),
        password: $("[name='password']").val(),
    }
    const url = common.get_my_domain() + "/login/check/";

    fetch.fetch_api(url, form_data).then((response) => {
        console.log(response);
        if (response.try_flag === true) {
            location.href = common.get_my_domain() + "/snippet/"
            // console.log("success");
        } else if (response.try_flag === false) {
            console.log(response.msg);
        } else {
            location.href = common.get_my_domain() + "/maintenance/except/";
        }
    }).catch((err) => {
        console.log(err);
        // location.href = common.get_my_domain() + "/maintenance/except/";
    })
}