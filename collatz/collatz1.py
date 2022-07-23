a = int(input('a?: '))
print(a)

maxiter = 1000
for i in range(maxiter):
    if a == 1:
        break
    if a%2 == 0:
        a = a//2
    else:
        a = 3*a + 1
    print(a)
   
