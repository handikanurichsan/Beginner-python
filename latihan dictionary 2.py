import os
import random
import string
import datetime

buku_template = {
    'isbn' : '00000000000',
    'judul' : 'Belajar Python',
    'penulis' : 'John Doe',
    'penerbit' : 'Penerbit ABC',
    'tahun_terbit' : 2020,
    'jumlah_halaman' : 300,
}


dict_buku = {}

while True:
    os.system('cls')
    

    print(f'Selamat datang di program pembuatan dictionary buku!')

    data_buku = dict.fromkeys(buku_template.keys())

    data_buku['isbn'] = input('Masukkan ISBN buku: ')
    data_buku['judul'] = input('Masukkan judul buku: ')
    data_buku['penulis'] = input('Masukkan nama penulis buku: ')
    data_buku['penerbit'] = input('Masukkan nama penerbit buku: ')
    data_buku['tahun_terbit'] = int(input('Masukkan tahun terbit buku: '))
    data_buku['jumlah_halaman'] = int(input('Masukkan jumlah halaman buku: '))

    KEY =''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    # KEY = data_buku['isbn']

    dict_buku.update({KEY: data_buku})

    for buku in dict_buku:
      

        JUDUL = dict_buku[buku]['judul']
        ISBN = dict_buku[buku]['isbn']
        PENULIS = dict_buku[buku]['penulis']
        PENERBIT = dict_buku[buku]['penerbit']
        TAHUN_TERBIT = dict_buku[buku]['tahun_terbit']
        JUMLAH_HALAMAN = dict_buku[buku]['jumlah_halaman']
        print(f'{KEY}, {JUDUL}, {PENULIS}, {PENERBIT}, {TAHUN_TERBIT}, {JUMLAH_HALAMAN}')


    isContinue = input('Apakah Anda ingin menambah data buku lagi? (y/n): ')
    if isContinue.lower() == 'n':
        print('Terima kasih telah menggunakan program ini!')
        break


