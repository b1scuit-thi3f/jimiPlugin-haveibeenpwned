# jimiPlugin: haveibeenpwned

A JIMI Plugin for querying HaveIBeenPwned and PwnedPasswords

Currently the following actions are available:

* haveibeenpwnedBreaches - returns breaches contained within the haveibeenpwned database
* haveibeenpwnedBreachedAccount* - returns data about any breaches related to the specified account
* haveibeenpwnedBreach - returns a specific breach, based on the name provided
* haveibeenpwnedPastes* - returns data about any pastes related to the specified account
* haveibeenpwnedPasswords - returns a count for how many times the provided password has been seen. This can be hashed (sha-1) or not.

\* requires an API key, this can be purchased via https://haveibeenpwned.com/API/Key
