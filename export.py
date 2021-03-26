#!/bin/python3

import csv

def export_txt(row_list):
    to_txt = []
    to_txt.append(["1","2","3","4","5","6","7","8","9","10"])
    
    txt = open("NF.txt", "w")
    
    for row in row_list:
        for c in range(0,9):
            to_txt.append(row[c])
    print(to_txt)
    for row in to_txt:
        print(row)