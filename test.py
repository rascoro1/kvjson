import kvjson

# Encoding Python Dictionary into JSON Key Value List
new_dict = {'firstname': 'Andrew', 'middlename': 'James', 'username': 'rascoro1'}
kv_json = kvjson.dumps(new_dict)
print(kv_json)

# Add Key and Value to JSON String
kv_json = kvjson.add(kv_json, 'key', 'value')

# Decoding JSON Key Value List into Python Dictionary
kv_dict = kvjson.loads(kv_json)
print(kv_dict)