
spam = ['apples','bananas','tofus',1,'cats']
# result should be apples,bananas,tofus and cats

# creating function
def functionList():
    name = ' '
    for i in range(len(spam) -1):
       name  += str(spam[i]) + ', '
    
    name += 'and ' + spam[-1]       
    print(name)
functionList()