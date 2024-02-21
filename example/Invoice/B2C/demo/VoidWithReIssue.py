#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／註銷重開
* 適用於發票註銷重開(發票號碼、自訂編號、開立時間不可更改)。
'''


# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'VOID_WITH_RE_ISSUE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/VoidWithReIssue'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['VoidModel'] = {
    'InvoiceNo':"DZ70000769",
    'VoidReason':"API Test"
}
ecpay_invoice.Send['IssueModel'] = {}

ecpay_invoice.Send['IssueModel']['RelateNumber'] = "ECPAY202303171651421757154922"
ecpay_invoice.Send['IssueModel']['InvoiceDate'] = "2023-03-17 16:51:44" 
ecpay_invoice.Send['IssueModel']['CustomerID'] = ''
ecpay_invoice.Send['IssueModel']['CustomerIdentifier'] = '97025978'
ecpay_invoice.Send['IssueModel']['CustomerName'] = 'test'
ecpay_invoice.Send['IssueModel']['CustomerAddr'] = 'test   zzz'
ecpay_invoice.Send['IssueModel']['CustomerPhone'] = ''
ecpay_invoice.Send['IssueModel']['CustomerEmail'] = 'test@local.com'
ecpay_invoice.Send['IssueModel']['ClearanceMark'] = ''
ecpay_invoice.Send['IssueModel']['Print'] = '1'
ecpay_invoice.Send['IssueModel']['Donation'] = '0'
ecpay_invoice.Send['IssueModel']['LoveCode'] = ''
ecpay_invoice.Send['IssueModel']['CarruerType'] = ''
ecpay_invoice.Send['IssueModel']['CarruerNum'] = ''
ecpay_invoice.Send['IssueModel']['TaxType'] = '1'
ecpay_invoice.Send['IssueModel']['SpecialTaxType'] = 0
ecpay_invoice.Send['IssueModel']['SalesAmount'] = 3931
ecpay_invoice.Send['IssueModel']['InvoiceRemark'] = 'SDK TEST Python V1.0.6'
ecpay_invoice.Send['IssueModel']['Items'] = []
ecpay_invoice.Send['IssueModel']['InvType'] = '07'
ecpay_invoice.Send['IssueModel']['vat'] = '0'

# 商品資訊
ecpay_invoice.Send['IssueModel']['Items'].append({
    'ItemSeq': 1,
    'ItemName': '商品名稱一',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 2052.0,
    'ItemTaxType': '',
    'ItemAmount': 2155,
    'ItemRemark': '商品備註一'
})
ecpay_invoice.Send['IssueModel']['Items'].append({
    'ItemSeq': 2,
    'ItemName': '商品名稱二',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 1692.0,
    'ItemTaxType': '',
    'ItemAmount': 1777,
    'ItemRemark': '商品備註二'
})


# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'InvoiceNo' in aReturn_Info:
    print ('發票號碼：', aReturn_Info['InvoiceNo'])