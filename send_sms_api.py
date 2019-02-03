#requests module will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python in the same way
import requests
#Hitting fast2sms.com for developer bulk sms.
url = "https://www.fast2sms.com/dev/bulk"
# payload = "sender_id=FSTSMS&message=Your message body&language=english&route=p&numbers=10 digit mobile number-1,10 digit mobile number-2"
payload = "sender_id=FSTSMS&message=Good Morning !!!&language=english&route=p&numbers=9999999999,8888888888"
#For DEV-API go to "https://www.fast2sms.com/dashboard/dev-api"
headers = {
    'authorization': "Your fast2smsm DEV-API",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
}

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)