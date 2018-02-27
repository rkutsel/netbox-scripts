AWS Direct-Connect set up | Python 2.7 and 3.5. Python 3.5 or higher is recommended
--------------------------------

First step is to install dependencies. Run:
```
pip3 install -r requirements.txt --upgrade
```
Then modify apy.py file by putting your [NetBox Token](https://netbox.readthedocs.io/en/latest/api/authentication/):
```
headers = {'Authorization': 'Token 11111111111111111111111'}
```

At this point you should be good to go. The only information you'll need are AWS account number && name of the AWS virtual interface(s).

The assumption here is that there's two environments: PROD & STAGE with preallocated prefixes: 169.254.0.0/20 for STAGE & 169.254.16.0/20 for PROD. You can easily expand/modify that functionality by adding another function(s) in api.py for as many environments as you have.
