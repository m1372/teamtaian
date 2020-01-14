import requests
 
def LineNotify(message):
    line_notify_token = "CSovvMnibCrRem01t0NoAjjXcWGQHVAtZYpFFF2D1eb"
    line_notify_api = "https://notify-api.line.me/api/notify"
 
    payload = {"message":message}
    headers = {"Authorization":"Bearer " + line_notify_token}
    requests.post(line_notify_api, data = payload, headers = headers)
 
message = 'メッセージ本文'
LineNotify(message)
