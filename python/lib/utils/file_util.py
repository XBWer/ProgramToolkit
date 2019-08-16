# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：		file_util
   Description :	
   Author :			bowenxu
   Create date：		12/9/18
   Update date:		12/9/18
-------------------------------------------------
"""

import os
from subprocess import call
import shutil


def read_kth_line_of_file(file_path, k):
    '''
    read kth line from a file, k start from 0
    :param file_path:
    :param k:
    :return:
    '''
    with open(file_path) as fp:
        for i, line in enumerate(fp):
            if i == k:
                return str(line).strip()


def write_file(file_path, obj):
    write_str = ''
    if type(obj) == list:
        write_str = ('\n'.join(obj))
    elif type(obj) == str:
        write_str = obj
    else:
        write_str = obj
    file_object = open(file_path, 'wb')
    file_object.write(write_str.encode('utf-8').strip())
    file_object.close()


def insert_str_at_end(file_path, str):
    my_open = open(file_path, 'a')
    my_open.write(str)
    my_open.close()


def clean_dir(dir_path):
    import os
    if os.path.exists(dir_path):
        import shutil
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)


def get_par_path(path):
    import os.path
    return os.path.abspath(os.path.join(path, os.pardir))


def cp_dir(source, target):
    if not os.path.exists(target):
        os.mkdir(target)
    call(['cp', '-r', source, target])


def delete_dir(source):
    call(['rm', '-rf', source])


def cp_file(source, target):
    call(['cp', source, target])


def write_str2file(file_path, w_str):
    with open(file_path, 'w') as the_file:
        the_file.write(str(w_str))


def write_byte2file(file_path, w_byte):
    with open(file_path, 'wb') as the_file:
        the_file.write(w_byte)


def write_list2file(file_path, w_list):
    with open(file_path, "a+") as f:
        for item in w_list:
            f.write(str(item) + "\n")


def read_file_to_str(file_path):
    with open(file_path, 'r') as myfile:
        data = myfile.read()
    return data


def read_file_into_line_list(file_path, if_strip=False):
    with open(file_path) as f:
        content = f.readlines()
    if if_strip:
        content = [x.strip() for x in content]
    else:
        content = [x for x in content]
    return content


def list_files(dir):
    import os
    dir_list = [dir]
    file_list = []
    while len(dir_list) != 0:
        cur_dir = dir_list[0]
        for f in os.listdir(cur_dir):
            if os.path.isdir(cur_dir + os.sep + f):
                dir_list.append(cur_dir + os.sep + f)
            elif os.path.isfile(cur_dir + os.sep + f):
                file_list.append(cur_dir + os.sep + f)
        dir_list.pop(0)
    return file_list


def move_files(src, dst):
    shutil.move(src, dst)


def remove_file(file_path):
    os.remove(file_path)


def clear_folder(dir_path):
    for item in os.listdir(dir_path):
        itemsrc = os.path.join(dir_path, item)
        shutil.rmtree(itemsrc)


def copy_file(fpath, dst):
    from shutil import copyfile
    try:
        copyfile(fpath, dst)
    except Exception as e:
        import subprocess
        cmd = "cp -f {} {}".format(fpath, dst)
        subprocess.call(cmd, shell=True)


def remove_dir(dir_path):
    import shutil
    try:
        shutil.rmtree(dir_path)
    except Exception as e:
        import subprocess
        cmd = "rm -rf {}".format(dir_path)
        subprocess.call(cmd, shell=True)
