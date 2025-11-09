# mencetak berapa huruf vokal yang ada di nama kita
n=int(input())
print("--------for--------")
total = 0
count = 0
for i in range(n,0,-1):
    print(i)
    total +=i
    count +=1

    print ("hasil= ",total)
    print("jumlah angka ",count)
    print("rata-rata = ",total/count)

#while
print ("------while----------")
i=n
while i>0:
    print(i)
    i-=1


print("--------do while--------")
i=n
while i>0:
    print(i,end='')
    i-=1
    if i==0:
        break


print("----------mencetak bintang------")
for i in range(1, n+1):
    for j in range(1, i+1):
      print("*",end= '')
    print()#new line


print("-----------mencetak bintang versi python---------")
for i in range(1,n+1):
    print('*'*i)