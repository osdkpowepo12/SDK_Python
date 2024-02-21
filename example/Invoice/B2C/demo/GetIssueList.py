#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票查詢／查詢特定多筆發票
* 特店可使用此API查詢各種類別多筆發票資訊，綠界提供Json/CSV格式回傳。
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'GET_ISSUE_LIST'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/GetIssueList'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['BeginDate'] = '2023-02-01'
ecpay_invoice.Send['EndDate'] = '2023-02-01'
ecpay_invoice.Send['NumPerPage'] = 5
ecpay_invoice.Send['ShowingPage'] = 2
ecpay_invoice.Send['DataType'] = 1
ecpay_invoice.Send['Query_Award'] = '0'
ecpay_invoice.Send['Query_Invalid'] = '0'
ecpay_invoice.Send['Query_Print'] = '0'
ecpay_invoice.Send['Query_Upload'] = '0'
ecpay_invoice.Send['Query_Identifier'] = '0'
ecpay_invoice.Send['Query_TaxType'] = '0'
ecpay_invoice.Send['Query_Category'] = '0'
ecpay_invoice.Send['Query_Customer_Name'] = ''
ecpay_invoice.Send['Query_Customer_Phone'] = ''


# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'InvoiceData' in aReturn_Info:
    print ('發票資料：', aReturn_Info['InvoiceData'])