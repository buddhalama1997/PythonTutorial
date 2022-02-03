# import regular expression

import re

# Regular Expression
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Input for Regex
message = 'Call me at 415-555-1011 tomorrow.'

# Applying Regex and search the given criteria
mo = phoneNumRegex.search(message)

print('Phone number found: ' + mo.group())

phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

mo = phoneNumRegex1.search(message)
areaCode, mainNumber = mo.groups()
print(mo.group())
print(mo.group(0))

print(mo.group(1))

print(mo.group(2))

print(areaCode)
print(mainNumber)

phoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
message2= 'Call me at (415) 555-1011 tomorrow.'

mn = phoneNumRegex2.search(message2)

print(mn.group())
print(mn.group(0))

print(mn.group(1))

print(mn.group(2))