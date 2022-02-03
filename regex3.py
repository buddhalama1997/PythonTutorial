#Implementaton of Regex
# Matching Multiple Groups with the pipe


import re
# matches either Bataman or Tina Frey
heroRegex = re.compile(r'Batman|Tina Frey')

heroName = 'Batman and Tina Frey'

# Whhen there is both the matches but return only the first match
findHero = heroRegex.search(heroName) 

# print the matched value

print(findHero.group())

heroName1 = 'Tina Frey and Batman'

findHero1 = heroRegex.findall(heroName1) 
print(findHero1)



batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

message1 = 'Batman has a Batmobile.'

mo = batRegex.search(message1)

print(mo.group())
print(mo.group(0))
print(mo.group(1))

bat = batRegex.findall(message1)

print(bat)