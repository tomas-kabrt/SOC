from DtAuth import DtAuth
import requests
import warnings

'''
Basic class to simplify access to some of the Darktrace API
'''
class DtAPI:

    __server=r'https://darktrace'
    __dtsign=None
    __sess=None

    def __init__(self, server, pubtoken, pritoken):
        self.__server = server
        self.__dtsign = DtAuth(pubtoken=pubtoken, pritoken=pritoken)

    def __apicall(self, url, postdata=False):
         #prevent unverified SSL warnings
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", message="Unverified HTTPS.*")

            if self.__sess==None:
                self.__sess=requests.Session()
                self.__sess.auth=self.__dtsign

            # Do not verify since DT probably has self-signed cert
            if postdata:
                r=self.__sess.post(self.__server+url, data=postdata, verify=False,
                                headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"})
            else:
                r=self.__sess.get(self.__server+url, verify=False)
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception(r.status_code, r.text)

    def getModelBreaches(self, params):
        url = '/modelbreaches'
        if len(params)>0:
            url+='?'+params
        return self.__apicall(url)

    def getStatus(self, includeProbes=True):
        url='/status'
        if includeProbes:
            url+='?includeprobes=true'
        return self.__apicall(url)

    def appendWatchedList(self, list):
        url='/intelfeed'
        self.__apicall(url, postdata='addlist='+list)

    def getWatchedList(self):
        url='/intelfeed'
        return self.__apicall(url)

    def deleteFromWatchedList(self, entry):
        url='/intelfeed'
        self.__apicall(url, postdata='removeentry='+entry)

    def getDeviceDetails(self, did):
        url='/devices?did={}'.format(did)
        return self.__apicall(url)

    def getDeviceByIP(self, ip):
        url = '/devices?ip=' + ip
        return self.__apicall(url)

    def getDetails(self, params):
        url='/details'
        if len(params)>0:
            url+='?'+params
        return self.__apicall(url)

    def acknowledgeModelBreach(self, pbid):
        url='/acknowledgeevent'
        return self.__apicall(url, postdata='pbid='+pbid)

    def unacknowledgeModelBreach(self, pbid):
        url='/unacknowledgeevent'
        return self.__apicall(url, postdata='pbid='+pbid)
