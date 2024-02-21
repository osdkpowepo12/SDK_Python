#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／開立發票／取消延遲開立發票
* 營業人(特店)可使用此功能將預約開立時間未到或尚未觸發開立之發票取消延遲開立。
'''

# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

import time
import random

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'CANCEL_DELAY_ISSUE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/CancelDelayIssue'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['Tsr'] = 'ECPAY202303171511391521578202'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
