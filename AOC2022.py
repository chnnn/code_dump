#day 1 ------------------------------------------------------------------------------------------------------------------------------------

with open('input.txt') as f:
    maxx = []
    curr = 0

    for i in f:
        line = i.strip()
        if line == '': 
            maxx.append(curr)
            if len(maxx) == 4:
                maxx.sort()
                maxx = maxx[1:]
            curr = 0
        else:
            curr += int(line)
            
    print(maxx, sum(maxx)) #67658 200158
    
    #day 2 ------------------------------------------------------------------------------------------------------------------------------------
    
    with open('input.txt') as f:
    dic = {'A':1,'B':2,'C':3, 'X':1, 'Y':2, 'Z':3}
    part1, part2 = 0,0
    
    for line in f:
        f, b = line.strip().split(' ')
        part1 += dic[b]
        if f+b in ['CX', 'BZ', 'AY']: part1 += 6
        if dic[f] == dic[b]: part1 +=3
            
        part2 += (b == 'X')*((f=='A')*3 + (f=='B') + (f=='C')*2) 
        part2 += (b == 'Y')*(3 + dic[f]) 
        part2 += (b == 'Z')*((f=='A')*2 + (f=='B')*3 + (f=='C') + 6) 
                
    print(part1, part2) #15337 #11696
    
#day 3 ------------------------------------------------------------------------------------------------------------------------------------

with open('input.txt') as f: #part 1
    total = 0
    for line in f:
        line = line.strip()
        sack1, sack2 = sorted(line[0:len(line)//2]), sorted(line[len(line)//2:])
        
        o = ord([i for i in sack1 if i in sack2][0])
        if o <123 and o >96: total += o-96
        else: total += o-38
             
    print(total) #7997 

with open('input.txt') as f: #part 2
    l = f.readlines()
    l = [l[i*3:i*3+3] for i in range(len(l)//3)]

total = 0
for i in l:
    i = [sorted(x.strip()) for x in i]
    o = ord([y for y in i[0] if y in i[1] and y in i[2]][0])
    if o <123 and o >96: total += o-96
    else: total += o-38
            
print(total) #2545

#day 4 ------------------------------------------------------------------------------------------------------------------------------------





