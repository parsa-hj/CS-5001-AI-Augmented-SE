def first_non_repeating_character(str1):
    char_order = []
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            char_order.append(char)
    for char in char_order:
        if char_count[char] == 1:
            return char
    return None
