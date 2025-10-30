import os

os.system('cls')

def tambah(*data):
    output = 0
    for angka in data:
        output += angka

    return output

def kali(*data):
    output = 1
    for angka in data:
        output *= angka
    return output

def simple(*args, **kwargs):
    operasi = kwargs.get('opsi')
    if operasi == '+':
        return tambah(*args)
    elif operasi == '*':
        return kali(*args)
    else :
        print("operasi tidak valid")


# def tambah_kali(*gabungan, **option):
#     output = 0
#     if option ["opsi"] == '+':
#         for angka in gabungan:
#             output += angka
#     elif option ["opsi"] == "*":
#         output = 1
#         for angka in gabungan:
#             output *= angka
#     else:
#         print("Opsi tidak valid, gunakan '+' atau '*'")
    
#     return output


hasil = simple(1,2,3,4, opsi = '+')

print(f"hasil adalah {hasil}")


# print(f"hasil adalah {tambah(1,2,3,4)}")
# print(f"hasil adalah {kali(1,2,3,4)}")



# latihan lambda dasar
# lambda kuadrat
kuadrat = lambda angka : angka ** 3
print (kuadrat(3))

# lambda pangkat
pangkat = lambda nilai, pangkat : nilai ** pangkat
print (pangkat(2,2))

# menggabungkan dua string
gabung = lambda a, b : a + b
a = 'makan '
b = 'nasi'
print(gabung(a,b))

a = "dimanakah semua itu "
b = "apakah ada jalan"
print(gabung(a, b))

# latihan lambda level 2
# angka list jadi pangkat 3
data = [1,2,3,4,5]
pangkat_tiga = list(map(lambda angka:angka ** 3, data))

print(pangkat_tiga)

# ambil angka genap
data = [10,15,20,25,30,35,40]
genap = list(filter(lambda angka:angka % 2==0, data))

print(genap)

# latihan lambda level 3
# sorting custom
data = [
   
    ("budika", 25),
    ("andi", 30),
    ("citra", 20),
]
# berdasarkan alphabet
data.sort(key=lambda nama:nama[0]) 
print(f"berdasarkan alphabet = {data}") 
# berdasarkan panjang nama
data.sort(key= lambda nama:len(nama[0]))
print(f"berdasarkan panjang nama = {data}")
# berdasarkan urutan usia
data.sort(key = lambda usia:usia[1])
print("berdasarkan usia = {data}")

# level 4 kombinasi

kalimat = ["Python", "is", "awesome", "and", "fun"]

kombinasi = list(fill())
print(kombinasi)