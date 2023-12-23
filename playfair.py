import string
def playfaireEncrypt(plainText,key,mode=0):
    '''
    This function encrypt the plain text using Playfaire cipher.
    key parameter for encryption key(Not optional).
    mode parameter for encryption mode(By Default 0).
    mode -> 0 only alpha letters are acceptable.
    mode -> 1 if there is non-alpha letters will ignore it from both plain text and key.
    '''
    match mode:
        case 0:
            if not plainText.isalpha():
                raise ValueError(f'Invalid plain text: {plainText}')
            if not key.isalpha():
                raise ValueError(f'Invalid key: {key}')
        case 1:
            plainText = ''.join([i for i in plainText if i.isalpha()])
            key = ''.join([i for i in key if i.isalpha()])
        case _:
            raise ValueError(f'Invalid mode: {mode}')
    
    # Remove all spaces
    spaces = [i for i in range(len(plainText)) if plainText[i] == ' ']
    tempPlainText = plainText.replace(' ','').upper().replace('J','I')
    # Process the plainText
    temp = ''
    i = 0
    while i < len(tempPlainText):
        if i == len(tempPlainText) - 1:
            temp += tempPlainText[i] + 'X'
            break
        substr = tempPlainText[i:i+2]
        if substr[0] != substr[1]:
            temp += substr
            i += 2
        else:
            temp += substr[0] + 'X'
            i += 1
    
    tempPlainText = temp

    # Build the key
    uppper = string.ascii_uppercase.replace('J','')
    freq = {i:0 for i in uppper}
    charToPos = {}
    idx = 0
    for value in key.upper().replace('J','I') + uppper:
        if not freq[value]:
            freq[value] = 1
            charToPos[value] = (idx // 5 , idx % 5)
            idx += 1
    
    posToChar = {charToPos[i]:i for i in charToPos}

    # Encryption
    cipherText = []
    for i in range(0,len(tempPlainText),2):
        substr = tempPlainText[i:i+2]
        if charToPos[substr[0]][0] == charToPos[substr[1]][0]:
            cipherText.append(posToChar[(charToPos[substr[0]][0],(charToPos[substr[0]][1] + 1) % 5)])
            cipherText.append(posToChar[(charToPos[substr[1]][0],(charToPos[substr[1]][1] + 1) % 5)])
        elif charToPos[substr[0]][1] == charToPos[substr[1]][1]:
            cipherText.append(posToChar[((charToPos[substr[0]][0] + 1) % 5,charToPos[substr[0]][1])])
            cipherText.append(posToChar[((charToPos[substr[1]][0] + 1) % 5,charToPos[substr[1]][1])])
        else:
            cipherText.append(posToChar[(charToPos[substr[0]][0],charToPos[substr[1]][1])])
            cipherText.append(posToChar[(charToPos[substr[1]][0],charToPos[substr[0]][1])])
    
    for i in spaces:
        cipherText.insert(i," ")
    return "".join(cipherText)


def playfaireDecrypt(cipherText,key,mode=0):
    '''
    This function decrypt the cipher text using Playfaire cipher.
    key parameter for decryption key(Not optional).
    mode parameter for decryption mode(By Default 0).
    mode -> 0 only alpha letters are acceptable.
    mode -> 1 if there is non-alpha letters will ignore it from both plain text and key.
    '''
    match mode:
        case 0:
            if not plainText.isalpha():
                raise ValueError(f'Invalid plain text: {plainText}')
            if not key.isalpha():
                raise ValueError(f'Invalid key: {key}')
        case 1:
            plainText = ''.join([i for i in cipherText if i.isalpha()])
            key = ''.join([i for i in key if i.isalpha()])
        case _:
            raise ValueError(f'Invalid mode: {mode}')
    
    # Remove all spaces
    if len(cipherText.replace(' ','')) % 2:
        return None , None
    spaces = [i for i in range(len(cipherText)) if cipherText[i] == ' ']
    tempCipherText = cipherText.replace(' ','').upper().replace('J','I')

    # Build the key
    uppper = string.ascii_uppercase.replace('J','')
    freq = {i:0 for i in uppper}
    charToPos = {}
    idx = 0
    for value in key.upper().replace('J','I') + uppper:
        if not freq[value]:
            freq[value] = 1
            charToPos[value] = (idx // 5 , idx % 5)
            idx += 1
    
    posToChar = {charToPos[i]:i for i in charToPos}

    # Decryption
    plainText = []
    for i in range(0,len(tempCipherText),2):
        substr = tempCipherText[i:i+2]
        if charToPos[substr[0]][0] == charToPos[substr[1]][0]:
            plainText.append(posToChar[(charToPos[substr[0]][0],(charToPos[substr[0]][1] - 1) % 5)])
            plainText.append(posToChar[(charToPos[substr[1]][0],(charToPos[substr[1]][1] - 1) % 5)])
        elif charToPos[substr[0]][1] == charToPos[substr[1]][1]:
            plainText.append(posToChar[((charToPos[substr[0]][0] - 1) % 5,charToPos[substr[0]][1])])
            plainText.append(posToChar[((charToPos[substr[1]][0] - 1) % 5,charToPos[substr[1]][1])])
        else:
            plainText.append(posToChar[(charToPos[substr[0]][0],charToPos[substr[1]][1])])
            plainText.append(posToChar[(charToPos[substr[1]][0],charToPos[substr[0]][1])])
    
    for i in spaces:
        plainText.insert(i," ")
    plainText = "".join(plainText)
    textAfterFiltration = [plainText[0] if plainText[0] != 'I' else '(I/J)']
    for i in range(1,len(plainText)-1):
        if plainText[i] == 'X' and plainText[i-1] == plainText[i+1]:
            continue
        elif plainText[i] == 'I':
            textAfterFiltration.append('(I/J)')
        else:
            textAfterFiltration.append(plainText[i])
    if textAfterFiltration[-1] == 'X':
        textAfterFiltration.pop()
    
    return plainText , ''.join(textAfterFiltration)

