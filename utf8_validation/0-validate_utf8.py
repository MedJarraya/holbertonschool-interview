#!/usr/bin/python3
"""
utf8 validation
"""


from codecs import decode


def validUTF8(data):
    """utf8 validation"""
    try:
        decoded_data = decode(bytes(data), 'utf-8')
        return True
    except ValueError:
        return False
