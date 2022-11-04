from . import Util
from . import Operasi as Op


def update_console():
    read_console()
    while True:
        no_buku = int(input('Masukkan no nuku'))
        data_buku = Op.read(index=no_buku)

        if data_buku:
            break
        else:
            print('nomor tidak valid, silahkan masukan lagi')

    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while (True):
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("judul\t: ")
            case "2": penulis = input("penulis\t: ")
            case "3":
                while (True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print(
                                "tahun harus angka, silahkan masukan tahun lagi (yyyy)")
                    except:
                        print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")
            case _: print("index tidak cuocuoook")

        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah data sudah sesuai(y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    Op.update(no_buku, pk, data_add, tahun, judul, penulis)


def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while (True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")
        except:
            print("tahun harus angka, silahkan masukan tahun lagi (yyyy)")

    Op.create(tahun, judul, penulis)
    print("\nBerikut adalah data baru anda")
    read_console()


def read_console():
    Util.read_view()
    data_file = Op.read()
    index = 'No'
    judul = 'judul'
    penulis = 'penulis'
    tahun = 'tahun'

    # header
    print('\n'+'='*100)
    print(f'|{index:3} | {judul:40} | {penulis:40} | {tahun:5} |')
    print('-'*100)
    for i, data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        judul = data_break[1]
        penulis = data_break[2]
        tahun = data_break[3]
        print(f'|{i+1:3} | {judul:.40} | {penulis:.40} | {tahun:.5}  |')

    print('='*100+'\n')
