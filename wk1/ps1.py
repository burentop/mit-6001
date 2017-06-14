

s = 'abcbcd'

longest = ''
longlen = 0
length = len(s)
for i in range(length - 1):
    start = i
    end = i + 1
    tempLong = s[i]
    tempLongLen = 1
    while True:
        if end < length:
            if s[end] >= s[start]:
                tempLong += s[end]
                tempLongLen += 1
                end += 1
                start += 1
            else:
                break
        else:
            break
    if tempLongLen > longlen:
        longest = tempLong
        longlen = tempLongLen
            
print('Longest substring in alphabetical order is: ' + longest)
        
        
        
        
        