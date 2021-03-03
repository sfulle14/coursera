text = ('X-DSPAM-Confidence:    0.8475')
pos1 = text.find('0')
pos2 = text.find('5')

print(pos1)
print(pos2)
data = text[pos1:pos2+1]
data = float(data)
print(type(data))
print(data)