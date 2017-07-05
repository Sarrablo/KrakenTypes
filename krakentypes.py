from collections import namedtuple

class Time():
    def __init__(self, dictio):
        d_named = namedtuple("Time", dictio.keys())(*dictio.values())
        result = namedtuple("Result", d_named.result.keys())(*d_named.result.values())
        self.unix_time = result.unixtime
        self.date_time = result.rfc1123

