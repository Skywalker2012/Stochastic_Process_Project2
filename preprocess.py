#!/usr/bin/env python
#By Skywalker 2014/1/22
import csv

f_in = open('train_set.csv','rb')
reader = csv.reader(f_in)
filename_pre = 'pre_train_set.csv'
f_out = open(filename_pre,'wb')
f_writer = csv.writer(f_out, dialect = 'excel')
for row in reader:
	f_writer.writerow(row[21:29] + row[30:35])
