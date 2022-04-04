#was to enter 5 string in a list and check and print  those string whose length has even number without any string function:
#note:To do this script using UDF...
l=[]
count=0
def least():
    for i in range(5):
        s=input("Enter string:")
        l.append(s)
least()
def strlen(l):
    for i in l:
        count=0
        for j in i:
            count=count+1
        if(count%2==0):
                print("IN the list evennumber string is {} and string length is {}".format(i,count))   
s=strlen(l)




