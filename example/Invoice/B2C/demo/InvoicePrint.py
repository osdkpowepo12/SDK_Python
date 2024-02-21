#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票列印
* 特店可使用此API取得發票列印網址
'''


# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'INVOICE_PRINT'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/InvoicePrint'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceNo'] = 'DZ70000201'
ecpay_invoice.Send['InvoiceDate'] = '2023-03-17'
ecpay_invoice.Send['PrintStyle'] = 1
ecpay_invoice.Send['IsShowingDetail'] = 1
# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'InvoiceHtml' in aReturn_Info:
    print ('發票列印網址：', aReturn_Info['InvoiceHtml'])