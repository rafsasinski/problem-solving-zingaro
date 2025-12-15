# https://dmoj.ca/problem/ccc02j2

input_word = ""
vovels = "aeiouy"

while input_word != "quit!":
    input_word = input()
    if input_word == "quit!":
        break
    elif len(input_word) > 4:
        if input_word[-3] not in vovels and input_word[-2:] == "or":
            input_word = input_word[0:-2] + "our"

    print(input_word)
