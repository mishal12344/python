import csv
with open("csv3.csv",newline="")as csvfile:
    d=csv.DictReader(csvfile)
    print("ROLLNO STUDENTNAME")
    print("___________")
    for i in d:
       print(i['ROLLNO'],i['STUDENTNAME'])

