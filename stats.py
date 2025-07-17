def words_counter(text):
    counter = 0
    for word in text.split():
        counter += 1
    return counter

def char_counter(text):
    char_dict = {}
    for char in text.lower():
        if char.isalpha():
            counter = char_dict.get(char, 0)
            char_dict[char] = counter + 1
    return char_dict

def dict_to_ordered_list(d):
    l = []
    for key, value in d.items():
        l.append((key, value))
    l.sort(key=lambda x: x[1], reverse=True)
    return l