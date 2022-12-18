import math

class Vegenere:
    def __init__(self):
        self.inputC = ''
        self.binaryC = []
        self.outputC = ''
        self.inputD = []
        self.binaryD = []
        self.outputD = ''
        self.stringD = ''

        self.keyword = 'crystalgems'

        self.charToIndex = {
            'c': 2,
            'r': 17,
            'y': 24,
            's': 18,
            't': 19,
            'a': 0,
            'l': 11,
            'g': 6,
            'e': 4,
            'm': 12
        }
    
    def getCryptographedLetter(self, index, letter):
        alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'

        if letter not in alphabet:
            return letter

        i = alphabet.index(letter) + self.charToIndex[index]
        if i >= len(alphabet):
            i-= len(alphabet)
        
        return alphabet[i]

    def getDecryptographedLetter(self, index, letter):
        alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'

        if letter not in alphabet:
            return letter

        i = alphabet.index(letter) - self.charToIndex[index]
        if i < 0:
            i+= len(alphabet)
        
        return alphabet[i]

    def fitKeyword(self):
        if self.inputC == '':
            times = math.floor(len(self.stringD)/len(self.keyword))
            rest = len(self.stringD) - times*len(self.keyword)
            return self.keyword*times + self.keyword[:rest]
        else:
            times = math.floor(len(self.inputC)/len(self.keyword))
            rest = len(self.inputC) - times*len(self.keyword)
            return self.keyword*times + self.keyword[:rest]

    
    def getCryptographedMessage(self):

        keyword = self.fitKeyword()
        
        for i, letter in enumerate(self.inputC):
            self.outputC+= self.getCryptographedLetter(keyword[i], letter)
        
        return self.outputC

    def getDecryptographedMessage(self):

        keyword = self.fitKeyword()

        for i, letter in enumerate(self.stringD):
            self.outputD+= self.getDecryptographedLetter(keyword[i], letter)
        
        return self.outputD
    
    def convertBinary(self):
        binaryC = ''
        for letter in self.outputC:
            binaryC += bin(ord(letter))[2:].zfill(8)

        for letter in binaryC:
            i = 0
            if letter == '1':
                i = 1
            self.binaryC.append(i)

        return self.binaryC

    def convertToString(self):
        self.binaryD = [self.inputD[i:i + 8] for i in range(0, len(self.inputD), 8)]
        

        for byte in self.binaryD:
            self.stringD += chr(int(''.join([str(item) for item in byte]), 2))
        
        return self.stringD

    def encodeVegenere(self, inputC):
        self.inputC = inputC
        self.binaryC = []
        self.outputC = ''

    def decodeVegenere(self, inputD):
        self.inputD = inputD

        self.binaryD = []
        self.outputD = ''
        self.stringD = ''

    def signalToString(self, signal):
        signal = [2 if x==-1 else x for x in signal]
        s = ''.join([str(item) for item in signal])
        return s

    def stringToSignal(self, str):
        newSignal = []

        letToNum = {'0': 0, '1': 1, '2': -1} 
        for i in str:
            newSignal.append(letToNum[i])
        
        return newSignal
    
    
    






    