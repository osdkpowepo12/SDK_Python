#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
資料驗證／捐贈碼驗證
* 特店系統可使用此API來驗證捐贈碼是否存在
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice


ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'CHECK_LOVE_CODE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/CheckLoveCode'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['LoveCode'] = '51919'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'IsExist' in aReturn_Info:
    print('捐贈碼是否存在', "存在" if aReturn_Info['IsExist']=="Y" else "不存在")