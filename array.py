# # import array
# # nilai= array.array("i",[5,6,4,8,7])
# # #menggunakan operator *
# # print(*nilai, sep=",")
# # #menggunakan for
# # for i in nilai:
# #     print(i,end="")
# # print()
# # print(nilai[2])


# #soal 1 : Membuat dan Menampilkan Array
# nilai=[10,20,30,40,50]
# print(*nilai,sep=",")

# #soal 2 : Menampilkan Elemen Tertentu
# nilai=[10,20,30,40,50]
# print(f'nilai elemen 1: {nilai[0]}')
# print(f'nilai elemen 3: {nilai[2]}')
# print(f'nilai elemen 5: {nilai[4]}')

# #soal 3 : Mengubah Nilai Elemen
# angka= [5, 10, 15, 20, 25]
# angka[1]=100
# for i in angka:
#     print(i,end=" ")
# print()

# #soal 4 : Menjumlahkan Semua Elemen
# data= [4, 8, 2, 6, 10]
# total= sum(data)
# print (total)

# # soal 5 : Mencari Nilai Tertinggi dan Terendah
# a= [12, 45, 7, 22, 89, 3]
# tertinggi= max(a)
# terendah= min(a)
# print(f'nilai tertinggi : {tertinggi}')
# print(f'nilai terendah : {terendah}')

# # soal 6 : Menampilkan Hanya Elemen Genap
# b= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# number= []
# for i in b:
#    if i % 2==0:
#      number.append(i)
# print(*number)

# # soal 7 : Menghitung Rata-rata Nilai
# c= [60, 70, 80, 90, 100]
# total= sum(c)
# jumlah_data= len(c)
# rata_rata= total/jumlah_data
# print(f'rata-rata nilai : {rata_rata}')








# ######kelas######

#students= ["bob","you","dea"] #array of string
# students_scor = [1,4,6,3] #' array of integer
# b_students_scor = len(students_scor)
# for i in range (b_students_scor):
#    print(students_scor [i])

# x = []
# x.append(1)
# x.append(2)
# x.append(3)
# x.append(4)
# x.append(5)
# print(x)

# banyak_x = len(x)
# for i in range (banyak_x):
#     myin = int(input())
#     x.append(myin)
# print(x)


#pakai bawaan pyton
# student_scor = [ 80, 90, 95, 100, 100]
# total =sum(student_scor)
# jumlah_data= len(student_scor)
# rata_rata =total/jumlah_data
# print(rata_rata)


#dasar nya
# student_scor = [ 80, 90, 95, 100, 100]
# banyak_data= len(student_scor)
# total= 0
# for i in range(banyak_data):
#     total += student_scor[i]
# rata_rata = total /banyak_data
# print(rata_rata)

student_scor = [ 80, 90, 95, 100, 100] # tidakj menggunakan array kosong
for i in range (len(student_scor)):
    student_scor[i]= student_scor[i] + (student_scor[i] * 10/100)
    if student_scor [i] >100:
        student_scor [i]=100
        
print(student_scor)

student_scor = [ 80, 90, 95, 100, 100] # menggunakan array kosong
final_scor = []
jumlah_data = len(student_scor)
for i in range (jumlah_data):
    original = student_scor[i]
    bonus = original + (0.1*original)
    if bonus >100:
        bonus = 100
    final_scor.append(bonus)
print(final_scor)
   