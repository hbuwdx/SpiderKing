#-*-coding:utf-8-*-
import hashlib


def to_md5_str(argument):
    h = hashlib.md5()
    h.update(argument)
    return h.hexdigest()