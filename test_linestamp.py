import requests
 
line_notify_token = "CSovvMnibCrRem01t0NoAjjXcWGQHVAtZYpFFF2D1eb"
line_notify_api = "https://notify-api.line.me/api/notify"
 
#定義
def LineNotify(mode):
    if (mode == "text"):
        payload = {"message":message}
    elif (mode == "stamp"):
        payload = {"message":message, "stickerPackageId": stickerPackageId, "stickerId": stickerId}
    headers = {"Authorization":"Bearer " + line_notify_token}
    requests.post(line_notify_api, data = payload, headers = headers)
 
#出力させる箇所に記述（テキスト）
#message = "テキストだけのメッセージです。"
#LineNotify("text")
 
#出力させる箇所に記述（テキストとスタンプ）
message = "明日の出演情報は"
stickerPackageId = "3"
stickerId = "227"
LineNotify("stamp")
