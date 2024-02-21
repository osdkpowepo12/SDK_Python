#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／作廢折讓
* 若特店開立折讓後，想取消折讓、或開立折讓錯誤..等，可使用此API將已開立折讓的部分作廢(不是整張發票作廢喔!)。
  此時會將折讓作廢發票參數傳送至綠界暫存。綠界會於隔日，將折讓作廢發票資訊上傳至財政部電子發票整合服務平台。
'''


# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'ALLOWANCE_INVALID'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/AllowanceInvalid'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceNo'] = 'DZ70000600'
ecpay_invoice.Send['AllowanceNo'] = '2023031716485772'
ecpay_invoice.Send['Reason'] = '錯開發票'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'IA_Invoice_No' in aReturn_Info:
    print ('發票號碼：'+ aReturn_Info['IA_Invoice_No'])