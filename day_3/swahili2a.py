
def createDictionary():
    '''Returns a tiny swa dictionary'''
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
    print('Count in swa: ' + dictionary['one'] + ', ' +
          dictionary['two'] + ', ' +dictionary['three'] + ', ...')
    print('swa colors: ' + dictionary['red'] + ', ' +
          dictionary['blue'] + ', ' +dictionary['green'] + ', ...')

main() # run the program
