
def createDictionary():
    '''Returns a tiny swahili dictionary'''
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
    numberFormat = "Count in swa: {one}, {two}, {three}, ..."
    withSubstitutions = numberFormat.format(**dictionary)
    print(withSubstitutions)
    print("swa colors: {red}, {blue}, {green}, ...".format(**dictionary))
    
main() # run the program
