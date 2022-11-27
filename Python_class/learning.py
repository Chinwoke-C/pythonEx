import string


def encryption_code(word1, key1):
    letters = string.ascii_lowercase
    inverse = letters[key1:] + letters[:key1]
    message = word1.translate(str.maketrans(letters, inverse))
    print(message)


def decryption_code(word2, key2):
    alphabet = string.ascii_lowercase
    revert = alphabet[key2:] + alphabet[:key2]
    message2 = word2.translate(str.maketrans(revert, alphabet))
    print(message2)


if __name__ == '__main__':
    word = input("Enter a word: ")
    key = int(input("Enter the key to encode with: "))
    encryption_code(word, key)

    key = int(input("Enter the key to decode with: "))
    word = input("Enter the encoded word: ")
    decryption_code(word, key)
