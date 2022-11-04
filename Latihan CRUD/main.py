import os
import re
import CRUD as crud
from CRUD import Util

if __name__ == '__main__':
    OS = os.name
    match OS:
        case 'posix': os.system('clear')
        case 'nt': os.system('cls')
    Util.template_welcome()
    # check datbase ada atau tidak
    crud.init_console()

    while (True):
        match OS:
            case 'posix': os.system('clear')
            case 'nt': os.system('cls')
        Util.template_welcome()
        Util.template_menu()

        user_option = input('Choose your option? ')
        match user_option:
            case '1': crud.read_console()
            case '2': crud.create_data()
            case '3': crud.update_console()
            case '4': crud.delete_console()

        is_done = input('Apakah anda ingin selesai (y/n)? ')
        if re.search('^[y|Y]', is_done):
            break

    print('Program finished thanks for joining this code')
