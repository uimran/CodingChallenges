def swap_case(s):
    swap=[]
    for i in range (len(s)):
        if s[i]==s[i].lower():
            swap.append(s[i].upper())
        elif s[i]==s[i].upper():
            swap.append(s[i].lower())
    answer=''.join(swap)
    return answer
s=raw_input()
print swap_case(s)
