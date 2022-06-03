def read_files_and_write_file(*files):
    file_dict = {}
    for file in files:
        with open(file, encoding='utf-8') as f:
            count = 0
            for line in f:
                count += 1
            temp_dict = file_dict.fromkeys([file], count)
            file_dict.update(temp_dict)

    sorted_tuple = sorted(file_dict.items(), key=lambda x: x[1])
    sorted_dict = dict(sorted_tuple)

    for key, value in sorted_dict.items():
        with open(key, 'r', encoding='utf-8') as f_temp:
            with open('all_files.txt', 'a', encoding='utf-8') as f:
                # Как это можно записать более компактно?
                f.write(key)
                f.write('\n')
                f.write(str(value))
                f.write('\n')
                f.write(f_temp.read())
                f.write('\n')


read_files_and_write_file('1.txt', '2.txt', '3.txt')
