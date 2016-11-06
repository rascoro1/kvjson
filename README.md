# kvjson
Dealing with Key Value Lists in Json

```python
from kvjson

# Encoding Python Dictionary into JSON Key Value List
new_dict = {'firstname': 'Andrew', 'middlename': 'James', 'username': 'rascoro1'}
kv_json = kvjson.dumps(new_dict)
print(kv_json)
[{"Key": "middlename", "Value": "James"}, {"Key": "username", "Value": "rascoro1"}, {"Key": "firstname", "Value": "Andrew"}]

# Add Key and Value from JSON String
kv_json = kvjson.add(kv_json, 'key', 'value')

# Decoding JSON Key Value List into Python Dictionary
kv_dict = kvjson.loads(kv_json)
print(kv_dict)
{'middlename': 'James', 'username': 'rascoro1', 'firstname': 'Andrew', 'key': 'value'}



```
