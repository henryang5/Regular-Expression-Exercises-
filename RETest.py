"""
Henry Ang
1/20/16
CSC 4800
Regular Expression Testing
"""

import re

def regularExpressionTest(patt, s):
    """
    Regular Expression test function.
    :param patt:
    :param s:
    """
    print("('" + s  + "')"+ ": ".format(s), end="")           # outputs the test string
    m = re.match(patt, s, flags=re.VERBOSE)     # performs the match, VERBOSE: white space ignored
    if m is not None: print(m.group())          # output the result
    else: print("No match")



