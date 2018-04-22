import csv
import sys
import re
import datetime

def record(stuff):
    with open('journal.csv', 'a') as f:
        f.write(str(datetime.datetime.now())+','+stuff+'\n')

def multi_line():
    while True:
        multi_stuff = input('Type "Q" to quit. Otherwise, talk to me -> ').lower()
        if multi_stuff == 'q':
            break
        with open('journal.csv', 'a') as f:
            f.write(str(datetime.datetime.now())+','+multi_stuff+'\n')


def search():
    keyword = input('search term -> ').lower()
    regex = r"\b(?=\w)" + re.escape(keyword) + r"\b(?!\w)"
    with open('journal.csv', 'r') as csv:
        for line in csv:
            if re.search(regex, line):
                print(line)

if __name__ == '__main__':
    if sys.argv[1].lower() == '-s':
        search()
    elif sys.argv[1].lower() == '-m':
        multi_line()
    else:
        record(' '.join(sys.argv[1:]))
