input_file = open("alphabet.txt", "r")

find_word = ''
for word_line in input_file:
    for word in word_line:
        if word in ['a', 'e', 'i', 'o', 'u']:
            find_word += word
    if find_word == 'aeiou':
        print(word_line, end='')

    find_word = ''
