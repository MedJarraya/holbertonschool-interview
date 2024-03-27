#!/usr/bin/python3
"""
utf8 validation
"""


def validUTF8(data):
    """
utf8 validation
"""
    try:
        bytes([n & 255 for n in data]).decode("UTF-8")
        return True
    except Exception:
        return False
