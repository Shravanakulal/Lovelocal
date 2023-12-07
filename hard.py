def short_p(s):
    if not s:
        return ""

    modified_s = s + '#' + s[::-1][1:]

    prefix_arr = [0] * len(modified_s)
    j = 0

    for i in range(1, len(modified_s)):
        while j > 0 and modified_s[i] != modified_s[j]:
            j = prefix_arr[j-1]


        if modified_s[i] == modified_s[j]:
            j+=1

        prefix_arr[i] = j


    palindrome_len = prefix_arr[-1]

    short_p = s[palindrome_len : ][::-1]+s


    return short_p


s = "abcd"
output = short_p(s)
print(output)


    
