#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票查詢／查詢作廢折讓明細
* 特店系統可使用此API查詢已作廢折讓明細資訊
'''

# 1.載入SDK程式與建立物件

from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'GET_ALLOWANCE_INVALID'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/GetAllowanceInvalid'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceNo'] = 'FY10004005'   # 發票號碼
ecpay_invoice.Send['AllowanceNo'] = '2018071615286810' # 折讓編號

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
