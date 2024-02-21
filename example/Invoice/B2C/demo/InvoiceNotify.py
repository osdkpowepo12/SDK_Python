#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發送通知／發送發票通知
* 
(若不撰寫此API，則可透過廠商後台功能處理)

情景一、【廠商後台>發票通知方式設定】通知選項沒有開啟：
          請特店完全只使用此API來發送電子發票各類通知
情景二、通知失敗，需要額外補送各類通知：
          可使用此API來補送各類發票通知特店
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'INVOICE_NOTIFY'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/InvoiceNotify'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceNo'] = 'DZ70000599' # 發票號碼
ecpay_invoice.Send['AllowanceNo'] = '' # 折讓編號
ecpay_invoice.Send['Phone'] = '' # 發送簡訊號碼
ecpay_invoice.Send['NotifyMail'] = 'demo@local.com' # 發送電子信箱
ecpay_invoice.Send['Notify'] = 'E' # 發送方式
ecpay_invoice.Send['InvoiceTag'] = 'I' # 發送內容類型
ecpay_invoice.Send['Notified'] = 'C'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()
# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
