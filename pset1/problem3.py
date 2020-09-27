temp = ''
lis = []

orignal_word = s
for i in range(len(s)):
    temp = ''
    for i in range(len(s)-1):
        if s[i] <= s[i+1]:
            temp += s[i]
        else:
            temp += s[i]
            lis.append(temp)
            s = s[i+1:]
            break

longest = ''            
for i in lis:
    if len(i) > len(longest):
        longest = i
        
if len(lis) == 0:
    longest = orignal_word
    
print('Longest substring in alphabetical order is:',longest)