long_text = input(int())
text = input()
list_words = text.rsplit()
print(list_words)
max_word = ''
max_count = 0
for word in list_words:
    if len(word) > max_count:
        max_count = len(word)
        max_word = word

print(max_word, max_count, sep='\n')
