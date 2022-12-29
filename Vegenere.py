# Authors:
# Andrea Alexandra Sánez Oquendo
# Fernanda Rocha Costa Neto
import math

class Vegenere:
    def __init__(self):
        self.keyword = 'crystalgems'

    ## Sets new keyword
    def set_keyword(self, keyword):
        self.keyword = keyword

    ## Returns the encrypted letter according to the keyword's letter
    def __get_encrypted_letter(self, key_letter, letter):
        alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'

        if letter not in alphabet:
            return letter

        i = alphabet.index(letter) + alphabet.index(key_letter)
        if i >= len(alphabet):
            i-= len(alphabet)
        
        return alphabet[i]

    ## Returns the original letter according to the keyword's letter
    def __get_original_letter(self, key_letter, letter):
        alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ'

        if letter not in alphabet:
            return letter

        i = alphabet.index(letter) - alphabet.index(key_letter)
        if i < 0:
            i+= len(alphabet)
        
        return alphabet[i]

    ## Makes a repetition of the keyword to fit the message's size
    def __fit_keyword(self, message):
        times = math.floor(len(message)/len(self.keyword))
        rest = len(message) - times*len(self.keyword)
        return self.keyword*times + self.keyword[:rest]
    
    ## Returns encrypted message
    def get_encrypted_message(self, message):

        keyword = self.__fit_keyword(message)
        encrypted_message = ''     
        for i, letter in enumerate(message):
            encrypted_message+= self.__get_encrypted_letter(keyword[i], letter)
        
        return encrypted_message

    # Returns original message (string) from encrypted message
    def get_original_message(self, message):

        keyword = self.__fit_keyword(message)  
        original_message=''
        for i, letter in enumerate(message):
            original_message+= self.__get_original_letter(keyword[i], letter)
        
        return original_message
    
    ## Returns list of the whole message in binary
    @staticmethod
    def convert_to_binary(message):
        binary_message_str = ''
        for letter in message:
            binary_message_str += bin(ord(letter))[2:].zfill(8)

        binary_message = []
        for letter in binary_message_str:
            i = 0
            if letter == '1':
                i = 1
            binary_message.append(i)

        return binary_message

    ## converts each byte into characters
    @staticmethod
    def binary_to_string(binary):
        binary_message = [binary[i:i + 8] for i in range(0, len(binary), 8)]
        
        message = ''
        for byte in binary_message:
            message += chr(int(''.join([str(item) for item in byte]), 2))
        
        return message

    ## Returns encrypted binary message
    def encode_vegenere(self, message):
        encrypted_message = self.get_encrypted_message(message)
        binary_message = self.convert_to_binary(encrypted_message)
        return binary_message

    ## Returns encrypted binary message to original message
    def decodeVegenere(self, binary_message):
        encrypted_message = self.binary_to_string(binary_message)
        original_message = self.get_original_message(encrypted_message)
        return original_message

    
    
    






    