# a=int(input())
# b=int(input())

# sum=0
# print(f'{a} x {b}', end= "=")
# for i in range(1,a+1):

#     sum +=b
#     if i <a:
#       print(b,end='+')
#     else:
#      print(b, end='=')

# print(sum)

# fibonaci
# a,b= 0,1
# n=int(input())

# for i in range(n-2):
#   print(a,end=" ")
#   a,b=b,a+b 

# if n==0:
#   print("no result")

#   cara bapaknya
n = int(input())
a = 0
b = 1
bilnext = 0
if n <=0 :
    print("no result")
elif n==1:
    print(0)
else:
    print (f'{a} {b}',end=" ")
    for i in range(n-2):
    #   bilnext= a + b
      print(bilnext, end= " ")
      a = b
      b = bilnext

