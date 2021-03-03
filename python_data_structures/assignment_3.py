
# Use the file name mbox-short.txt as the file name

fname = input('Enter file name: ')
fh = open(fname)
count = 0
tot = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:') : continue
    count += 1
    pos1 = line.find(':')
    data = line[pos1+1:]
    data = float(data)
    tot = tot + data

avg = tot / count
avg = str(avg)
print('Average spam confidence: ' + avg)
