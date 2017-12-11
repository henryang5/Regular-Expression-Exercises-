"""
Henry Ang
1/20/16
CSC 4800
Regular Expression Testing
Exercise 1-12: Match the set of all valid web site addresses (URL)
"""

from RETest import regularExpressionTest

def testWebsiteAddresses():
    """
    Test if website address (URL) is valid
    Match if:
    Contains: A-Z a-z 0-9-._~:/?#[]@!$&'()*+,;=`.
    Starts with http://www.
    Domain: # A-Z a-z 0-9
    # can ends in .com .org. net. gov .edu .co
    """
    print("Test Website Addresses (URL)")
    patt = "(http://|https://)((?!-)[A-Za-z0-9.-]{0,62}(?!-).[a-zA-Z]{2,6}?([A-Za-z0-9.-/]) |" \
           "(?!-)[A-Za-z0-9.-/]{0,62}(?<!-).[a-zA-Z]{2,6}?[A-Za-z0-9.-/])"

    print("Pattern: " + patt)
    print()
    regularExpressionTest(patt, 'http://google.com')
    regularExpressionTest(patt, 'http://apple.com/i_phone')
    regularExpressionTest(patt, 'http://wiki.com/blah_blah_(wikipedia)')
    regularExpressionTest(patt, 'https://www.example.com/foo/?bar=baz&inga=42&quux')
    regularExpressionTest(patt, 'http://1337.net')
    print()
    regularExpressionTest(patt, 'http://10111')
    regularExpressionTest(patt, 'httpa://domainskdls123.e')
    regularExpressionTest(patt, 'www.-.com')
    print()

if __name__ == "__main__":
    testWebsiteAddresses()