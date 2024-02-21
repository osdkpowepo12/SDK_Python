#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
前置作業／查詢財政部配號結果
* 特店系統可使用此API查詢字軌號碼以及字軌的使用情況
'''


# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'GET_INVOICE_WORD_SETTING'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/GetInvoiceWordSetting'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceYear'] = '112'
ecpay_invoice.Send['InvoiceTerm'] = 2
ecpay_invoice.Send['UseStatus'] = 0
ecpay_invoice.Send['InvoiceCategory'] = 1
ecpay_invoice.Send['InvType'] = '07'
ecpay_invoice.Send['InvoiceHeader'] = ''

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'InvoiceInfo' in aReturn_Info:
    print ('發票資訊：', aReturn_Info['InvoiceInfo'])