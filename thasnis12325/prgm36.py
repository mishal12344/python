class time:
    def __init__(self,h,m,s):
        self.__h1=h
        self.__m1=m
        self.__s1=s
    def __add__(self,x):
        sum1=self.__h1+x.__h1
        sum2=self.__m1+x.__m1
        sum2=self.__s1+x.__s1
        if sum3>=60:
            sum3=sum3-60
            sum2=sum2+1
        if sum2>=60:
            sum2=sum2-60
            sum1=sum1+1
        print(sum1,":",sum2,":",sum3);
print("TIME1")
h1=int(input("enter the hour in time1:"))
m1=int(input("enter the minute in time1:"))
s1=int(input("enter the second in time1:"))2
obj1=Time(h1,m1,s1)
print("TIME2")
h2=int(input("enter the hour in time2:"))
m2=int(input("enter the minute in time2:"))
s2=int(input("enter the second in time2:"))
obj1=Time(h2,m2,s2)
PRINT("the sum of the both time are:")
obj1+obj2