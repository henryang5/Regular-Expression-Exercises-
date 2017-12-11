"""
Henry Ang
1/20/16
CSC 4800
Regular Expression Testing
Exercise 1-6: Match simple web domains that begins with www. and ends with .com
"""

from RETest import regularExpressionTest

def testWebDomain():
    """
    Test if web domain is valid.
    # Match if:
    # begins with www. and ends with .com
    # Characters should only be a-z | A-Z | 0-9 and period(.) and dash(-)
    #The domain name part should not start or end with dash (-) (e.g. -google-.com)
    #The domain name part should be between 1 and 63 characters long
    """
    print("Test Web Domains")

    patt = "^www.((?!-)[a-zA-Z]{0,62}(?!-).com | (?!-)[a-zA-Z0-9-]{0,62}(?<!-).com)$"

    print("Pattern: " + patt)
    print()
    regularExpressionTest(patt, 'www.goog-le.com')
    regularExpressionTest(patt, 'www.123456.com')
    print()
    regularExpressionTest(patt, '-www.yahoo.com')
    regularExpressionTest(patt, 'www.facebook.com-')
    regularExpressionTest(patt, 'bing.com')
    regularExpressionTest(patt, 'www.apple.')
    regularExpressionTest(patt, 'www.spu.edu')
    regularExpressionTest(patt, 'www.-youtube.com')
    regularExpressionTest(patt, 'www.twitch-.com')
    print()

if __name__ == "__main__":
    testWebDomain()