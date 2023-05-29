# text = input()
text = 'A man, a plan, a canal: Panama ff'
words_list = text.split()
only_letters_list = []
for word in words_list:
    word = word.lower()
    letters = [letter for letter in word if letter.isalpha()]
    only_letters_list.extend(letters)

print(only_letters_list)

if len(only_letters_list) % 2 != 0:
    middle_index = len(only_letters_list) // 2
    only_letters_list.pop(middle_index)

print(only_letters_list)

x1 = len(only_letters_list) // 2
x2 = x1

if only_letters_list[:x1] == only_letters_list[x2:][::-1]:
    print('True')
else:
    print('False')
