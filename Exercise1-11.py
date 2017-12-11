"""
Henry Ang
1/20/16
CSC 4800
Regular Expression Testing
Exercise 1-11: Match the set of all valid email addresses
"""

from RETest import regularExpressionTest

def testEmailAddresses():
    """
    Test if email address is valid

    Match if:

    Acceptable email prefix formats
    Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
    An underscore, period, or dash must be followed by one or more letter or number.

    Acceptable email domain formats
    Allowed characters: letters, numbers, dashes.
    The last portion of the domain must be at least two characters, for example: .com, .org, .cc
    """
    print("Test Email Addresses")

    patt = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,6})$"

    print("Pattern: " + patt)
    print()
    regularExpressionTest(patt, 'myEmail@gmail.com')
    regularExpressionTest(patt, 'spu-cs@edu.com')
    regularExpressionTest(patt, '12seahawks@yahoo.us')
    regularExpressionTest(patt, 'white.House@cia.cc')
    regularExpressionTest(patt, 'tom_brady@football.nfl')
    print()
    regularExpressionTest(patt, 'C++@java.python')
    regularExpressionTest(patt, 'CEO@.co')
    regularExpressionTest(patt, 'google@gmail.-go')
    print()

if __name__ == "__main__":
    testEmailAddresses()