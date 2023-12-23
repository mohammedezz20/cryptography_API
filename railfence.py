def railfenceEncrypt(plainText,depth):
    '''
    This function encrypt the plain text using the Railfence cipher.
    depth parameter for the encryption depth(Not Optional).
    '''
    spaces = [i for i in range(len(plainText)) if plainText[i] == ' ']
    plainText = plainText.replace(' ','')
    cipherText = ''
    start_loop = 0
    end_loop = len(plainText)
    baseDepth = (depth - 2) * 2 + 1
    currentDepth = baseDepth + 1
    while len(cipherText) < len(plainText):
        for i in range(start_loop,end_loop,currentDepth):
            cipherText += plainText[i]
        start_loop += 1
        currentDepth -= 2
        currentDepth = baseDepth + 1 if currentDepth == 0 else currentDepth
    cipherText = list(cipherText)
    for i in spaces:
        cipherText.insert(i,' ')
    return ''.join(cipherText)


def railfenceDecrypt(cipherText,depth):
    '''
    This function decrypt the cipher text using the Railfence cipher.
    depth parameter for the encryption depth(Not Optional).
    '''
    gridPoints = {}
    i , j = 0 , 0
    flag = 1
    while j < len(cipherText):
        gridPoints[(i,j)] = ''
        if i == 0:
            flag = 1
        elif i == depth - 1:
            flag = 0
        if flag:
            i += 1
        else:
            i -= 1
        j += 1
    gridPoints = dict(sorted(gridPoints.items()))
    j = 0
    for point in gridPoints:
        gridPoints[point] = cipherText[j]
        j += 1
    gridPoints = dict(sorted(gridPoints.items(),key=lambda x:x[0][1]))
    plainText = ''
    for point in gridPoints:
        plainText += gridPoints[point]
    return plainText


print(railfenceDecrypt('PINALSIGYAHRPI',4) == 'PAYPALISHIRING')