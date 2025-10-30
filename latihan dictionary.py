import datetime
import os
import string
import random


# Program untuk membuat dictionary mahasiswa
mahasiswa_template = {
    'nama' : 'jon',
    'nim' : '123456789',
    'sks_lulus' : 144,
    'jurusan' : 'teknik informatika',
    'tanggal_lahir' : datetime.datetime(2000, 1, 1),
}

dict_mahasiswa = {}

while True:

    os.system('cls')
    print(f'Selamat datang di program pembuatan dictionary mahasiswa!')
    #ambil key dari mahasiswa_template
    mahasiswa = dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input('Masukkan nama mahasiswa: ')
    mahasiswa['nim'] = input('Masukkan NIM mahasiswa: ') 
    mahasiswa['sks_lulus'] = int(input('Masukkan SKS lulus mahasiswa: '))
    mahasiswa['jurusan'] = input('Masukkan jurusan mahasiswa: ')
    tahun_lahir = input('Masukkan tahun lahir mahasiswa (YYYY): ')
    bulan_lahir = input('Masukkan bulan lahir mahasiswa (MM): ')
    tanggal_lahir = input('Masukkan tanggal lahir mahasiswa (DD): ')
    mahasiswa['tanggal_lahir'] = datetime.datetime(int(tahun_lahir), int(bulan_lahir), int(tanggal_lahir))


    KEY = mahasiswa['nim']

    # KEY = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    dict_mahasiswa.update({KEY: mahasiswa})

  
    for mhs in dict_mahasiswa:
        
        
        NIM = dict_mahasiswa[mhs]['nim']
        NAMA = dict_mahasiswa[mhs]['nama']
        SKS_LULUS = dict_mahasiswa[mhs]['sks_lulus']
        JURUSAN = dict_mahasiswa[mhs]['jurusan']
        TANGGAL_LAHIR = dict_mahasiswa[mhs]['tanggal_lahir'].strftime('%d-%m-%Y')
        
        print(f'{KEY}, {NAMA}, {SKS_LULUS}, {JURUSAN}, {TANGGAL_LAHIR}')

    selesai = input('Apakah Anda ingin menambah data mahasiswa lagi? (y/n): ')
    if selesai.lower() == 'n':
        print('Terima kasih telah menggunakan program ini!')