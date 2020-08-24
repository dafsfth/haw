import os, threading


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
    local_dir = 'E:\CodeFile\Demo\\a\\4'
    goal_dir = '/pic'

    if not os.path.exists(goal_dir):
        os.makedirs(goal_dir)

    file_list = os.listdir(local_dir)

    for file_name in file_list:
        t = threading.Thread(target=copy1, args=(file_name, goal_dir, local_dir))
        t.start()