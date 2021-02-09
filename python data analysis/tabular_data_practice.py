






"""
Tabular data as a nested list.
"""
# # https://www.coursera.org/learn/python-analysis/lecture/57msf/tabular-data-as-a-nested-list


# # Programming language popularity, from www.tiobe.com/tiobe-index
# popularity = [["Language", 2017, 2012, 2007, 2002, 1997, 1992, 1987],
#               ["Java", 1, 2, 1, 1, 15, 0, 0],
#               ["C", 2, 1, 2, 2, 1, 1, 1],
#               ["C++", 3, 3, 3, 3, 2, 2, 5],
#               ["C#", 4, 4, 7, 13, 0, 0, 0],
#               ["Python", 5, 7, 6, 11, 27, 0, 0],
#               ["Visual Basic .NET", 6, 17, 0, 0, 0, 0, 0],
#               ["PHP", 7, 6, 4, 5, 0, 0, 0],
#               ["JavaScript", 8, 9, 8, 7, 23, 0, 0],
#               ["Perl", 9, 8, 5, 4, 4, 10, 0]]

# format_string = "{:<20}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}"

# # Display langauges table
# headers = popularity[0]
# header_row = format_string.format(*headers)
# print(header_row)
# print("-" * len(header_row))

# for language in popularity[1:]:
#     print(format_string.format(*language))

# print("")
    
# # Finding/selecting items

# # What was Python's popularity in 1997?
# print("Python's popularity in 1997:", popularity[5][5])

# def find_col(table, col):
#     """
#     Return column index with col header in table
#     or -1 if col is not in table
#     """
#     return table[0].index(col)

# def find_row(table, row):
#     """
#     Return row index with row header in table
#     or -1 if row is not in table
#     """
#     for idx in range(len(table)):
#         if table[idx][0] == row:
#             return idx
#     return -1
    
# idx1997 = find_col(popularity, 1997)
# idxpython = find_row(popularity, "Python")
# print("Python's popularity in 1997:", popularity[idxpython][idx1997])






"""
Tabular data as nested dictionaries.
"""

# Top 10 software products with the most vulnerabilities in 2017
# (through August).  From www.cvedetails.com.
vulnerabilities2017 = {
    'Android': {'vendor': 'Google',
                'type': 'Operating System',
                'number': 564},
    'Linux Kernel': {'vendor': 'Linux',
                     'type': 'Operating System',
                     'number': 367},
    'Imagemagick': {'vendor': 'Imagemagick',
                    'type': 'Application',
                    'number': 307},
    'IPhone OS': {'vendor': 'Apple',
                  'type': 'Operating System',
                  'number': 290},
    'Mac OS X': {'vendor': 'Apple',
                 'type': 'Operating System',
                 'number': 210},
    'Windows 10': {'vendor': 'Microsoft',
                   'type': 'Operating System',
                   'number': 195},
    'Windows Server 2008': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 187},
    'Windows Server 2016': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 183},
    'Windows Server 2012': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 176},
    'Windows 7': {'vendor': 'Microsoft',
                  'type': 'Operating System',
                  'number': 174}
}

# Display vulnerabilities table
print("Product               Vendor        Type               Vulnerabilities")
print("----------------------------------------------------------------------")

for product, values in vulnerabilities2017.items():
    row = "{:21} {:13} {:18} {:8}".format(product, values['vendor'], values['type'], values['number'])
    print(row)

print("")

# Finding/selecting items

# How many vulnerabilites does Windows 7 have?
print(vulnerabilities2017['Windows 7']['number'])

# What product had the most vulnerabilities?
maxproduct = None
maxnumber = -1

for product, values in vulnerabilities2017.items():
    if values['number'] > maxnumber:
        maxproduct = product
        maxnumber = values['number']

print(maxproduct, maxnumber)



