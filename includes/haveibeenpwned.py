import requests, json, hashlib
from pathlib import Path

class _haveibeenpwned():
    url = "https://haveibeenpwned.com/api/v3"
    
    def __init__(self, apiKey=None, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None
        self.headers = {"user-agent" : "jimi-automation"}
        if apiKey is not None:
            self.headers["hibp-api-key"] = apiKey

    def apiCall(self,service,value="",parameters=""):
        kwargs={}
        kwargs["timeout"] = self.requestTimeout
        kwargs["headers"] = self.headers
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            response = requests.get("{0}/{1}/{2}?{3}".format(self.url,service,value,parameters), **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200:
            return json.loads(response.text), response.status_code
        return response.text, response.status_code

    def getAccountBreaches(self,account,parameters=""):
        response, statusCode = self.apiCall("breachedaccount",account,"&".join(parameters))
        return response, statusCode

    def getAllBreaches(self,parameters=""):
        response, statusCode = self.apiCall("breaches","","&".join(parameters))
        return response, statusCode

    def getBreach(self,breach):
        response, statusCode = self.apiCall("breach",breach)
        return response, statusCode

    def getDataclasses(self):
        response, statusCode = self.apiCall("dataclasses")
        return response, statusCode

    def getAccountPastes(self,account):
        response, statusCode = self.apiCall("pasteaccount",account)
        return response, statusCode