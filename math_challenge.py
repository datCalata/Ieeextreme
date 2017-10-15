import scipy.special

def modexp(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y



line1 = int(input())
lines = []
for i in range(0,line1):
    lines.append(input())

new_lines = []
for i in lines:
    new_lines.append(i.split())
    
numbers = []
for i in range(0,len(new_lines)):
     numbers.append([int(j) for j in new_lines[i]])

print(numbers)

mod = 10e9 + 7

for nums in numbers:
    a = nums[0]
    b = nums[1]
    c = nums[2]
    ov = scipy.special.binom(b, c)
    res = modexp(a,ov,mod)
    print(str(res))
    
    