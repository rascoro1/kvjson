import json
import sys

"""
KV pairs

load: returns KV from dictionary
dumps:
"""


def dumps(dict_data):
    """
    Encoding Python Dictionary

    :param dict_data: [Dictionary] The dictionary you would like in Key Value Form
    :returns: [String] Json object of the Dictionary in Key Value form
    """
    kvs = []
    if isinstance(dict_data, dict):
        for key in dict_data:
            kv = {'Key': key, 'Value': dict_data[key]}
            kvs.append(kv)
    else:
        print("To dump data it must be in Dictionary Type")

    return json.dumps(kvs)

def loads(kv_data):
    """
    Decoding Key Value Json String

    :param kv_data: [String] JSON String representing the Key Value information
    :return: [Dictionary] Returns the JSON in dictionary form
    """
    dict_kv = {}
    if isinstance(kv_data, str):
        kvs =  json.loads(kv_data)
        for kv in kvs:
            dict_kv[kv['Key']] = kv['Value']
    else:
        print("To load Key Value Data it must be String Type")

    return dict_kv

def remove(kv_data, key):
    """
    Remove Key from a Key Value pair
    Can be performed on Dictionary or Json key value string
    :param kv_data: [Dictionary/String] The Key Value data that needs something removed
    :param key: [String] Name of the key of the Vey Value pair to remove
    :return: Returns the data given with the removed Key Value Pair in the given type
    """
    if isinstance(kv_data, str):
        kv_data = loads(kv_data) # Turn into Dictionary
        try:
            del kv_data[key]
        except NameError:
            print(key, " does not exists in key value pair.")
        kv_data = dumps(kv_data)
    else:
        print("Provide a Json Key Value String")
        sys.exit(6)
    return kv_data

def add(kv_data, key, value):
    """
    This will add a key, if key already exists it will overwrite
    :param kv_data:
    :param key:
    :param value:
    :return:
    """
    if isinstance(kv_data, str):
        kvs = loads(kv_data) # Turn json into dictionary
        kvs[key] = value # Add key
        kvs = dumps(kvs) # Turn back into json Key Value String
    else:
        print("Provide A JSON Key Value String")

    return kvs

def contains_value(kv_json, value):
    """
    If JSON Key Value, Value contains this value

    :param kv_json: [String] JSON Key Value String
    :param value: The value you are searching for inisde the JSON Key Value String
    :return: [Boolean] If the Value is in the JSON Key Value String
    """
    if isinstance(kv_json, str):
        kv_dict = loads(kv_json)
        for key in kv_dict:
                if kv_dict[key] == value: # Found value in dictionary
                    return True
        return False
    else:
        print("Provide A JSON Key Value String")

def contains_key(kv_json, key):
    """
    If the JSON Key Value Pair conatins a specific key

    :param kv_json: [String] JSON Key Value String
    :param key: The key that is conatined in kv_json
    :return: [Boolean] If key is found in JSON Key Value String
    """
    if isinstance(kv_json, str):
        kv_dict = loads(kv_json)
        try:
            res = kv_dict[key]
            return True
        except KeyError:
            return False
    else:
        print("Provide A JSON Key Value String")

def equals(kv_data, kv_data2):
    """
    Checks if the JSON Key Value String are equal

    :param kv_data: [String] JSON Key Value String
    :param kv_data2: [String] JSON Key Value String
    :return: [Boolean] Returns if the two strings are equal
    """
    kv_dict1 = loads(kv_data)
    kv_dict2 = loads(kv_data2)
    if kv_dict1 == kv_dict2:
        return True
    return False