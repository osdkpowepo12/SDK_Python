#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import base64
import time
import json
import urllib
import requests
from Crypto.Cipher import AES

from ecpay_invoice.ecpay_data_map import *


class EcpayInvoice():
    Invoice_Method = 'INVOICE'  # 電子發票執行項目
    Invoice_Url = 'Invoice_Url'  # 電子發票執行網址
    MerchantID = ''
    HashKey = ''
    HashIV = ''

    def __init__(self):
        self.Send = {}
        self.TimeStamp = int(time.time())

    def Check_Out(self):
        arParameters = self.Send.copy()
        arParameters['MerchantID'] = self.MerchantID
        arParameters['RqHeader'] = {"Timestamp": self.TimeStamp}
        return ECPay_Invoice_Send.CheckOut(arParameters, self.HashKey, self.HashIV, self.Invoice_Method,
                                           self.Invoice_Url)


'''
送出資訊
'''


class ECPay_Invoice_Send():
    # 發票物件
    InvoiceObj = ''
    InvoiceObj_Return = ''

    '''
    背景送出資料
    '''

    @staticmethod
    def CheckOut(arParameters=dict, HashKey='', HashIV='', Invoice_Method='', ServiceURL=''):
        # 發送資訊處理
        arParameters = ECPay_Invoice_Send.process_send(arParameters, HashKey, HashIV, Invoice_Method)
        # API
        szStatus, szResult = ECPay_IO.ServerPost(arParameters, ServiceURL)
        # print("送出結果", szStatus, szResult)
        # 回傳資訊處理
        szResultJson = json.loads(szResult)
        if szStatus == 200 and "TransMsg" in szResultJson and szResultJson["TransMsg"] == "Success":
            arParameters_Return = ECPay_Invoice_Send.process_return(szResultJson, HashKey, HashIV, Invoice_Method)
            return arParameters_Return
        else:
            customReturnData ={
                **szResultJson,
                "Status": f'回傳狀態:{szStatus}',
            }
            return customReturnData

    '''
    資料過濾(送出)
    '''
    @staticmethod
    def process_send(arParameters=dict, HashKey='', HashIV='', Invoice_Method=''):
        # 宣告物件
        InvoiceMethod = 'ECPay_' + Invoice_Method
        class_str = globals()[InvoiceMethod]
        InvoiceObj = class_str()
        # 1寫入所有參數, 並把藥需要加密的資料回傳
        arParameters = Data_process.insert(InvoiceObj.parameters, InvoiceObj.encrypted_data, arParameters)
        # print("Parameters未加密:",arParameters)
        # 2把Data加密
        arParameters = Data_process.encrypt(arParameters, HashKey, HashIV)
        return arParameters

    '''
    資料過濾(回傳)
    '''

    @staticmethod
    def process_return(sParameters='', HashKey='', HashIV='', Invoice_Method=''):
        # 解密Data
        if Invoice_Method not in ['GET_ISSUE_LIST']:
            arEncryptedData = Data_process.decrypt(sParameters, HashKey, HashIV)
        else:
            arEncryptedData = sParameters["Data"]
        return arEncryptedData



'''
資料處理
'''

class Data_process():
    
    @staticmethod
    def insert(parameters=dict, encrypted_data=dict, arParameters=dict):
        for key, val in parameters.items():
            if key in arParameters:
                parameters[key] = arParameters[key]

        for key, val in encrypted_data.items():
            if key in arParameters:
                encrypted_data[key] = arParameters[key]
        parameters['Data'] = encrypted_data
        return parameters

    '''
    *v3版本加解密
    '''
    @staticmethod
    def encrypt(arParameters=dict, HashKey=str, HashIV=str):
        arEncryptedData_text = json.dumps(arParameters['Data'], separators=(",", ":"))
        arEncryptedData_text = urllib.parse.quote_plus(arEncryptedData_text)
        arEncryptedData_text  = ECPay_V3_Data.do_str_replace(arEncryptedData_text)
        # 加密處理        
        aes = AESCipher(key=HashKey, iv=HashIV)
        arParameters['Data'] = aes.encrypt(arEncryptedData_text).decode("utf-8")
        return arParameters
    
    @staticmethod
    def decrypt(arParameters=dict, HashKey=str, HashIV=str):
        # 解密處理
        aes = AESCipher(key=HashKey, iv=HashIV)
        data_decrypted = arParameters['Data']
        data_decrypted = aes.decrypt(data_decrypted)
        # 資料轉換
        data_decrypted = urllib.parse.unquote_plus(data_decrypted)
        data_decrypted = json.loads(data_decrypted)
        return data_decrypted


class ECPay_IO():

    @staticmethod
    def ServerPost(parameters, ServiceURL):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(ServiceURL, json=parameters, headers=headers)
        return r.status_code, r.text


class ECPay_V3_Data():
    '''
    *產生檢查碼
    '''
    def __init__(self, raw_data, hash_key, hash_iv) :
        self.raw_data = raw_data
        self.hash_key = hash_key
        self.hash_iv = hash_iv


    def encrypt (self):

        raw_data_text = json.dumps(self.raw_data, separators=(",", ":"))
        raw_data_text = urllib.parse.quote_plus(raw_data_text)
        raw_data_text = self.restore_str_replace(raw_data_text)


        aes = AESCipher(key=self.hash_key, iv=self.hash_iv)

        data_encrypted = aes.encrypt(raw_data_text).decode("utf-8")

        return data_encrypted

    @staticmethod
    def restore_str_replace(string):
        mapping_dict = {
            "-":"%2d",
            "_":"%5f",
            ".":"%2e",
            "!":"%21",
            "*":"%2a",
            "(":"%28",
            ")":"%29",
            "~":"%7e"
        }
        for key, val in mapping_dict.items():
            string = string.replace(key, val)

        return string
    @staticmethod
    def do_str_replace(string):
        mapping_dict = {
            "-":"%2d",
            "_":"%5f",
            ".":"%2e",
            "!":"%21",
            "*":"%2a",
            "(":"%28",
            ")":"%29",
            "~":"%7e"
        }
        for key, val in mapping_dict.items():
            string = string.replace(val, key)

        return string


class AESCipher:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    @staticmethod
    def __pad(text):
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    @staticmethod
    def __unpad(text):
        pad = ord(text[-1])
        return text[:-pad]

    def encrypt(self, raw):
        raw = self.__pad(raw)
        cipher = AES.new((self.key).encode("utf8"), AES.MODE_CBC, (self.iv).encode("utf8"))
        return base64.b64encode(cipher.encrypt(raw.encode('utf-8')))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        cipher = AES.new((self.key).encode("utf8"), AES.MODE_CBC, (self.iv).encode("utf8"))
        return self.__unpad(cipher.decrypt(enc).decode("utf-8"))