# def count(string):
#     c = 0
#     vowels = "aeiouy"
#     if string[0] in vowels:
#         c += 1
#     for i in range(1, len(string)):
#         if string[i] in vowels and word[i-1] not in vowels:
#             c += 1
#             print(string[i]+"-")
#     if count == 0:
#         count += 1
#     return count

# count("")

def count(string):
    c = 1
    if string == "":
        c= 0
    for i in range(len(string)):
        if string[i] == '-':
            c +=1
    return c

print(count("met-a-phor"))
print(count("ho-tel"))
print(count("cat"))
print(count(""))


