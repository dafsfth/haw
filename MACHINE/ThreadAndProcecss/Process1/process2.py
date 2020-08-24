# 使用多进程拷贝文件

import os, multiprocessing


def copy1(file_name1, dest_dir1, source_dir1):
    source_path = source_dir1 + '\\' + file_name1
    dest_path = dest_dir1 + '\\' + file_name1

    with open(source_path, 'rb') as read_source:
        with open(dest_path, 'wb') as write_source:
            while True:
                data = read_source.read(1024)
                if data:
                    write_source.write(data)
                else:
                    break


if __name__ == '__main__':
    dest_dir = 'E:\LEARN\PYTHON\Picture'
    source_dir = 'D:\\untitled1\python文件\photo\demo1\\4'
    # try:
    #     os.mkdir(dest_dir)
    # except:
    #     print('文件夹已创建')

    file_list = os.listdir(source_dir)
    for file_name in file_list:
        p = multiprocessing.Process(target=copy1, args=(file_name, dest_dir, source_dir))
        p.start()
    print('ok')


