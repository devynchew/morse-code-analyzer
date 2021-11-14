# given a dictionary of unique keys, how to sort by value desc first, then same freq will be sorted by length in asc. Finally, words with same freq and length sort alphabetically desc
freq = {'HELP': 2, 'US': 2, 'SOS': 5, 'OUR': 2, 'SHIP': 2, 'HAS': 1, 'HIT': 2, 'AN': 3, 'ICEBERG': 2, 'PLEASE': 1, 
'THIS': 2, 'IS': 3, 'A': 1, 'SINKING': 1, 'WE': 1}
print(sorted(freq.items(), key=lambda x: (-x[1], len(x[0]), x[0])))

