#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／開立折讓／線上開立折讓（通知開立）
* 若商品質量、規格等不符合消費者要求，特店同意在商品價格上給予減讓，可使用此API將開立折讓發票參數傳送至綠界，暫存折讓發票資料。
  綠界會寄折讓同意通知信給買家，待買家同意折讓後，綠界會依發票折讓開立參數，開立發票折讓單並於隔日，將折讓資料上傳至財政部電子發票整合服務平台。
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'ALLOWANCE_BY_COLLEGIATE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/AllowanceByCollegiate'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊

ecpay_invoice.Send['InvoiceNo'] = 'DZ70000601'
ecpay_invoice.Send['InvoiceDate'] = '2023-03-17'
ecpay_invoice.Send['AllowanceNotify'] = 'E'
ecpay_invoice.Send['CustomerName'] = ''
ecpay_invoice.Send['NotifyMail'] = 'test@local.com'
ecpay_invoice.Send['AllowanceAmount'] = 3
ecpay_invoice.Send['Items'] = []
ecpay_invoice.Send['ReturnURL'] = ''

# 商品資訊


ecpay_invoice.Send['Items'].append({
    'ItemSeq': 1,
    'ItemName': '商品名稱一',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 1.0,
    'ItemTaxType': '',
    'ItemAmount': 2,
})
ecpay_invoice.Send['Items'].append({
    'ItemSeq': 2,
    'ItemName': '商品名稱二',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 1.0,
    'ItemTaxType': '',
    'ItemAmount': 1,
})



# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print(aReturn_Info)
print(aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'IA_Allow_No' in aReturn_Info:
    print('折讓單號：' + aReturn_Info['IA_Allow_No'])

