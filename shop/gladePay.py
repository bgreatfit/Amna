import requests
import json

headers = {'content-type': 'application/json',
            'key':'t4IuG0pSBoKucTjCE5gTQDDO2OFJrdAI25c',
            'mid':'GP_PHMQwuSPbN03qyRPQ84ygfiYeGGny7eR'}






def make_payment(card_no="",expiry_month="",expiry_year="",cvv="",pin="",amount=""):
    payload = {
  "action":"initiate",
  "paymentType":"card",

  "card":{
      "card_no":card_no,
      "expiry_month":expiry_month,
      "expiry_year":expiry_year,
      "ccv":cvv,
      "pin":pin
  },
  "amount":pin,
  "country": "NG",
  "currency": "NGN",
}
    r = requests.put("https://demo.api.gladepay.com/payment", data=json.dumps(payload), headers=headers )

    # print(r.status_code)
    a = json.loads(r.text)
    if a['status'] == 202:
        print(a['txnRef'])
        return a['txnRef']
    else:
        print("something went wrong!!!")
        return "error"
   

# make_payment(card_no="5221 8424 2698 7779",expiry_month="12",expiry_year="22",cvv="000",pin="100",amount="1000")



def validate_otp(txnRef="",otp=""):
    vali = {
    "action":"validate",
    "txnRef":txnRef,
    "otp":otp
    }
    r = requests.put("https://demo.api.gladepay.com/payment", data=json.dumps(vali), headers=headers )
    a = json.loads(r.text)
    if a['status'] == 200:
        return True
    else:
        print("error can't validate otp")
        return False

# validate_otp(txnRef="GP54705346020191208A",otp="123456")

