import math
file = open('input.txt', "r")
l = open("output.txt", "w")
a = file.read().split(" ")

def f(t):
    t=float(t)
    y=math.sqrt(t**3-1)+3.31
    k=math.sin(2*y+1.21)
    return [t,y,k]

result=f(a[0])

string=str(result[0])+" "+str(result[1])+" "+str(result[2])

print(string)
l.write(string)

file.close()
l.close()

