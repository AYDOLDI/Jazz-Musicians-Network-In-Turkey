file = open('JazzMusicians text.txt', 'r', encoding="utf-8")
lines = file.readlines()
listData = []
for i, line in enumerate(lines):
    line = line.strip()
    listData.append(line)

file.close()

#prints the pairs with some problems like, A,B 1 9 12 then A,B 9 12
"""
# Splitting the names and storing them in a list
data = [line.split(',') for line in listData]

# Getting all the pairs for each row
pairs = {i: [tuple(sorted((x, y))) for idx, x in enumerate(data[i]) for y in data[i][idx + 1:]] for i in range(len(data))}

# Checking if the pairs in the current row exist in the following rows
found_pairs = []
for i in pairs:
    for pair in pairs[i]:
        for j in range(i + 1, len(data)):
            if pair[0] in data[j] and pair[1] in data[j]:
                found_pairs.append((i, j, pair))


# Printing the pairs found
with open('reversedpair.txt', 'w', encoding='utf-8') as f:
    for i, j, pair in found_pairs:
        f.write(f"{pair[0]}, {pair[1]} -> {i+1} {j+1}\n")
"""

#writes distinct rows of all pairs
"""
# Splitting the names and storing them in a list
data = [line.split(',') for line in listData]

# Getting all the pairs for each row
pairs = {i: [tuple(sorted((x, y))) for idx, x in enumerate(data[i]) for y in data[i][idx + 1:]] for i in range(len(data))}

# Checking if the pairs in the current row exist in the following rows and store the row numbers
pair_rows = {}
for i in pairs:
    for pair in pairs[i]:
        for j in range(i + 1, len(data)):
            if pair[0] in data[j] and pair[1] in data[j]:
                if pair in pair_rows:
                    pair_rows[pair].add(j + 1)
                else:
                    pair_rows[pair] = {i + 1, j + 1}

# Printing the pairs and the distinct rows they were found in
with open('DistinctPairsCount.txt', 'w', encoding='utf-8') as f:
    for pair, rows in pair_rows.items():
        f.write(f"{pair[0]}, {pair[1]} --> {', '.join(map(str, sorted(rows)))}\n")
"""


#gets all distinct pair count.

# Splitting the names and storing them in a list
data = [line.split(',') for line in listData]

# Getting all the pairs for each row
pairs = {i: [tuple(sorted((x, y))) for idx, x in enumerate(data[i]) for y in data[i][idx + 1:]] for i in range(len(data))}

# Checking if the pairs in the current row exist in the following rows and store the row numbers
pair_rows = {}
for i in pairs:
    for pair in pairs[i]:
        for j in range(i + 1, len(data)):
            if pair[0] in data[j] and pair[1] in data[j]:
                if pair in pair_rows:
                    pair_rows[pair].add(j + 1)
                else:
                    pair_rows[pair] = {i + 1, j + 1}

# Printing the pairs, the distinct rows they were found in and the count
with open('DistinctPairsCountLastofLast.txt', 'w', encoding='utf-8') as f:
    for pair, rows in pair_rows.items():
        count = len(rows)
        f.write(f"{pair[0]},{pair[1]}-{count}\n")
        
