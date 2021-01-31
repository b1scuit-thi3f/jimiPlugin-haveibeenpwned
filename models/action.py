import jimi
from plugins.haveibeenpwned.includes import haveibeenpwned, pwnedpasswords

class _haveibeenpwnedBreaches(jimi.action._action):
    domain = str()
    
    def run(self,data,persistentData,actionResult):
        domain = jimi.helpers.evalString(self.domain,{"data" : data})      

        pwnedApi = haveibeenpwned._haveibeenpwned()
        result, statusCode = pwnedApi.getAllBreaches(parameters=["domain={}".format(domain)])
        
        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from haveibeenpwned API"
        return actionResult 

class _haveibeenpwnedBreachedAccount(jimi.action._action):
    domain = str()
    truncateResponse = bool()
    includeUnverified = bool()
    account = str()
    apiKey = str()
    
    def run(self,data,persistentData,actionResult):
        domain = jimi.helpers.evalString(self.domain,{"data" : data})
        account = jimi.helpers.evalString(self.account,{"data" : data})  
        
        if not hasattr(self,"plain_apiKey"):
            self.plain_apiKey = jimi.auth.getPasswordFromENC(self.apiKey)       

        pwnedApi = haveibeenpwned._haveibeenpwned(self.plain_apiKey)
        result, statusCode = pwnedApi.getAccountBreaches(account,parameters=["domain={}".format(domain),"truncateResponse={}".format(self.truncateResponse),"includeUnverified={}".format(self.includeUnverified)])
        
        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from haveibeenpwned API"
        return actionResult 

    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_haveibeenpwnedBreachedAccount, self).setAttribute(attr,value,sessionData=sessionData)

class _haveibeenpwnedBreach(jimi.action._action):
    breachName = str()
    
    def run(self,data,persistentData,actionResult):
        breachName = jimi.helpers.evalString(self.breachName,{"data" : data})      

        pwnedApi = haveibeenpwned._haveibeenpwned()
        result, statusCode = pwnedApi.getBreach(breachName)
        
        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from haveibeenpwned API"
        return actionResult 

class _haveibeenpwnedPastes(jimi.action._action):
    account = str()
    apiKey = str()
    
    def run(self,data,persistentData,actionResult):
        account = jimi.helpers.evalString(self.account,{"data" : data})  

        if not hasattr(self,"plain_apiKey"):
            self.plain_apiKey = jimi.auth.getPasswordFromENC(self.apiKey)   

        pwnedApi = haveibeenpwned._haveibeenpwned(self.plain_apiKey)
        result, statusCode = pwnedApi.getAccountPastes(account)
        
        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from haveibeenpwned API"
        return actionResult 
        
    def setAttribute(self,attr,value,sessionData=None):
        if attr == "apiKey" and not value.startswith("ENC "):
            if jimi.db.fieldACLAccess(sessionData,self.acl,attr,accessType="write"):
                self.apiKey = "ENC {0}".format(jimi.auth.getENCFromPassword(value))
                return True
            return False
        return super(_haveibeenpwnedPastes, self).setAttribute(attr,value,sessionData=sessionData)

class _haveibeenpwnedPasswords(jimi.action._action):
    password = str()
    isHashed = bool()
    
    def run(self,data,persistentData,actionResult):
        password = jimi.helpers.evalString(self.password,{"data" : data})  

        pwnedApi = pwnedpasswords._pwnedpasswords()
        result, statusCode = pwnedApi.pwnedPassword(password,self.isHashed)
        
        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from pwnedpasswords API"
        return actionResult 