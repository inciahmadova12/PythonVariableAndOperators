#Compare two numbers
num1=int(input())
num2=int(input())
if num1>num2:
    ptint(f"{num1}is greater than {num2}")
elif num1==num2:
    print(f"{num1}is equal to {num2}")
else:
    print(f"{num1}is less than {num2}")


#Check if a number is positive, negative, or zero
num=int(input())
if num>0:
    ptint(f"{num}is positive")
elif num==0:
    ptint(f"{num}is equal to zero")
else:
     ptint(f"{num}is negative")


#  Check if a number is even or odd
num=int(input())
if num%2==0:
    ptint(f"{num}is even")
else:
    ptint(f"{num}is odd")


#Exam grade
score=int(input())
if score<0:
    print("Invalid score")
elif score>100:
    print("Invalid score")
elif score>=91:
    print("Grade: A")
elif score>=81:
    print("Grade: B")
elif score>=71:
    print("Grade: C")
elif score>=61:
    print("Grade: D")
elif score>=51:
    print("Grade: E")
else:
    print("Grade: F")


#Find the largest of three numbers
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(f"{num1}is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2}is the largest number")
else:
    print(f"{num3}is the largest number")


#Simple calculator
num1=int(input())
num2=int(input())
operation=input()
if operation =='+':
    print( num1+num2)
elif operation=='-':
    print( num1-num2)
elif operation=='*':
    print( num1*num2)
elif operation=='/':
    print( num1/num2)
elif operation=='%':
    print( num1%num2)
elif operation=='**':
    print( num1**num2)
elif operation=='//':
    print( num1//num2)
else:
    print("Invalid operation")


#Age category
age=int(input())
if age<0:
    print("Invalid age")
elif age<=12:
    print("Child")
elif age<=17:
    print("Teenager")
elif age<=64:
    print("Adult")
else:
    print("Senior")


#Discount calculator
amount=int(input())
if amount<100:
    print(f"{amount},no discount")
elif amount>=100 and amount<=299:
    b=amount*0.9
    print(f"{amount},10%,{b}")
elif amount>=300 and amount<=499:
    c=amount*0.75
    print(f"{amount},15%,{c}")
else:
    d=amount*0.8
     print(f"{amount},20%,{d}")


#order three numbers
num1=int(input())
num2=int(input())
num3=int(input())
if num1<=num2 and num1<=num3:
    smallest=num1
    if num2<=num3:
        middle=num2
        largest=num3
    else:
        middle=num3
        largest=num2
elif num2<=num1 and num2<=num3:
    smallest=num2
    if num1<=num3:
        middle=num1
        largest=num3
    else:
        middle=num3
        largest=num1
else:
    smallest=num3
    if num1<=num2:
        middle=num1
        largest=num2
    else:
        middle=num2
        largest=num1
print(smallest,middle,largest)


#ATM WITHDRAWAL
balance=1000
withdraw=int(input())
if withdraw<=0:
    print("Invalid amount")  
elif withdraw>balance:
    print("Insufficient balance")  
else:
    balance=balance-withdraw
    print(balance)  


#Electricity bill
usage=int(input())
if usage<0:
    print("Invalid input")  
elif usage<=100:
    rate=0.08  
    total=usage*rate
     print(usage,rate,total)   
elif usage<=300:
    rate=0.12  
    total=usage*rate
     print(usage,rate,total) 
else:
    rate=0.15
    total=usage*rate
    print(usage,rate,total)  


#Taxi fare
starting_fee=2.0
distance=int(input())
if distance<0:
    print("Invalid input")
elif distance<=5:
    distance_fee=distance*0.70
    print(distance_fee)
elif distance<=15 and distance>5:
    distance_fee=distance*0.60
    print(distance_fee)
else:
    distance_fee=distance*0.50
    print(distance_fee)


#
a = int(input(""))
b = int(input(""))
c = int(input(""))

if a + b > c:
    if a + c > b:
        if b + c > a
            if a == b and b == c:
                print("Equilateral")
            elif a == b or b == c or a == c:
                print("Isosceles")
            else:
                print("Scalene")
        else:
            print("Triangle cannot be created")
    else:
        print("Triangle cannot be created")
else:
    print("Triangle cannot be created")
