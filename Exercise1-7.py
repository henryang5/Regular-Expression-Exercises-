"""
Henry Ang
1/20/16
CSC 4800
Regular Expression Testing
Exercise 1-7: Match string repesentation of all python integer literals
"""

from RETest import regularExpressionTest

def testIntegerLiterals():
    """
    Test if string repesentation python integer literals is valid.
    Match if:
    integer      ::=  decinteger | bininteger | octinteger | hexinteger
    decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
    bininteger   ::=  "0" ("b" | "B") (["_"] bindigit)+
    octinteger   ::=  "0" ("o" | "O") (["_"] octdigit)+
    hexinteger   ::=  "0" ("x" | "X") (["_"] hexdigit)+
    nonzerodigit ::=  "1"..."9"
    digit        ::=  "0"..."9"
    bindigit     ::=  "0" | "1"
    octdigit     ::=  "0"..."7"
    hexdigit     ::=  digit | "a"..."f" | "A"..."F"
    """
    print("Test Integer Literals")

    patt = "[1-9]+ | 0b[0-1]+ | 0o[0-7]+ | 0x[0-9a-fA-F]+"

    print("Pattern: " + patt)
    print();
    regularExpressionTest(patt, '0b1010101')
    regularExpressionTest(patt, '0x1234567')
    regularExpressionTest(patt, '0xabdefAB')
    regularExpressionTest(patt, '0o012345')
    regularExpressionTest(patt, '12312353')
    regularExpressionTest(patt, '0xgFGd')
    regularExpressionTest(patt, '0b2345')
    regularExpressionTest(patt, '0o99999')

    print()

if __name__ == "__main__":
    testIntegerLiterals()