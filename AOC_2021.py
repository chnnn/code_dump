
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
