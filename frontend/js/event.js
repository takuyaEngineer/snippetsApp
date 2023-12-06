import $ from "jquery";

/**
 * パスワードの表示非表示を切り替える.
 */
export const switch_show_password = () => {
    if ($(".js_password_switch_checkbox").prop("checked")) {
        $(".js_password_input").attr("type", "text");
    } else {
        $(".js_password_input").attr("type", "password");
    }
}