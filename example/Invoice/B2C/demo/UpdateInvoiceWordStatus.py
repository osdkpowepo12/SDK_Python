#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
前置作業／設定字軌號碼狀態
* 營業人(特店)新增字軌後，字軌的預設狀態皆為已審核且未啟用。如欲使用字軌，必須先設定狀態將字軌啟用。
  在開立發票之前，必須先將已新增完成的字軌做狀態的設定。
'''


# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'UPDATE_INVOICE_WORD_STATUS'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/UpdateInvoiceWordStatus'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['TrackID'] = '2524'
ecpay_invoice.Send['InvoiceStatus'] = 2

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])