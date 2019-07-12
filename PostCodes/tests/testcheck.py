from ukpostcodes import validate

# Using pytest for testing
# Randomly generated postal codes: First 10 are correct and another 10 with mistakes
def test_postcodes():
    assert validate.isValid('SA70 7EA') == True
    assert validate.isValid('WN5 7LU') == True
    assert validate.isValid('SA64 0HH') == True
    assert validate.isValid('SW10 9JH') == True
    assert validate.isValid('BA16 9LD') == True
    assert validate.isValid('S74 0LD') == True
    assert validate.isValid('SP3 4BX') == True
    assert validate.isValid('PH13 9NF') == True
    assert validate.isValid('PL34 0HJ') == True
    assert validate.isValid('LL42 1SU') == True
    assert validate.isValid('AB4 3LV') == False
    assert validate.isValid('W43SQ') == False
    assert validate.isValid('CO43SQAVCC') == False
    assert validate.isValid('CO4 A') == False
    assert validate.isValid('ca23 4A') == False
    assert validate.isValid('FF224 34A') == False
    assert validate.isValid('G23A RA') == False
    assert validate.isValid('AAAAAAA') == False
    assert validate.isValid('5555555') == False
    assert validate.isValid('AAA 555') == False
