class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        lis = [0,0,-1]
        count = 0
        for s in range(26):
            string = self.apply_shift(26-s)
            for word in string.split(' '):
                if is_word(self.valid_words, word):
                    count += 1
            
            if count >= lis[2]:
                lis[0] = string
                if s%26 == 0: 
                    lis[1] = 0
                else:
                    lis[1] = 26-s
                lis[2] = count
            count = 0
            
        return tuple(lis[0:2][::-1]) 