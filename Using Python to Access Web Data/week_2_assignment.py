import regex as re

with open('coursera_classes/Python for Eerybody/Using Python to Access Web Data/regex_sum_1508779.txt') as f:
    text = f.read()

    nums = re.findall(r'[0-9]+', text)
    
    length = len(nums)+ 1

    total = 0
    for x in nums:
        x = int(x)
        total += x 
    print(total)






#practice
"""
with open('coursera_classes/Python for Eerybody/Using Python to Access Web Data/regex_sum_42.txt') as f:
    text = f.read()

    nums = re.findall(r'[0-9]+', text)
    
    length = len(nums)+ 1

    total = 0
    for x in nums:
        x = int(x)
        total += x 
    print(total)
"""


