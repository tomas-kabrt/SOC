__author__ = 'chris'
from requests.auth import AuthBase
import time
import hmac
import hashlib
import re

class DtAuth(AuthBase):

    __prit=''
    __pubt=''

    def __init__(self, pubtoken, pritoken):
        # setup any auth-related data here
        self.__prit = pritoken
        self.__pubt = pubtoken


    def __call__(self, r):

        from datetime import datetime

        d = datetime.utcnow()
        now = d.strftime('%Y%m%dT%H%M%S')
        # print(now)
        fullquery=re.search(r'(/.+)', r.url[len('https://'):]).group(1) #find the full URL after the hostname (path+params)
        # print(fullquery)
        if r.method=='POST' and len(r.body)>0:
            maccer = hmac.new(self.__prit.encode('ASCII'), (fullquery+'?'+r.body+'\n'+self.__pubt+'\n'+now).encode('ASCII'), hashlib.sha1)
        else:
            maccer = hmac.new(self.__prit.encode('ASCII'), (fullquery+'\n'+self.__pubt+'\n'+now).encode('ASCII'), hashlib.sha1)
        sig = maccer.hexdigest()
        r.headers.update({'DTAPI-Token': self.__pubt, 'DTAPI-Date': now, 'DTAPI-Signature': sig})
        # print(r.headers)
        return r

