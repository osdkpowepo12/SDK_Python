#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
前置作業／查詢財政部配號結果
* 當營業人(特店)取得財政部的配號結果後，可建立當年度(含當月)或下個年度的字軌。在開立發票之前，必須先設定字軌區間，並且可設定多組。

❗ 注意事項：

電子發票號碼為 50 個一組
若您並非將所有配得的字軌號碼都新增到綠界科技系統，請務必特別留意，電子發票號碼為 50 個一組，
分配時請以 50 個號碼為一個單位，且起始號碼尾數一定為 00 或 50，結尾號碼尾數一定為 49 或 99。
範例：
甲公司本次配得共 1000 個號碼(AB10000050~AB10001049)，要分配給 A、B 兩間發票加值中心，因為在 B
加值中心開立的發票不多，故甲公司只想設定最低數量在 B 加值中心，其餘都分給 A 加值中心。
甲公司可分配如下：
A 加值中心：950 號 (AB10000050~AB10000999)
B 加值中心：50 號 (AB10001000~AB10001049)
※ 因一組為 50 號，B 加值中心至少必須設定 50 個號碼。
請勿於多個發票系統設定相同字軌號碼
若您同時有使用其他 POS 系統、加值中心或發票平台服務，請特別注意不可於多個發票系統設定到相同區間的字軌！以免發票號碼重覆開立。
'''


# 1.載入SDK程式與建立物件
from ecpay_invoice.ecpay_main import EcpayInvoice

ecpay_invoice = EcpayInvoice()

# 2.寫入基本介接參數
ecpay_invoice.Invoice_Method = 'GET_GOV_INVOICE_WORD_SETTING'
ecpay_invoice.Invoice_Url = 'https://einvoice-stage.ecpay.com.tw/B2CInvoice/GetGovInvoiceWordSetting'
ecpay_invoice.MerchantID = '2000132'
ecpay_invoice.HashKey = 'ejCk326UnaZWKisg'
ecpay_invoice.HashIV = 'q9jcZX8Ib9LM8wYk'

# 3.寫入發票相關資訊
ecpay_invoice.Send['InvoiceYear'] = '112'

# 4. 送出
aReturn_Info = ecpay_invoice.Check_Out()

# 5. 返回
print (aReturn_Info)
if 'RtnMsg' in aReturn_Info:
    print ('回傳訊息: ', aReturn_Info['RtnMsg'])
if 'RtnCode' in aReturn_Info and  aReturn_Info['RtnCode'] == 1 and 'InvoiceInfo' in aReturn_Info:
    print ('發票配號結果清單：', aReturn_Info['InvoiceInfo'])