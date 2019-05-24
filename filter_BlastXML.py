#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'shengwei ma'
__author_email__ = 'shengweima@icloud.com'

# output TOP N blast hits
# input is a blast result file in XML format
# out file is also in XML format

def filter_blastXML(a):
    # Filter hit according to <Hit_num>
    c = []
    for num, value in enumerate(a):
        if  '<Hit>' in value:
            start = num
        if '</Hit>' in value:
            end = num +1
            b = a[start:end]
            for i in b:
                if '<Hit_num>' in i:
                    n = int(i.split('>')[1].split('<')[0])
                    if n > 3 :   # retain top 3 hits
                        c.append((start, end))
    return c  


with open('test.xml','r') as f:
    a = []
    for line in f:
        a .append(line)
        if '</Iteration>' in line:
            new= filter_blastXML(a)
            for x in new[::-1]:
                del a[x[0]:x[1]]
            print(''.join(a), end='')
            a = []
    print('</BlastOutput_iterations>\n</BlastOutput>', end='')
