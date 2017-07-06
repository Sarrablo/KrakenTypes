from collections import namedtuple

class Time():
    def __init__(self, dictio):
        d_named = namedtuple("Time", dictio.keys())(*dictio.values())
        result = namedtuple("Result", d_named.result.keys())(*d_named.result.values())
        self.unix_time = result.unixtime
        self.date_time = result.rfc1123

class Assets():
    def __init__(self, dictio):
        d_named = namedtuple("Time", dictio.keys())(*dictio.values())
        self.assets = namedtuple("Assets", d_named.result.keys())(*d_named.result.values())

class AssetPairs():
    def __init__(self, dictio):
        for k,v in dictio.items():
            if isinstance(v,dict):
                self.__dict__[k] = AssetPairs(v)
            else:
                self.__dict__[k] = v
