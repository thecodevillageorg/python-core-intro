
def createDictionary():
    '''Returns a tiny Swahili dictionary'''
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
    return swa

def main():
    dictionary = createDictionary()
    print(dictionary['two'])
    print(dictionary['red'])

main()
