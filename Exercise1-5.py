"""
Henry Ang
1/20/16
CSC 4800
Regular Expression Testing
Exercise 1-5: Match a street address according the the american format
              3307 3rd
              3307 3rd West
              1180 Bordeaux Drive
              3210 De la Cruz Boulevard
"""

from RETest import regularExpressionTest

def testStreetAddress():
    """
    Test if street address matches the American format
    # Match if:
    # House Number: 0-9 [1-6 digits]
    # Street: Aa-z (First letter Capitalized) or 0-9[1-4 digits]
    # Street, Drive, Avenue, Boulevard,
    # N, E, S, W, NE, SE, SW, NW
    """
    print("Test Street Addresses")

    patt = "^\d(([A-Za-z0-9.-]+[ ])+)|" \
           "(Avenue|Lane|Road|Boulevard|Drive|Street|Ave|Dr|Rd|Blvd|Ln|St|N|E|S|W|NE|SE|SW|NW)$"

    print("Pattern: " + patt)
    print()
    regularExpressionTest(patt, '3307 3rd')
    regularExpressionTest(patt, '3307 3rd West')
    regularExpressionTest(patt, '1180 Bordeaux Drive')
    regularExpressionTest(patt, '3210 De la Cruz Boulevard')
    regularExpressionTest(patt, '12345 N')
    print()
    regularExpressionTest(patt, '5343_Oak')
    regularExpressionTest(patt, 'Oak Street')
    print()

if __name__ == "__main__":
    testStreetAddress()