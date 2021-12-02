#DAY 1  
lst = []
with open('input.txt','r') as file:
    for line in file:
        lst.append(int(line.strip()))

x = [sum([lst[i] for i in range(y,y+3)]) for y in range(0, 2000-2)]
z = [i for i in range(0,len(x)-1) if x[i+1]>x[i]]
print(len(z))

#-------------------------------------------------------------------------------------------------------
#DAY 2 A
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
