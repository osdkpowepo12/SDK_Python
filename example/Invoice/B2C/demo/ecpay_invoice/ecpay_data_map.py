#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
*  前置作業／查詢財政部配號結果
'''
class ECPay_GET_GOV_INVOICE_WORD_SETTING():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceYear': str(),
    })


'''
*  前置作業／字軌與配號設定
'''
class ECPay_ADD_INVOICE_WORD_SETTING():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceTerm': int(),
        'InvoiceYear': str(),
        'InvType': str(),
        'InvoiceCategory': str(),
        'InvoiceHeader': str(),
        'InvoiceStart': str(),
        'InvoiceEnd': str(),
    })


'''
*  前置作業／設定字軌號碼狀態
'''
class ECPay_UPDATE_INVOICE_WORD_STATUS():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'TrackID': str(),
        'InvoiceStatus': int(),
    })


'''
*  前置作業／查詢字軌
'''
class ECPay_GET_INVOICE_WORD_SETTING():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceYear': str(),
        'InvoiceTerm': int(),
        'UseStatus': int(),
        'InvoiceCategory': int(),
        'InvType': str(),
        'InvoiceHeader': str()
    })


'''
*  資料驗證／統一編號驗證
'''
class ECPay_GET_COMPANY_NAME_BY_TAX_ID():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'UnifiedBusinessNo': str()
    })


'''
*  資料驗證／手機條碼驗證
'''
class ECPay_CHECK_BARCODE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'BarCode': str()
    })


'''
*  資料驗證／捐贈碼驗證
'''
class ECPay_CHECK_LOVE_CODE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'LoveCode': str(),
    })


'''
*  發票作業／開立發票／一般開立發票 
'''
class ECPay_ISSUE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'RelateNumber': str(),
        'CustomerID': str(),
        'CustomerIdentifier': str(),
        'CustomerName': str(),
        'CustomerAddr': str(),
        'CustomerPhone': str(),
        'CustomerEmail': str(),
        'ClearanceMark': str(),
        'Print': str(),
        'Donation': str(),
        'LoveCode': str(),
        'CarruerType': str(),
        'CarruerNum': str(),
        'TaxType': str(),
        'SpecialTaxType': int(),
        'SalesAmount': int(),
        'InvoiceRemark': str(),
        'Items': list(),
        'InvType': str(),
        'vat': str(),
    })


'''
*  發票作業／開立發票／延遲開立發票（預約開立發票）
'''
class ECPay_DELAY_ISSUE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'RelateNumber': str(),
        'CustomerID': str(),
        'CustomerIdentifier': str(),
        'CustomerName': str(),
        'CustomerAddr': str(),
        'CustomerPhone': str(),
        'CustomerEmail': str(),
        'ClearanceMark': str(),
        'Print': str(),
        'Donation': str(),
        'LoveCode': str(),
        'CarrierType': str(),
        'CarrierNum': str(),
        'TaxType': str(),
        'SpecialTaxType': int(),
        'SalesAmount': int(),
        'InvoiceRemark': str(),
        'Items': list(),
        'InvType': str(),
        'DelayFlag': str(),
        'DelayDay': int(),
        'Tsr': str(),
        'PayType': str(),
        'PayAct': str(),
        'NotifyURL': str(),
        'vat':str()
    })


'''
*  發票作業／開立發票／觸發開立發票
'''
class ECPay_TRIGGER_ISSUE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'Tsr': str(),
        'PayType': str()
    })


'''
*  發票作業 / 開立發票 / 取消延遲開立發票
'''
class ECPay_CANCEL_DELAY_ISSUE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'Tsr': str(),
    })


'''
*  發票作業／開立折讓／一般開立折讓（紙本開立）
'''
class ECPay_ALLOWANCE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'InvoiceDate': str(),
        'AllowanceNotify': str(),
        'CustomerName': str(),
        'NotifyMail': str(),
        'NotifyPhone': str(),
        'AllowanceAmount': int(),
        'Items': list()
    })


'''
*  發票作業 / 開立折讓 / 線上開立折讓（通知開立）
'''
class ECPay_ALLOWANCE_BY_COLLEGIATE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'InvoiceDate': str(),
        'AllowanceNotify': str(),
        'CustomerName': str(),
        'NotifyMail': str(),
        'AllowanceAmount': int(),
        'Items': list(),
        'ReturnURL': str(),
    })


'''
*  發票作業／作廢發票
'''
class ECPay_INVALID():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'InvoiceDate': str(),
        'Reason': str()
    })


'''
*  發票作業／作廢折讓
'''
class ECPay_ALLOWANCE_INVALID():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'AllowanceNo': str(),
        'Reason': str(),
    })


'''
*  發票作業／取消線上折讓
'''
class ECPay_ALLOWANCE_INVALID_BY_COLLEGIATE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'AllowanceNo': str(),
        'Reason': str()
    })


'''
*  發票作業／註銷重開
'''
class ECPay_VOID_WITH_RE_ISSUE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'VoidModel': dict(),
        'IssueModel': dict(),
    })


'''
*  發票查詢／查詢發票明細
情境一：以特店自訂編號[RelateNumber]做查詢
'''
class ECPay_GET_ISSUE():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'RelateNumber': str(),
    })


'''
*  發票查詢／查詢發票明細
情境二：以發票號碼[InvoiceNo]與發票開立日期[InvoiceDate]做查詢
'''
class ECPay_GET_ISSUE2():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'InvoiceDate': str(),
    })


'''
*  發票查詢／查詢特定多筆發票
'''
class ECPay_GET_ISSUE_LIST():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'BeginDate': str(),
        'EndDate': str(),
        'NumPerPage': int(),
        'ShowingPage': int(),
        'DataType': int(),
        'Query_Award': str(),
        'Query_Invalid': str(),
        'Query_Print': str(),
        'Query_Upload': str(),
        'Query_Identifier': str(),
        'Query_TaxType': str(),
        'Query_Category': str(),
        'Query_Customer_Name': str(),
        'Query_Customer_Phone': str(),
    })


'''
*  發票查詢／查詢折讓明細
'''
class ECPay_GET_ALLOWANCE_LIST():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'SearchType': str(),
        'AllowanceNo': str(),
        'InvoiceNo': str(),
        'Date': str()
    })


'''
*  發票查詢／查詢作廢發票明細
'''
class ECPay_GET_INVALID():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'RelateNumber': str(),
        'InvoiceNo': str(),
        'InvoiceDate': str()
    })


'''
*  發票查詢／查詢作廢折讓明細
'''
class ECPay_GET_ALLOWANCE_INVALID():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'AllowanceNo': str()
    })


'''
*  發送通知／發送發票通知
'''
class ECPay_INVOICE_NOTIFY():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'AllowanceNo': str(),
        'Phone': str(),
        'NotifyMail': str(),
        'Notify': str(),
        'InvoiceTag': str(),
        'Notified': str()
    })


'''
*  發票列印
'''
class ECPay_INVOICE_PRINT():
    # 所需參數
    parameters = dict({
        'MerchantID': str(),
        'RqHeader': dict(),
        'Data': str()
    })
    # 需要做加密的資料
    encrypted_data = dict({
        'MerchantID': str(),
        'InvoiceNo': str(),
        'InvoiceDate': str(),
        'PrintStyle': int(),
        'IsShowingDetail': int()
    })