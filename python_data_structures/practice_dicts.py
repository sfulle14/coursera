

# counts = dict()
# names = ['csev', 'cwen','csev','zqian','cwen']
# # for name in names:
# #     if name not in counts:
# #         counts[name] = 1
# #     else:
# #         counts[name] = counts[name] + 1

# # print(counts)

# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)




# counts = dict()
# print('enter line of text:')
# line = input('')

# words = line.split()

# print('Words:', words)

# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1

# print('Counts', counts)


# c = {'chuck':1, 'fred':42, 'jan':100}
# for k, v in c.items():
#     print(k,v)


name = input('enter file: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count   

print(bigword, bigcount)