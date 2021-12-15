#------------------------------------------------------------------------------------
#DAY13
#------------------------------------------------------------------------------------
#DAY12
ll = [ x.split('-') for x in open('day12.txt').read().strip().split('\n')]
d = {}

for ele in ll:
    if ele[0] in d.keys() and ele[1] not in d[ele[0]]: d[ele[0]] += [ele[1]]
    else: d[ele[0]] = [ele[1]]
    if ele[1] in d.keys() and ele[0] not in d[ele[1]]: d[ele[1]] += [ele[0]]
    else: d[ele[1]] = [ele[0]]

def distinct_ways(l,d,init):
    start, total= d['start'], 0
    def helper(path,visited,smalls):
        if path in visited:
            if path == path.upper(): #upper case
                nexts = d[path] 
                return total + sum(helper(x,visited+[path],smalls) for x in nexts)
            else: #lower case
                if path != 'start' and not smalls: 
                    nexts = d[path] 
                    return total + sum(helper(x,visited+[path],True) for x in nexts)
                else: return 0   
        else:
            if path == 'end': return 1
            else:
                nexts = d[path] 
                return total + sum(helper(x,visited+[path],smalls) for x in nexts)
            
    return total + sum(helper(x,['start'],init) for x in start)

print(f'part 1: {distinct_ways(ll,d,True)} \npart 2: {distinct_ways(ll,d,False)}') #4720 147848
#------------------------------------------------------------------------------------
#DAY11
ll = [[int(y) for y in x] for x in open('day11.txt').read().strip().split('\n')]
flash = 0

def any_ten(ll):
    return sum(row.count(10) for row in ll)
def all_zero(ll):
    return sum(row.count(0) for row in ll) == 100
def cont_flasher(i,j):
    global flash
    ind = [(i+1,j), (i-1,j), (i,j-1), (i,j+1), (i-1,j-1), (i-1,j+1),(i+1,j-1),(i+1,j+1)]
    for (di,dj) in ind:
        if di in range(10) and dj in range(10):
            if ll[di][dj] !=0 : ll[di][dj] = ll[di][dj]+ 1
            if ll[di][dj] > 9:
                ll[di][dj] = 0
                flash += 1
                cont_flasher(di,dj)

count = 0
while not all_zero(ll): 
    count+=1 
    if count == 101: print(f'#part 1: {flash} flashes') #1615
    ll = [[ele+1 for ele in row] for row in ll]
    while any_ten(ll):
        for i in range(10):
            for j in range(10):
                if ll[i][j] > 9:
                    ll[i][j] = 0
                    flash += 1
                    cont_flasher(i,j)
print(f'#part 2: all flash at step {count}') #249
#------------------------------------------------------------------------------------
#DAY10
ll = [x for x in open('day10.txt').read().strip().split('\n')]
flaw = {')': 3, ']': 57, '}':1197, '>': 25137}
matcher = {')': '(', ']': '[', '}':'{', '>': '<'}
score = {')': 1, ']': 2, '}':3, '>': 4}
matcher2 = {v:k for k,v in matcher.items()}
all_scores, summ = [],0

for line in ll:
    stack = []
    for chara in line:
        if chara in '({[<': stack.append(chara)
        else: 
            last = stack.pop()
            if matcher[chara] != last: 
                summ += flaw[chara] #part 1
                break
    else: #part 2
        s = 0
        while len(stack) !=0:
            s *=5
            curr = stack.pop()
            s += score[matcher2[curr]]
        all_scores.append(s)

all_scores.sort() 
print(summ, all_scores[len(all_scores)//2]) #394647 2380061249
#-------------------------------------------------------------------------------------------
#DAY9 (could not do part 2, part 1 referenced too)
lst = [[int(y) for y in x] for x in open('day9.txt').read().strip().split('\n')]
     
risk_sum = 0
for r in range(len(lst)):
    for c in range(len(lst[0])):
        if r>0 and lst[r][c] >= lst[r-1][c]: continue #up
        if r<len(lst)-1 and lst[r][c] >= lst[r+1][c]: continue #not last row, down
        if c>0 and lst[r][c] >= lst[r][c-1]:continue #not sidest left, left
        if c<len(lst[0])-1 and lst[r][c] >= lst[r][c+1]: continue #not sidest right, right
        risk_sum += int(lst[r][c])+1
print(risk_sum) #575
#part2 (not mine)
from collections import Counter
ll = [[int(y) for y in x] for x in open('day9.txt').read().strip().split('\n')]
def basin(i,j):
	downhill = None
	for (di, dj) in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
		if di in range(len(ll)) and dj in range(len(ll[0])):
			if ll[i][j] > ll[di][dj]:
				downhill = (di, dj)
	if downhill is None:
		return (i, j)
	ret = basin(*downhill) #not entirely sure how this works
	return ret
basins = []
for i in range(len(ll)):
	for j in range(len(ll[0])):
		if ll[i][j] != 9:
			basins.append(basin(i, j))
ret = 1
for basin, common in Counter(basins).most_common(3): ret *= common
print(ret) #1019700
#-------------------------------------------------------------------------------------------------------
#DAY8
summ = 0
with open('day8.txt','r') as file:
    for line in file:
        front,back = line.strip().split('|')
        back = [i for i in back.strip().split(' ') if len(i) in [2,3,4,7]]
        summ +=len(back)
print(summ) #476

def sub(back,first): #part2
    first = first.strip().split(' ')
    one,four = [i for i in first if len(i) == 2][0], [i for i in first if len(i) == 4][0]
    output = ''
    for n in back:
        l = len(n)
        if l in [2,3,4,7]:
            output+= str(1*(l==2) + 4*(l==4) + 7*(l==3) + 8*(l==7))
        elif l == 5:
            if len([i for i in one if i in n]) == 2: output+='3'
            elif len([i for i in four if i in n]) ==3 : output +='5'
            else: output += '2'
        else:
            if len([i for i in one if i in n]) != 2: output+='6'
            elif len([i for i in four if i in n]) == 4 : output +='9'
            else: output += '0'
    return int(output)
summ = 0
with open('day8.txt','r') as file:
    for line in file:
        front,back = line.strip().split('|')
        back = back.strip().split(' ')
        summ+= sub(back,front)  
print(summ) #1011823
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
