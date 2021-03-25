#!/bin/python3

import csv

def export_csv(row_list):
    to_csv = []
    to_csv.append(["1","2","3","4","5","6","7","8","9","10"])
    
    
        
    with open('NF.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        #writer.writerows(to_csv)
    
        for row in row_list:
            to_csv.append(row)
            
            for c in range(0,9):
                print([row[c]])
                writer.writerow([row[c]])
                
