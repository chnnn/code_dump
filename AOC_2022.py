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

with open('input.txt') as f:
    part1 = part2 = 0
    
    for line in f:
        elf1, elf2 = line.strip().split(',') 
        elf1, elf2 = list(map(int, elf1.split('-'))), list(map(int, elf2.split('-')))
        elf1, elf2 = list(range(elf1[0], elf1[1]+1)), list(range(elf2[0], elf2[1]+1))
        l1, l2 = len(elf1), len(elf2)
        tgt = len(set(elf1+elf2))
        
        if tgt == l2 or tgt == l1: part1+=1    
        if tgt < l1+l2: part2 += 1   
        
    print(part1, part2) #450, 837
    
#day 5 ------------------------------------------------------------------------------------------------------------------------------------

with open('input.txt') as f: l = f.readlines()
    
stack = [[] for i in range(9)]
for line in l[:8]:
    for i in range(9):
        if line[1 + i*4] != ' ': stack[i].append(line[1 + i*4])
        
stack1, stack2 = [i[::-1] for i in stack], [i[::-1] for i in stack]  
    
for line in l[10:]:
    movenum, rest = line.strip().split(' from ')
    movenum = int(movenum[5:])
    fro, to = map(int, rest.split(' to '))
    
    for i in range(movenum): stack1[to-1].append(stack1[fro-1].pop())   
    stack2[to-1] += stack2[fro-1][-movenum:]
    stack2[fro-1] = stack2[fro-1][:-movenum]
    
part1, part2 = ''.join(i[-1] for i in stack1), ''.join(i[-1] for i in stack2)
print(part1, part2) #ZSQVCCJLL, QZFJRWHGS

#day 6 ------------------------------------------------------------------------------------------------------------------------------------

with open('input.txt') as f: l = f.readlines()[0].strip()
    
for i in range(len(l)-3):
    curr = l[i:i+4]
    if len(set([x for x in curr])) == 4: 
        print(i+4) #1100
        break

for i in range(len(l)-13):
    curr = l[i:i+14]
    if len(set([x for x in curr])) == 14: 
        print(i+14) #2421
        break
        
#day 7 ------------------------------------------------------------------------------------------------------------------------------------       
        
