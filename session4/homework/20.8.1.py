input_sen = str(input("Enter a sentence"))
sen = input_sen.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
charac_count = {}

for charac in sen:
    if charac in alphabet:
        if charac in charac_count:
            charac_count[charac] += 1
        else:
            charac_count[charac] = 1

for i in charac_count:
    print(i,charac_count[i])
