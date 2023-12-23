# Note: this implementation of the algorithm is based on writing by row and reading by column

def columnarEncrypt(plainText,key,ignore_special_chars=True,padding=''):
    '''
    This function encrypt the plain text using Columnar cipher.
    key parameter for encryption key(Not optional).
    ignore_special_chars parameter to specify wether to ignore the special chars or not (By default True).
    padding parameter to specify the padding character (By default '').
    '''
    if not key.isalnum():
        raise ValueError(f'Invalid key: {key}')

    # Processing the plaintext
    if ignore_special_chars:
        plainText = ''.join([i if i.isalnum() else '' for i in plainText])
    plainText = plainText.upper()
    key = key.upper()
    size = len(key)
    plainText += padding * (size - len(plainText) % size) if len(plainText) % size else ''
    if padding == '':
        plainText += '_' * (size - len(plainText) % size) if len(plainText) % size else ''
    matrix = []

    # Encryption
    sortedKey = ''.join(sorted(key))
    for i in range(0,len(plainText),size):
        row = [''] * size
        substr = plainText[i:i+size]
        dictKey = {}
        for idx,val in enumerate(sortedKey):
            dictKey.setdefault(val,idx)
        for idx,val in enumerate(key):
            row[dictKey[val]] = substr[idx]
            dictKey[val] += 1
        if padding == '':
            for j in range(len(row)):
                row[j] = '' if row[j] == '_' else row[j]
        matrix.append(row)
    # Processing the output
    trasposedMatrix = list(zip(*matrix))
    cipherText = [''.join(i) for i in trasposedMatrix]

    return ''.join(cipherText)

def columnarDecrypt(cipherText,key,ignore_special_chars=True,padding=''):
    '''
    This function decrypt the cipher text using Columnar cipher.
    key parameter for decryption key(Not optional).
    ignore_special_chars parameter to specify wether to ignore the special chars or not (By default True).
    padding parameter to specify the padding character (By default '').
    '''
    if not key.isalnum():
        raise ValueError(f'Invalid key: {key}')
    if padding != '' and len(cipherText) % len(key):
        raise ValueError('Invalid padding: No padding specified!')
    
    # Processing the cipherText
    if ignore_special_chars:
        cipherText = ''.join([i if i.isalnum() else '' for i in cipherText])
    cipherText = cipherText.upper()
    key = key.upper()
    cipherTextLen = len(cipherText)
    size = len(key)

    numberOfCols = (cipherTextLen + size - 1) // size # ceil with intger division
    trasposedMatrix = [''] * size
    currentRow = size
    numberOfPads = (size - cipherTextLen % size) if cipherTextLen % size else 0

    # Procesing the matrix as it's transposed and transposed it again to get the final matrix
    sortedKey = ''.join(sorted(key))
    dictKey = {}
    for idx,val in enumerate(sortedKey):
            dictKey.setdefault(val,idx)
    newKey = []
    for ele in key:
        newKey.append(dictKey[ele])
        dictKey[ele] += 1
    newDictKey = {}
    for idx,val in enumerate(newKey):
        newDictKey.setdefault(val,idx)
    # Note that until here we get the key right! and the deleted code in the test file
    
    i = portion = 0
    while i < cipherTextLen:
        if portion >= size - numberOfPads and padding == '':
            substr = cipherText[i:i + numberOfCols - 1]
            i += numberOfCols - 1
        else:
            substr = cipherText[i: i + numberOfCols]
            i += numberOfCols
        row = list(substr)
        if padding == '':
            row.append('')
        trasposedMatrix[newDictKey[portion]] = row
        portion += 1
    
    matrix = list(zip(*trasposedMatrix))
    plainText = ''.join([''.join(row) for row in matrix])
    for i in range(cipherTextLen-1,-1,-1):
        if plainText[i] != padding:
            break
    return plainText



