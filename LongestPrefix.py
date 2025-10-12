def longestprefix(a):
    size = len(a)

    if size == 0:
        return ""
    
    if size == 1:
        return a[0]
    
    a.sort()

    end = min(len(a[0]), len(a[-1]))  # Corrected

    i = 0
    while i < end and a[0][i] == a[-1][i]:
        i += 1

    output = a[0][:i]  # Clean slice syntax
    return output


words = ["Daniel", "Dani", "Dany"]
print("The longest prefix is", longestprefix(words))
