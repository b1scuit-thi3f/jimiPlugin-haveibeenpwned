import requests, json, hashlib
from pathlib import Path

class _pwnedpasswords():
    url = "https://api.pwnedpasswords.com"
    
    def __init__(self, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None
        self.headers = {"user-agent" : "jimi-automation"}

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
            return response.text.split("\r\n"), response.status_code
        return response.text, response.status_code    
    
    def pwnedPassword(self,hashedPass,hashed=True):
        if hashed == False:
            hashedPass = hashlib.sha1(hashedPass.encode()).hexdigest().upper()
        else:
            hashedPass = hashedPass.upper()
        response, statusCode = self.apiCall("range",hashedPass[0:5])
        newResponse = {hashedPass:0}
        for returnedHashes in response:
            if hashedPass in "{}{}".format(hashedPass[0:5],returnedHashes.split(":")[0]):
                newResponse = {hashedPass:returnedHashes.split(":")[1]}
        return newResponse, statusCode