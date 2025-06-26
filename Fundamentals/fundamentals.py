# """<---------------------python output------------------------------------------>"""
# # print('hello world')
# # print(7+6,True,6.7,'ayush',sep='\n')
# # print('Hinata Hyuga',end="@",sep="&")
# # print('Ayush')
# """<-------------------Python Datatypes---------------------------------->"""
# #-------Integer---->
# x=2e4 #e=10^something
# # print(x)


# #<------Boolean------------>
# # print(int(True))
# #<---------tuples,list,sets,dictionary------------------------>
# t1=(1,2,3,4,5)
# l1=[1,3,4,5,6]
# s1={1,2,4,5,6}
# d1={"name":'ayush','age':21,'skills':['python','javascript','mysql']}
# print(type(t1),type(l1),type(s1),type(d1))

#<-------variables------------------------------->
# static typing-no need to declare the type of the variable python is inference typed language and supports dynamic typing
# a,b=1,'itachi'
#<----------------dynamic binding------------------>
#the value of the variable can be changed independent of datatype eg first value of a is int,then it can be changed to string,the variable can hold different types
# a=1
# # print(a)
# a='shisui'
# # print(a)
# a,b,c=1,2,3
# print(a,b,c)
# a=b=c=4
# print(a,b,c)

# print(f'the sum of two numbers is {int(input('Enter the number1 :')) +int(input('Enter the number2 :'))+int(input('Enter the number3 :'))}')
# x=int(input("Enter a number :"))
# a=x%10
# num=x//10
# b=num%10
# num=num//10
# c=num%10
# print(a+b+c)

# s=0
# for i in str(x):
#     s+=int(i)
# print(s)
# username=input("Enter the username :")
# password=input("Enter the password :")
# if(username=='ayuhina' and password=='#456'):
#     print('welcome')
# elif(username=='ayuhina' and password!='#456'):
#     print("Enter the password again")
#     password=input("Enter the password :")
#     if(password!='#456'):
#         print('incoorect password,logging out')
#     else:
#         print('Welcome User')
# else:
#     print('incorrect password')
# num=int(input("Enter the number : "))
# n=int(input("Enter the number of times you want to print the table :"))
# for i in range(1,n+1):
#     print(num ,'*',i,'=', num * i)
# i=1
# while(i<=n):
#     print(num,'*',i,'=',num*i)
#     i+=1
# import random
# att=4
# n=random.randint(1,21)
# print(n)
# print('Guess the number between 1 and 20')
# while(att>0):
#     num=int(input("Enter the guessed number :"))
#     if(num==n):
#         print("Congratulation you guessed the right number 🏆")
#         break
#     elif(num>n):
#         print(" Wrong ❌ ,The number is smaller than than guessed number")
#         print(f'you have {att} chances left to guess the name')
#         att-=1
#     else:
#         print(" Wrong ❌ ,The number is bigger than than than guessed number")
#         print(f'you have {att} chances left to guess the name')
#         att-=1
# pop=10000
# for i in range(10,0,-1):
#     print('year',i,':',pop)
#     pop=pop/1.1

# s=0
# n=int(input("Enter the nth term :"))
# f=1
# for i in range(1,n+1):
#     f=f*i
#     s+=i/f
# print('The sum is :',s)
# for i in range(1,5):
#     for j in range(1,5):
#         print((i,j),end=" ")


#-bitwise solution for even or odd
def evod(n):
    if(n&1==0):
        print('even')
    else:
        print('odd')
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
def rev(x):
    ans=0
    n= -x if(x<0) else x
    while(n>0):
        rem=n%10
        ans=ans*10+rem
        n=n//10
    ans=-ans if(x<0) else ans
    print(ans)


def prime(n):
    f=0
    for i in range(1,n):
        if(n%i==0):
            f+=1
    if(f==1):
        return True
    else:
         return False
def pr(n):
    for i in range(1,n+1):
        if(prime(i)):
            print(i,end=" ")
def cn(n,k):
    v=1<<k
    ans=n|v
    print(ans)
l=[-1,-2,-3,-4,-5,-6,44,6546,3112,45]
max=l[0]
for i in range(len(l)):
    if(max< l[i]):
        max=l[i]
print(max)
m=[1,2,3,4,5,6,7,8,9,10,11]
i=0
j=len(m)-1
l=[]

while(True):
        if(i>j):
            break
        if(i==j):
            l.append((m[i],))
            break
        else:
            l.append((m[i],m[j]))
            i+=1
            j-=1
print(l)
# def p(n):
#     f=0
#     for i in range(2,n+1):
#         if(n%i==0):
#             f+=1
#     if(f==1):
#         return 1
#     else:
#         return 0
# def rop(n):
#     for i in range(1,n+1):
#         if(p(i)):
#             print(i,end=" ")

# rop(51)
l=[1,2,2,3,4,5]
a={}
for i in l:
    a[i]=a.get(i,0)+1

print(a.get(2))

