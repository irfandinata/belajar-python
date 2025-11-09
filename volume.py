# # #mengitung volume tabung
# # diameter=int(input())
# # tinggi=10+diameter

# # r=diameter/2
# # if r%7==0:
# #  phi=22/7
# # else:
# #   phi= 3.14
# # volume=phi*r*r*tinggi
# # print("volume tabung adalah ",volume)

# # r= float(input())
# # if r%7==0:
# #     phi=22/7
# # else:
# #     phi= 3.14
# # hasil=phi*r*r
# # print(hasil)


# a= int(input())
# t= int(input())
# if a<0:
#     print("NoProceed")
# else: 
#     hasil= 1/2*a*t
#     print(f"{hasil:g}")


# #pola bintang
# n= int(input())
# if n<=0:
#     print("NoPattern")
# else:
#     for i in range(1,n+1):
#         print('*'*i)


# #faktorial salah
# import math
# a= int(input())
# for i in range(4):
#     n= int(input())
#     if n>a:
#        a=n

# print(a)
# if a<0:
#     print("NoProceed")
# else:
#     x= math.factorial(a)
#     print(x)


#kedua salah
# import math
# a=[]
# for i in range(5):
#     n= int(input())
#     a.append(n)
# b= max(a)

# print(b)
# if b<0:
#     print("NoProceed")
# else:
#     x= math.factorial(b)
#     print(x)



# n = int(input())
# variabel = {
#      "O": 1000,"EO":900,"F":500,"EF":400,"E":100,"ZE":90,"N":50,"ZN":40,"Z":10,"KZ":9,"X":5,"KX":4,"K":1,
# }

# hasil = ""

# if n < 1:
#     print('NoProceed')
# elif n > 3999:
#     print('NoProceed')
# else:
#     for huruf, nilai in variabel.items():
#         while n >= nilai:
#             hasil = hasil+huruf
#             n = n-nilai
# print(hasil)



# #kode segitiga
# a= float(input())

# if a<=0 or a!=int(a):
#     print("NoProceed")
# else:
#     a= int(a)
#     for i in range(1,a+1):
#         hasil= i * (i+1)//2
#         if i<a:
#             print(f'{hasil}', end=", ")
#         else:
#             print(f'{hasil}', end="")


#kode segitiga 2
# a=float(input())

# if a>0 and a == int(a):
#   a= int(a)
#   for i in range(1,a+1):
#       hasil= i * (i+1)//2
#       if i<a:
#           print(f"{hasil}", end=", ")
#       else:
#           print(f'{hasil}', end="")
# else:
#     print("NoProceed")


# n = float(input())
# if n <= 0:
#     print("NoProceed")
# elif n != int(n):
#     print("NoProceed")
# else:
#     n = int(n)
#     for i in range(1, n+1):
#         hasil = i * (i + 1) // 2
#         if i < n:
#             print(hasil, end=", ")
#         else:
#             print(hasil, end="")



####kode pemdassssss m2
# largest = int(input())

# for i in range(1,5):
#     number = int(input())
#     if number > largest:
#         largest = number

# print(largest)

# if largest > 0:
#     factorial = 1
#     for i in range(largest, 0, -1):  
#         factorial *= i
#     print(factorial)
# else:
#     print("NoProceed")



##########M2
# import math

# Input 5 numbers
# numbers = []
# for i in range(5):
#     num = int(input())
#     numbers.append(num)

# # Find the largest number
# largest = max(numbers)

# # Display the largest number
# print(largest)

# # Calculate factorial if it's a positive integer
# if largest > 0:
#     factorial = math.factorial(largest)
#     print(factorial)
# else:
    # print("NoProceed")




###################M2####


a= None

for i in range(5):
    num = int(input())
    if num >= 0 and ( a is None or num > a):
       a = num

if a is None:
    print(-1)
    print("NoProceed")
else:
    print(a)
    hasil = 1
    for i in range(1, a + 1):
        hasil *= i
    print(hasil)