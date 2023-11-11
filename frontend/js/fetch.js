import * as common from "./common";

/**
 * APIを叩く
 * @param {*} url APIのエンドポイント
 * @param {*} form_data APIに送るリクエストボディ
 * @returns APIから返ってきたレスポンスのプロミス型のデータ
 */
export const fetch_api = (url, form_data) => {
    return new Promise((resolve, reject) => {
        const csrf = common.get_Cookie("csrftoken");
        fetch(url, {
            headers: {
                'Content-Type': "application/json",
                "X-CSRFToken": csrf
            },
            method: "POST",
            mode: "same-origin",
            // credentials: 
            body: JSON.stringify(form_data)
        }).then((res) => {
            return res.json()
        }).then((data) => {
            return resolve(data);
        }).catch((err) => {
            return reject(err)
        });
    })
}