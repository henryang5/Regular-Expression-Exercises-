"""
Henry Ang
1/20/16
CSC 4800
Regular Expression Testing
Exercise 1-4: Match the set of all valid python identifiers
"""

from RETest import regularExpressionTest

def testPythonIdentifers():
    """
    Test if python identifiers are valid
    # Match if:
    # Upper and Lower case a-z, A-z
    # Digits 0-9
    # Can't start with digit
    """
    print("Test Python Identifers")

    patt = "^(?!\d)[A-Za-z0-9_]*$"

    print("Pattern: " + patt )
    print()
    regularExpressionTest(patt, 'strings')
    regularExpressionTest(patt, 'INTEGER')
    regularExpressionTest(patt, 'double2')
    regularExpressionTest(patt, 'abc_123')
    regularExpressionTest(patt, 'Python_')
    regularExpressionTest(patt, '_qwerty')
    print()
    regularExpressionTest(patt, 'my SQL ')
    regularExpressionTest(patt, '4251234')
    print()

if __name__ == "__main__":
    testPythonIdentifers()