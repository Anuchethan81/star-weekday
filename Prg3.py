# Loops
#for loop

for i in range(2, 13):
    print(i)

#even and odd numbers
for i in range(1,10,2):
    print(i)

#asc n desc order
for i in range(10,1,-2):
    print(i)

for i in range(100,49,-10):
    print(i)

#sum of all even number from 1 to 20

sum = 0
for i in range(2,31,2):
    sum1 = sum + i
print(sum1)

# while loop
a=0

while a<100 :
    a=a+2
print(a)

# if-else statement

balamt =3000
wdamt = int (input("enter the amount to withdraw "))
if wdamt>=balamt:
    print("insufficient amt")
else:
    balamt = balamt - wdamt
print("current bal is:" , balamt)
