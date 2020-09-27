count = 0
for i in range(len(s)):
    if s[i] == 'b':
        x = s[i:i+3]
        #print(x)
        if x == 'bob':
            count += 1
print('Number of times bob occurs is:', count)