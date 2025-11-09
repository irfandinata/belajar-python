# # # n= float(input())

# # # if n<=0 or n!=int(n):
# # #    print("NoProceed")
# # # else:
# # #    n= int(n)
# # #    for i in range(1,n+1):
# # #       output= i * (i+1)//2
# # #       if i<n:
# # #          print(f'{output}', end=", ")
# # #       else:
# # #          print(f'{output}', end="")
      

# # #sum
# # n= float(input())

# # if n<=0 or n!=int(n):
# #     print("NotProceed")
# # else:
# #     n= int(n)
# #     total_bil = 0.0
# #     f= False
# #     for i in range(n):
# #         angka= float(input())
# #         if angka % 1 !=0:
# #             total_bil += angka
# #             f= True

# #     if not f:
# #         print(0)
# #     else:
# #         print(float(total_bil))


# # # kode 2
# # # n= float(input())

# # # if n<=0 or n!=int(n):
# # #     print("NotProceed")
# # # else:
# # #     n= int(n)
# # #     total_bil = 0.0
# # #     for i in range(n):
# # #         angka= float(input())
# # #         if angka % 1 !=0:
# # #             total_bil += angka

# # #     print(float(total_bil)if total_bil !=0 else 0)

    

# #kode h2
# n= int(input())
# kode={"O":1000,
#       "EO":900,
#       "F":500,
#       "EF":400,
#       "E":100,
#       "ZE":90,
#       "N":50,
#       "ZN":40,
#       "Z":10,
#       "KZ":9,
#       "X":5,
#       "KX":4,
#       "K":1,}

# hasil= ""
# if n<1 or n>3999:
#     print("NoProceed")
# else:
#     sisa= n
#     for simbol,nilai in kode.items():
#         while sisa >= nilai:
#           hasil +=simbol
#           sisa -=nilai
#     print(hasil)


#############belajar############
#nested if#
# x= int(input("masukan nilai: "))
# if x>60:
#     if x==100:
#         print("selamat kamu lulus dengan nilai terbaik")
#     print("kamu lulus")
# else:
#     print("kamu tidak lulus")

# umur=int(input())
# print("kamu bisa memilih")if umur>17 else print("kamu tidak bisa memilih")

n= int(input())
if n>=70 and n<=100:
    print("anda lulus")
else:
    print("anda tolol")