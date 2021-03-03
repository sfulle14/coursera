

f = open('coursera_classes/python_data_structures/romeo.txt')
counts = dict()
for line in f:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# lst = list()
# for key, val in counts.items():
#     newtup = (val,key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# for val, key in lst[:10]:
#     print(key,val)

# print(sorted([(v,k) for k,v in counts.items()], reverse=True))