#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／開立發票／延遲開立發票（預約開立發票）
*  
I.  預約開立發票：
    特店可使用此功能先將開立發票參數傳送至綠界，由綠界暫存發票資料，待預約開立時間到，系統會自動開立發票。
II. 觸發開立發票：
    特店可使用此功能先將開立發票參數傳送至綠界，由綠界暫存發票資料，等待確認要開立時，再由特店進行觸發開立。
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

import time
import random

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'DELAY_ISSUE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/DelayIssue'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
RelateNumber = 'ECPAY' + time.strftime("%Y%m%d%H%M%S", time.localtime()) +\
   str(random.randint(1000000000, 2147483647))  # 產生測試用自訂訂單編號
ecpay_invoice.Send['RelateNumber'] = RelateNumber
ecpay_invoice.Send['CustomerID'] = ''
ecpay_invoice.Send['CustomerIdentifier'] = ''
ecpay_invoice.Send['CustomerName'] = ''
ecpay_invoice.Send['CustomerAddr'] = ''
ecpay_invoice.Send['CustomerPhone'] = ''
ecpay_invoice.Send['CustomerEmail'] = 'test@localhost.com'
ecpay_invoice.Send['ClearanceMark'] = ''
ecpay_invoice.Send['Print'] = '0'
ecpay_invoice.Send['Donation'] = '0'
ecpay_invoice.Send['LoveCode'] = ''
ecpay_invoice.Send['CarrierType'] = ''
ecpay_invoice.Send['CarrierNum'] = ''
ecpay_invoice.Send['TaxType'] = '1'
ecpay_invoice.Send['SpecialTaxType'] = 0
ecpay_invoice.Send['SalesAmount'] = 500
ecpay_invoice.Send['InvoiceRemark'] = 'SDK TEST Python V1.0.6'
ecpay_invoice.Send['Items'] = []
ecpay_invoice.Send['InvType'] = '07'
ecpay_invoice.Send['DelayFlag'] = '1'
ecpay_invoice.Send['DelayDay'] = 1
ecpay_invoice.Send['Tsr'] = RelateNumber
ecpay_invoice.Send['PayType'] = '2'
ecpay_invoice.Send['PayAct'] = 'ECPAY'
ecpay_invoice.Send['NotifyURL'] = ''
ecpay_invoice.Send['vat'] = '1'

# 商品資訊
ecpay_invoice.Send['Items'].append({
    'ItemSeq':1,
    'ItemName': '商品名稱一',
    'ItemCount': 1,
    'ItemWord': '批',
    'ItemPrice': 100,
    'ItemTaxType': '',
    'ItemAmount': 100,
})
ecpay_invoice.Send['Items'].append({
    'ItemSeq':2,
    'ItemName': '商品名稱二',
    'ItemCount': 2,
    'ItemWord': '件',
    'ItemPrice': 200,
    'ItemTaxType': '',
    'ItemAmount': 400,
})



# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回)
print ('RelateNumber：' + str(RelateNumber))
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'OrderNumber' in aReturn_Info:
    print ('交易單號：'+ aReturn_Info['OrderNumber'])