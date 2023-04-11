#!/usr/bin/python3
''' function that returns the list
'''                                                                                                                                                                                                                                                                                                                                                             def lookup(obj):
    attrs = dir(obj)
    methods = [attr for attr in attrs if callable(getattr(obj, attr))]
    return attrs + methods
