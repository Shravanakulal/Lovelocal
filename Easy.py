def len_of_last_word(s):
    words = s.split()

    if not words:
        return 0


    return len(words[-1])


s = "luffy is still joyboy"
result = len_of_last_word(s)
print(result)
