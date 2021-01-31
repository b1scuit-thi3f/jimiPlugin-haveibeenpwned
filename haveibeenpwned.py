import jimi

class _haveibeenpwned(jimi.plugin._plugin):
    version = 0.1
    jimiMinVersion = 1.8

    def install(self):
        # Register models
        jimi.model.registerModel("haveibeenpwnedBreaches","_haveibeenpwnedBreaches","_action","plugins.haveibeenpwned.models.action")
        jimi.model.registerModel("haveibeenpwnedBreachedAccount","_haveibeenpwnedBreachedAccount","_action","plugins.haveibeenpwned.models.action")
        jimi.model.registerModel("haveibeenpwnedBreach","_haveibeenpwnedBreach","_action","plugins.haveibeenpwned.models.action")
        jimi.model.registerModel("haveibeenpwnedPastes","_haveibeenpwnedPastes","_action","plugins.haveibeenpwned.models.action")
        jimi.model.registerModel("haveibeenpwnedPasswords","_haveibeenpwnedPasswords","_action","plugins.haveibeenpwned.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("haveibeenpwnedBreaches","_haveibeenpwnedBreaches","_action","plugins.haveibeenpwned.models.action")
        jimi.model.deregisterModel("haveibeenpwnedBreachedAccount","_haveibeenpwnedBreachedAccount","_action","plugins.haveibeenpwned.models.action")
        jimi.model.deregisterModel("haveibeenpwnedBreach","_haveibeenpwnedBreach","_action","plugins.haveibeenpwned.models.action")
        jimi.model.deregisterModel("haveibeenpwnedPastes","_haveibeenpwnedPastes","_action","plugins.haveibeenpwned.models.action")
        jimi.model.deregisterModel("haveibeenpwnedPasswords","_haveibeenpwnedPasswords","_action","plugins.haveibeenpwned.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        pass