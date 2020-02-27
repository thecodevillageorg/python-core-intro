swa = dict()
swa['hello'] = 'niaje'
swa['yes'] = 'ndio'
swa['one'] = 'moja'
swa['two'] = 'mbili'
swa['three'] = 'tatu'
swa['red'] = 'nyekundu'
swa['black'] = 'nyeusi'
swa['green'] = 'kijani'
swa['blue'] = 'blue'

'''
Access Ite
'''
x = swa["hello"]
print(x)


'''
Using the .get() method
'''

x = swa.get('hello')

print(x)

'''
Changing values in a Dict()
'''

swa['hello'] = 'Mambo vipi'

x= swa.get('hello')
print(x)

'''
LOOP THROUGH A DICT e.g for loop

'''

'''
print key names
'''

for k in swa:
    print(k)


'''
print values
'''

for k in swa:
    print(swa[k])


'''
Get values with .values() function
'''
for v in swa.values():
    print(v)

'''
Get Keys and values with .items() function
'''

for k, v in swa.items():
    print(k,'\t',v)


'''
Check if Key Exists
'''

if 'hello' in swa:
    print("Yes 'hello' Exists ")
else:
    print("No 'hello' does not exist ")


'''
Length of dict with .len()
'''

print(len(swa))

'''
Remove Items pop(), popitem() in versions before 3.7, a random item is removed instead, del 
'''

'''
pop() //remove item with key specified
'''

swa.pop('hello')

print(swa)


'''
popitem() 

removes the last inserted item
NB: in versions before 3.7 - random item is removed instead
'''

swa.popitem()
print(swa)
print(len(swa))


'''
del keyword

deletes with specified keyname
NB: can also delete dictonary completely.

'''

del swa["green"]
print(len(swa))

'''
clear() //empties the dictionary
'''

swa.clear() 
print(len(swa))


'''
delete dictionary del
'''

##del swa
#print(len(swa))


'''
copy a dictionary

You cannot copy a dictionary simply by typing dict2 = dict1, 
Reason : dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

Soln: use the built-in Dictionary method 

    - copy()

    - dict()

'''

newswadict = swa.copy()
print(newswadict)

newswadict1 = dict(swa)
print(newswadict1)













