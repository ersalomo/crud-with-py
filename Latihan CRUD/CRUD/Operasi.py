from . import Database, Util
import os


def delete(no_nuku):
    try:
        with open(Database.DB_NAME, 'r') as f:
            counter = 0

            while True:
                content = f.readlines()
                if (len(content) == 0):
                    break
                elif counter == no_nuku - 1:
                    pass
                else:
                    with open(Database.DB_NAME, 'a', encoding='utf-8') as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")

    os.rename("data_temp.txt", Database.DB_NAME)


def create_first_data():
    penulis = input('Penulis : ')
    judul = input('Judul : ')
    tahun = input('Tahun : ')

    data = Database.TEMPLATE.copy()

    data['pk'] = Util.nanoid(6)
    data['time_add'] = Util.time_add()
    data['penulis'] = penulis.title(
    ) + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul.title() + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun
    data_str = f"""{data['pk']},{data['judul']},{data['penulis']},{data['tahun']},{data['time_add']}"""

    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
    except:
        print('Tidak dapat menemukan database')


def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_data = len(content)

            if 'index' in kwargs:
                index_buku = kwargs['index'] - 1
                if index_buku < 0 or index_buku > jumlah_data:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print('There are error')
        return False


def update(no_buku, pk, data_add, tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f"{data['pk']},{data['judul']},{data['penulis']}"
    panjang_data = len(data_str)

    try:
        with (open(Database.DB_NAME, 'r+', encoding='utf-8')) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print('error while updatin data')


def create_data():
    penulis = input('Penulis : ')
    judul = input('Judul : ')
    tahun = input('Tahun : ')

    data = Database.TEMPLATE.copy()

    data['pk'] = Util.nanoid(6)
    data['time_add'] = Util.time_add()
    data['penulis'] = penulis.title(
    ) + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul.title() + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun

    data_str = f"""{data['pk']},{data['judul']},{data['penulis']},{data['tahun']},{data['time_add']}"""

    try:
        with open(Database.DB_NAME, 'a', encoding='utf-8') as file:
            file.writelines(data_str)
            return
    except:
        print('Tidak dapat menemukan database')


def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = Util.nanoid(6)
    data["date_add"] = Util.time_add()
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan boooos, gagal maning")
