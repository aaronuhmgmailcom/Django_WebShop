import json

from alipay import AliPay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

app_private_key_string = open(settings.ALIPAY_KEY_DIR + 'app_private_key.pem').read()
alipay_public_key_string = open(settings.ALIPAY_KEY_DIR + 'alipay_publickey.pem').read()
class MyAliPay(View):
    # ftljjl6769 @ sandbox.com      111111
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.alipay=AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None,
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,
            sign_type='RSA2',
            debug=True
        )
    def get_trade_url(self,order_id,amount):
        base_url='https://openapi.alipaydev.com/gateway.do'
        order_string=self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=amount,
            subject=order_id,
            return_url=settings.ALIPAY_RETURN_URL,
            notify_url=settings.ALIPAY_NOTIFY_URL
        )
        return base_url+'?'+order_string

class JumpView(MyAliPay):
    def get(self,request):
        return render(request,'ajax_alipay.html')

    def post(self,request):
        json_obj=json.loads(request.body)
        order_id=json_obj['order_id']
        pay_url=self.get_trade_url(order_id,99)
        return JsonResponse({'pay_url':pay_url})
