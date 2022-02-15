import email
import os
import re


def task1():
    
    gen = os.walk('test')
    data = list()
    while True:
        try:
            data.append(gen.__next__())
        except StopIteration:
            break

    files = data[-1][2]
    count = 0
    for file in files:
        if re.fullmatch(r'filenames — копия \(\d\).txt', file):
            count += 1

    if 'filenames.txt' in files:
        count += 1

    print(f'Количество файлов filenames: {count}')

def task2():
    email_template = r'^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$'
    emails_list = list()

    for root, _, files in os.walk('test'):
        for filename in files:
            filepath = os.path.join(root, filename)
            with open(filepath, 'r') as source:
                for line in source.readlines():
                    if re.match(email_template, line.strip()) is not None:
                        emails_list.append(line.strip())


    print('Все электронные почты, найденные в файлах: ')
    for email in set(emails_list):
        print(email)


def main():
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()