#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
#DAY7
with open('day7.txt','r') as file:
    lst = [int(i) for i in file.readline().strip().split(',')]
    d = {m: lst.count(m) for m in set(lst)}

curr_align = curr_sum = 0
for align in range(min(lst),max(lst)):
    s = sum([abs(x-align)*d[x] for x in d.keys()])
    if s<curr_sum or curr_sum == 0: curr_sum, curr_align = s, align
print(curr_align, curr_sum)   #317 331067

#part 2 same as above except formula for s is different and one additional function
def partsum(n):
    return n*(n+1)//2
s = sum([d[x]*partsum(abs(x-align)) for x in d.keys()]) 
#458 92881128
#-------------------------------------------------------------------------------------------------------
#DAY6
with open('day6.txt','r') as file:
    lst = [int(i) for i in file.readline().strip().split(',')]
    d = {n:lst.count(n) for n in range(9)}

for i in range(256): #80 instead of 256 for part 1
    due = d[0]
    for x in range(8):
        d[x] = d[x+1]
    d[8] = due
    d[6] += due

print(sum(d.values())) #391671 and 1754000560399
#-------------------------------------------------------------------------------------------------------
#DAY 5
d = {}
with open('day5.txt','r') as file:
    for line in file:
        front,back = line.strip().split(' -> ')
        x1,y1 = front.split(',')
        x2,y2 = back.split(',')
        if x1 == x2:
            m,M = min(int(y1),int(y2)), max(int(y1),int(y2))
            for i in range(m,M+1):
                if x1+'|'+str(i) not in d.keys(): d[x1+'|'+str(i)] = 1
                else: d[x1+'|'+str(i)] += 1
        elif y1 == y2: 
            m,M = min(int(x1),int(x2)), max(int(x1),int(x2))
            for i in range(m,M+1):
                if str(i)+'|'+y1 not in d.keys(): d[str(i)+'|'+y1] = 1
                else: d[str(i)+'|'+y1] += 1
        else: #part2
            x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)
            jump_x = -1*(x1>x2) + (x1<x2)
            jump_y = -1*(y1>y2) + (y1<y2)
            for i in range(abs(x1-x2)+1):
                if str(x1)+'|'+str(y1) not in d.keys(): d[str(x1)+'|'+str(y1)] = 1
                else: d[str(x1)+'|'+str(y1)] += 1
                x1,y1 = x1+jump_x, y1+jump_y

more_than_two = len([i for i in d.values() if i>1])
print(more_than_two)  #6225 and 22116
#-------------------------------------------------------------------------------------------------------
#DAY4(failed part 2)
with open('day4.txt','r') as file:
    boards = []
    seq = [int(i) for i in file.readline().strip().split(',')]
    
    x = file.readline()
    new_board = []
    while x:
        if x == '\n':
            copy = newboard
            boards.append(copy)
            newboard = []
        else:
            newboard.append([i for i in x.split()])
        x = file.readline()
def bingo_check(b):
    hori = [x.count('X') == 5 for x in b].count(True) #checks all rows
    vert = [[b[r][c] for r in range(5)].count('X') == 5 for c in range(5)].count(True)
    return hori>=1 or vert>=1
def x_replace(b,s):
    for row in range(5):
        for col in range(5):
            if b[row][col] == s: b[row][col] = 'X'

bingoed = False
pos = 0
while not bingoed:
    curr = str(seq[pos])
    for b in boards:
        x_replace(b,curr)
        if bingo_check(b):
            got = b
            lastnum = curr
            bingoed = True
    pos += 1

summ = sum([sum([int(i) for i in x if i!='X']) for x in got])
print(summ,lastnum)
#44*947 = 41668
#-------------------------------------------------------------------------------------------------------
#DAY 3
lst = []
with open('day3.txt','r') as file:
    for line in file:
        lst.append(line.strip())
length = len(lst)

#PART 1
gamma,eps = '',''
for i in range(0,len(lst[0])):
    zeros = len([j for j in range(0,length) if lst[j][i]=='0'])
    if zeros > length/2:
        gamma += '0'
        eps += '1'
    else:
        gamma += '1'
        eps += '0'
print(int(gamma,2)*int(eps,2)) # 394*3701  = 1458194

#PART 2
oxygen = carbon = lst
def find_last(l, var):
    pos,ll = 0,len(l)
    while ll!= 1 :
        zeros = len([j for j in range(0,ll) if l[j][pos]=='0'])
        if zeros > ll/2:
            l = [z for z in l if z[pos] == var]
        else:
            l = [z for z in l if z[pos] != var]
        pos += 1
        ll = len(l) 
    return l
print(int(find_last(carbon, '1')[0],2)* int(find_last(oxygen,'0')[0],2))

#-------------------------------------------------------------------------------------------------------
#DAY 2
#PART 1
hori, vert = 0,0
with open('day2.txt','r') as file:
    for line in file:
        move, size = line.strip().split(' ')
        size = int(size)
        if move == 'forward': hori += size
        elif move == 'down' : vert += size
        else : vert -= size
print(vert*hori)

#PART 2
hori, vert, aim = 0,0,0
with open('day2.txt','r') as file:
    for line in file:
        move, size = line.strip().split(' ')
        size = int(size)
        if move == 'forward': 
            hori += size
            vert += aim * size
        elif move == 'down' : aim += size
        else : aim -= size
print(vert*hori)

#-------------------------------------------------------------------------------------------------------
#DAY 1  
lst = []
with open('day1.txt','r') as file:
    for line in file:
        lst.append(int(line.strip()))

x = [sum([lst[i] for i in range(y,y+3)]) for y in range(0, 2000-2)]
z = [i for i in range(0,len(x)-1) if x[i+1]>x[i]]
print(len(z))
