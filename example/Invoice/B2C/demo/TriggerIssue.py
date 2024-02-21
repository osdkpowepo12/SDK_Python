#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／開立發票／觸發開立發票
* 
I. 觸發開立發票：
待消費者付款完成後會呼叫此API，觸發先前暫存在綠界的參數開立發票。

II. 觸發後延遲開立發票：
待消費者付款完成後會呼叫此API，觸發先前暫存在綠界的參數開立發票，再依據先前所設定的延遲開立天數，待預約開立時間到，系統自動開立。
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'TRIGGER_ISSUE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/TriggerIssue'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['Tsr'] = 'ECPAY201807161533501566047166' # 交易單號
ecpay_invoice.Send['PayType'] = '2'        # 交易類別

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'Tsr' in aReturn_Info:
    print ('交易單號：', aReturn_Info['Tsr'])