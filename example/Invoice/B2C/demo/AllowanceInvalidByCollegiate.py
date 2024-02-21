#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
發票作業／取消線上折讓
* 若特店開立線上折讓後，想取消折讓，可使用此API將已開立線上折讓的部分取消。此時綠界會將該筆線上折讓申請取消，並將該筆折讓金額返還至該發票可折讓金額。
'''


# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'ALLOWANCE_INVALID_BY_COLLEGIATE'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/AllowanceInvalidByCollegiate'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceNo'] = 'DZ70000601'
ecpay_invoice.Send['AllowanceNo'] = '2303171650095962'
ecpay_invoice.Send['Reason'] = '取消線上折讓測試'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'IA_Invoice_No' in aReturn_Info:
    print ('發票號碼：'+ aReturn_Info['IA_Invoice_No'])