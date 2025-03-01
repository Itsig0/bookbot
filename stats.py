def get_word_cound(t):
    return len(t.split())

def get_character_count(t):
    t = t.lower()
    char_counts = dict()
    for char in t:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_character_count(c):
    return sorted(c.items(), key=lambda item: item[1], reverse=True)
