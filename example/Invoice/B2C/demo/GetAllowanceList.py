#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票查詢／查詢折讓明細
* 可使用此API查詢已開立折讓之發票資訊，但不包含消費者尚未同意之線上折讓單
'''

# 1.載入SDK程式與建立物件

from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'GET_ALLOWANCE_LIST'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/GetAllowanceList'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['SearchType'] = '0' # 查詢方式
ecpay_invoice.Send['AllowanceNo'] = '2018071615286810' # 折讓編號
ecpay_invoice.Send['InvoiceNo'] = 'FY10004005'  # 發票號碼
ecpay_invoice.Send['Date'] = ''  # 日期

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'AllowanceInfo' in aReturn_Info:
    print ('折讓資訊列表：', aReturn_Info['AllowanceInfo'])