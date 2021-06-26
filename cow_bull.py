import random

def list_Of_Number(listofnum):
    i=1
    list1=set()
    while True:
        if i>0:
            value=(random.choice(listofnum))
            list1.add(value)
        if len(list1)==5:
            break
#         i=i+1
    return(list1)
numbers=[0,1,2,3,4,5,6,7,8,9]
num=list_Of_Number(numbers)
secretNumlist=list(num)



def findindex(a):
    indexofnum = secretNumlist.index(a)
    return(indexofnum)

name_of_player=input("Enter Player Name:----")
print("WELCOME",name_of_player,"To this Game")
print("Our number list is:----",secretNumlist)
list2=[]
list3=[]
i=0
chances=10
while i<10:
    number=int(input("enter number ="))
    position=int(input("enter position ="))
    
    if number not in secretNumlist:
        print("Number not exists")
    elif number in secretNumlist:
        indexofnum=findindex(number)
        
        if number in secretNumlist and position==indexofnum:
            print("Bull")
            list2.insert(indexofnum,number) 
    if number in secretNumlist and position!=indexofnum:
        print("Cow")
        list3.append(number)
        print("These are correct numbers you can reuse it",list3)
   
    i=i+1
    chances=chances-1
    print("chances :---",chances)

    
if list2==secretNumlist:
        print("Congratulation ",name_of_player, "You are the winner!!!!!")
else :
    print("Opps You are the looser")
print("orignal:----",secretNumlist)
print("user gave:---",list2) 
print("correct number but wrong position;---",list3)
