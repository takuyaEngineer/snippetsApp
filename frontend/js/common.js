import $ from "jquery";
/**
 * ドメイン名を取得する.
 * もしポート番号があるならポート番号もつけて取得する。
 * @returns ドメイン名
 */
export const get_my_domain = () => {
    if ($(location).attr("port")) {
        return $(location).attr("protocol") + "//" + $(location).attr("hostname") + ":" + $(location).attr("port");
    } else {
        return $(location).attr("protocol") + "//" + $(location).attr("hostname");
    }
}
/**
 * cookieを取得する.
 * @param {*} name cookieのkey
 * @returns 取得したcookieのvalue
 */
export const get_Cookie = (name) => {
    let cookie_value;
    const cookie = document.cookie
    const cookies = cookie.split(";")
    for (const cookie of cookies) {
        const cookie_arr = cookie.split("=");
        // 半角スペースを排除する
        const cookie_name = cookie_arr[0].replace(" ", "")
        if (cookie_name === name) {
            cookie_value = cookie_arr[1]
        }
    }
    return cookie_value;
}