import sys
import os
from file_manager import create_file, create_folder, copy_file_or_folder, delete_file_or_folder, get_list, save_info, \
    change_dir, start_game, start_reverse_game

save_info('start')
try:
    command = sys.argv[1]
except IndexError as e:
    print('choose command, for example " help" for list of commands')
else:
    if command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError as e:
            print('enter file name,', e)
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError as e:
            print('enter folder name,', e)
        else:
            create_folder(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError as e:
            print('enter file/folder name and new file name,', e)
        else:
            copy_file_or_folder(name, new_name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError as e:
            print('enter file/folder name,', e)
        else:
            delete_file_or_folder(name)
    elif command == 'list':
        get_list()
    elif command == 'save_info':
        try:
            message = sys.argv[2]
        except IndexError as e:
            print('enter message,', e)
        else:
            save_info(message)
    elif command == 'help':
        print('create_file (name, text) - создать файл')
        print('create_folder (name, text) - создать папку')
        print('copy (name, new_name) - скопировать папку или файл')
        print('delete (name) - удалить папку или файл')
        print('get_list() - получить список папок и файлов, get_list(folders_only=True) - получить список папок')
        print('save_info(message) - сохранить лог в log.txt с указанием месседжа')
    elif command == 'cd':
        path = sys.argv[2]
        change_dir(path)
        print(os.path.curdir)
    elif command == 'game':
        start_game()
    elif command == 'reverse_game':
        start_reverse_game()
    else:
        print(f'there\'s no such command "{command}"')

save_info('end')
