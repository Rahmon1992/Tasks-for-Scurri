import re

# Patterns for all regular expressions
GENERAL_PATTERN = r'^([A-Z0-9]{3}|[A-Z0-9]{4})\ [A-Z0-9]{3}$'
AA9A_PATTERN = r'^(^(WC[12]|EC[1-4]|SW1)[ABEHMNPRVWXY]$|SE1P|NW1W)$'
A9A_PATTERN = r'^(E1W|N1[CP]|W1[ABCDEFGHJKPSTUW])$'
A9_PATTERN = r'^([BEGLMNSW][1-9])$'
A99_PATTERN = r'^([BEGLMNSW][1-9]\d)$'
AA9_PATTERN = r'^(((?!AB|LL|SO)[A-PR-UWYZ][A-HK-Y][1-9])|((BL|BS|CM|CR|FY|HA|PR|SL|SS)\d))$'
AA99_PATTERN  = r'^(((?!BR|FY|HA|HD|HG|HR|HS|HX|JE|LD|SM|SR|WC|WN|ZE)[A-PR-UWYZ][A-HK-Y][1-9]\d))$'

OUTWARDCODE_PATTERN = '|'.join((AA9A_PATTERN,A9A_PATTERN,A9_PATTERN,A99_PATTERN,AA9_PATTERN,AA99_PATTERN))
INWARDCODE_PATTERN = r'^ \d[A-BD-HJLNPQ-UW-Z]{2}$'

# Checking in this function Validation of the postcodes
def isValid(postcode):
    if (re.match(GENERAL_PATTERN, postcode)):
      if (re.match(OUTWARDCODE_PATTERN, postcode[:-4]) and re.match(INWARDCODE_PATTERN, postcode[-4:])):
        return True
      else:
        return False
    else:
        return False
