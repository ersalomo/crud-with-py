from . import Operasi
TEMPLATE = {
    'pk': 'xxxxxx',
    'time_add': 'yyyy-mm-dd',
    'penulis': 250 * ' ',
    'judul': 250 * ' ',
    'tahun': 'yyyy',
}
DB_NAME = 'data.txt'


def init_console():
    try:
        with open(DB_NAME, 'r') as file:
            print('database tersedia')
    except:
        print('datbase tidak tersedia/error')
        Operasi.create_first_data()
