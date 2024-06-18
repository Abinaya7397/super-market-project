import re
import datetime
import storeroom
import smtplib
f=open("thinks.txt" ,"r")
txt=f.read()
ur_word=input("enter a word :")
x=re.search(ur_word,txt)
print(x)
try:
    def main():
       user=int(input("view the row : "))
       if user == 1:
              storeroom.rice()
              con=input("do you want continue press yes/no : ")   
              if con=="yes":
                 print("go on next item search ")
                 main() 
       elif user==2:
            storeroom.biscuits()
            con=input("do you want continue press yes/no : ")   
            if con=="yes":
               print("go on next item search ")
            main()
       elif user == 3:
            storeroom.oil()
            con=input("do you want continue press yes/no : ")   
            if con=="yes":
                print("go on next item search ")
                main()
       elif user == 4:
                storeroom.shampoo()
                con=input("do you want continue press yes/no : ")   
                if con=="yes":
                 print("go on next item search ")
                main()
       elif user == 5:
                storeroom.soap()
                con=input("do you want continue press yes/no : ")   
                if con=="yes":
                 print("go on next item search ")
                main()
       elif user == 6:
                storeroom.fruits()
                con=input("do you want continue press yes/no : ")
                if con=="yes":
                 print("go on next item search ")
                main()
       elif user == 7:
                storeroom.vegetables()
                con=input("do you want continue press yes/no : ")
                if con=="yes":
                 print("go on next item search ")
                main()
       elif user == 8:
                storeroom.nuts()
                con=input("do you want continue press yes/no : ")
                if con=="yes":
                 print("go on next item search ")
                main()
       elif user == 9:
                storeroom.masala()
                con=input("do you want continue press yes/no : ")
                if con=="yes":
                 print("go on next item search ")
                main()
       elif user == 10:
                storeroom.juice() 
                con=input("do you want continue press yes/no : ")
                if con=="yes":
                 print("go on next item search ")
                 main()
                
except NameError:
    print(" this is name error")
except ValueError:
    print(" this is value error ")
except TypeError:
    print("this is type error")
except IndexError:
    print(" this index error")
 
x=datetime.datetime.now()
print(x)
receiver_mails="thila2978@gmail.com"
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("abinaya4959@gmail.com","")
f=open("billing.txt","r")
bill=f.read()
message=(f"your bill{bill}")
s.sendmail ("abin59853@gmail.com",receiver_mails,message)
s.quit()
print("mail send success")
main()


main()
    





