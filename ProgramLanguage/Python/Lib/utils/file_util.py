# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     file_util
   Description :
   Author :       bowenxu
   date：          27/8/18
-------------------------------------------------
"""
import os


def read_file_to_string(fpath):
    try:
        if not os.path.exists(fpath):
            Exception("The file %s not exist!" % fpath)
        with open(fpath, 'rb') as myfile:
            fstr = myfile.read()
        return str(fstr.decode("utf-8"))
    except Exception as e:
        print('Read failed %s!' % fpath)
        print("Error: %s" % str(e))
        return None


def read_kth_line_of_file(fpath, k):
    '''
    read kth line from a file, k start from 0
    :param fpath:
    :param k:
    :return:
    '''
    with open(fpath) as fp:
        for i, line in enumerate(fp):
            if i == k:
                return str(line).strip()


def write_file(file_path, obj):
    write_str = ''
    if type(obj) == list:
        for tmp in obj:
            write_str += (str(tmp) + '\n')
    elif type(obj) == str:
        write_str = obj
    else:
        write_str = obj
    file_object = open(file_path, 'wb')
    file_object.write(write_str.encode('utf-8').strip())
    file_object.close()


def insert_str_at_end(fpath, str):
    my_open = open(fpath, 'a')
    my_open.write(str)
    my_open.close()


def clean_dir(dir_path):
    import os
    if os.path.exists(dir_path):
        import shutil
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)
