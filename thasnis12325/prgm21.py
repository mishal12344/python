nterms=int(input("Enter the number"))
n1,n2=0,1
count=0
print("fibonacci SERIES:")
while count<nterms:
    print(n1)
    nth=n1+n2

    n1=n2
    n2=nth
    count+=1