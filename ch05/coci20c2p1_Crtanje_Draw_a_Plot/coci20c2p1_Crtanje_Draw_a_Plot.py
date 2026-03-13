n_days = int(input())
changes = list(input())

CHANGE_TO_INT = {
    "+": 1,
    "-": -1,
    "=": 0
}
CHANGE_TO_SYMBOL = {
    "+": "/",
    "-": "\\",
    "=": "_"
}

rows = []
x = 0
y = 0
y_offset = 0
prev_delta = None
curr_delta = None
while x < n_days:
    ch = changes[x]

    if x > 0:
        curr_delta = CHANGE_TO_INT[ch]
        if curr_delta == -1 and prev_delta <= 0:
            y -= 1
        elif curr_delta >= 0 and prev_delta == 1:
            y += 1

    if len(rows) <= y + y_offset or len(rows) == 0:
        row = "." * n_days
        row = row[0:x] + CHANGE_TO_SYMBOL[ch] + row[x + 1:]
        rows.append(row)
    elif 0 > y + y_offset:
        y_offset += 1
        row = "." * n_days
        row = row[0:x] + CHANGE_TO_SYMBOL[ch] + row[x + 1:]
        rows.insert(0, row)
    else:
        row = rows[y + y_offset]
        row = row[0:x] + CHANGE_TO_SYMBOL[ch] + row[x + 1:]
        rows[y + y_offset] = row



    prev_delta = CHANGE_TO_INT[ch]
    x += 1

lines = len(rows)
while lines > 0:
    print(rows[lines-1])
    lines -= 1

'''
-2: -1 -1 -- DOWN 
-1: 0 -1 =- DOWN 
-1: -1 0 -= STAY 
0: -1 1 -+ STAY 
0: 0 0 == STAY 
0: 1 -1 +- STAY 
1: 0 1 =+ STAY 
1: 1 0 += UP 
2: 1 1 ++ UP 
'''