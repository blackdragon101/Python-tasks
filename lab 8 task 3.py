
def encryption(sentence):
    key = {'a': '2', 'b': '@', 'c': '-', 'd': '+', 'e': '|', 'f': '&', 'g': '3', 'h': '!', 'i': '#',
           'j': '%', 'k': '9', 'l': '^', 'm': '5', 'n': '$', 'o': '*', 'p': '6', 'q': '1', 'r': '?',
           's': '4', 't': '7', 'u': '~', 'v': '8', 'w': '<', 'x': '{', 'y': '0', 'z': '>'}
    random_words = 'abcdefghijklmnopqrstuvwxyz'
    sen1 = sentence.lower()
    reverse = sen1[::-1]
    input_list = reverse.split()
    new_list = []
    for elements in input_list:
        list = []
        for letter in elements:
            list.append(key[letter])
        new_list.append(list)
    import random
    random_numbers = ''
    for words in new_list:
        for i in range(3):
            random_numbers += random.choice(random_words)
        words.append(random_numbers)
        random_numbers = ''
    return new_list


def decryption(code_language):
    code = {'a': '2', 'b': '@', 'c': '-', 'd': '+', 'e': '|', 'f': '&', 'g': '3', 'h': '!', 'i': '#',
           'j': '%', 'k': '9', 'l': '^', 'm': '5', 'n': '$', 'o': '*', 'p': '6', 'q': '1', 'r': '?',
           's': '4', 't': '7', 'u': '~', 'v': '8', 'w': '<', 'x': '{', 'y': '0', 'z': '>'}
    message1 = code_language.split()
    decipher_list = []
    for output in message1:
        message2 = ""
        for outs in output:
            if not outs.isalpha():
                message2 += outs
        decipher_list.append(message2)
    decrypt_list = []
    for decipher in decipher_list:
        finale = ""
        for units in decipher:
            for keys, values in code.items():
                if units == values:
                    finale += keys
                    reverse = finale[::-1]
                    break
        decrypt_list.append(reverse)
    final_list = []
    for i in range(len(decrypt_list) - 1, -1, -1):
        final_list.append(decrypt_list[i])
    for elements in final_list:
        return elements

file1 = open('file1.txt','r')
decrypted_content = file1.read()
cipher = encryption(decrypted_content)
file1.close()
decrypt = open('decrypt.txt','w')
for elements in cipher:
    for words in elements:
        decrypt.write(words)
decrypt.close()
file2 = open('decrypt.txt','r')
encrypted_content = file2.read()
decipher = decryption(encrypted_content)
file2.close()
encrypt = open('encypt.txt','w')
encrypt.write(decipher)
encrypt.close()



