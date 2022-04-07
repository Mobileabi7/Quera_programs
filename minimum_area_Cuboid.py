# minimum area of cuboid , Volume is constant 
# <=1 v =< 1,000,000
s = []
V = float (input())
#for minimum of s ----> should x,y,z

for x in range(1,100):
    for y in range(1,100):
        for z in range (1,100):
            if (x*y*z) == V:
                s.append((2*x*y)+(2*x*z)+(2*y*z))
print(min(s))

