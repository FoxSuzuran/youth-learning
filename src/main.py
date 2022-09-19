import os
import AutoEmail
import json
import requests

request_url = "https://dxx.scyol.com/api/student/commit"

request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6307062c)",
    "Content-Type": "application/json",
    "token": os.environ.get("token"),
}

request_json = {
    "name": os.environ.get("name"),
    "tel": os.environ.get("tel"),
    "org": os.environ.get("org"),
    "lastOrg": os.environ.get("lastOrg"),
    "orgName": os.environ.get("orgName"),
    "allOrgName": os.environ.get("allOrgName"),
}

if __name__ == "__main__":
    r = requests.post(
        url=request_url, headers=request_header, data=json.dumps(request_json)
    )
    r.encoding = "utf-8"
    message = json.loads(r.text)["msg"]
    if r.status_code == 200 and not message == "微信用户未登录":
        print(message)
    else:
        AutoEmail.EmailSend()
