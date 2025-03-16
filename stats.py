def get_num_words(text):
    return text.split()

def count_char(text):
    words_arr = get_num_words(text)
    characters = {}
    letters = []

    for char in words_arr:
        letter_list = list(char)
        for l in letter_list:
            letters.append(l)

    for letter in letters:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1

    return characters

def sort_character_counts(char_count_dict):
    alpha_chars = {char: count for char, count in char_count_dict.items() if char.isalpha()}

    sorted_list = [{'char': char, 'count': count} for char, count in alpha_chars.items()]

    sorted_list.sort(key=lambda x: x['count'], reverse=True)

    return sorted_list
