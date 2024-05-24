original_text = (
    '“Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
    + 'facilisis vitae semper at, dignissim vitae libero”'
)

words = original_text.split()
formatted_text = []
for word in words:
    if ',' in word:
        formatted_word = word[:-1] + 'ing,'
    elif '.' in word:
        formatted_word = word[:-1] + 'ing.'
    elif '”' in word:
        formatted_word = word[:-1] + 'ing”'   
    else:
        formatted_word = word + 'ing'
    formatted_text.append(formatted_word) 

print(' '.join(formatted_text))
