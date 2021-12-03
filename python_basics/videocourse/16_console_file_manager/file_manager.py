import datetime
import os
import shutil
import guess_the_number
import computer_guess_the_number


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError as e:
        print('file already exist', e)


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [folder for folder in result if os.path.isdir(folder)]
    print(result)


def delete_file_or_folder(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError as e:
        print('file not found:', e)


def copy_file_or_folder(name, new_name):
    try:
        if os.path.isdir(name):
            shutil.copytree(name, new_name)
        else:
            shutil.copy(name, new_name)
    except FileExistsError as e:
        print(e)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{result}\n')


def change_dir(path):
    os.chdir(path)
    print('current dir path:', os.getcwd())


def start_game():
    guess_the_number.start_game()


def start_reverse_game():
    computer_guess_the_number.start_game()

# if __name__ == '__main__':
#     save_info('info')
#     copy_file_or_folder('test.dat', 'test_2.dat')
#     create_file('test.dat', 'some text')
#     create_folder('folder_for_test')
#     delete_file_or_folder('test.dat')
#     delete_file_or_folder('folder_for_test')
#     get_list()
#     get_list(folders_only=True)
