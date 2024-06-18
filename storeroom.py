print("***seven*supermarker***")
print("welcome")
print(f"row 1 :rice items\nrow 2:biscuits\nrow 3:oil\nrow4 :shampoo\nrow 5:soap\nrow 6:fruits\nrow 7 :vegetables\nrow 8 :nuts\nrow 9:masala\nrow 10:juices")
print("what do you want")
def rice():
    print("rice is avaliable ")
    print("basmathi,white rice,brown rice")
    brand=input("enter brande name : ")
    one_kg=50
    how_many=int(input("enter your kg : "))
    rc=one_kg*how_many
    print(f"rice brand name is {brand}\none kg of rice is {one_kg}\n total price of rice is {rc}")
    f=open("billing.txt","a")
    f.write(f"total rice is {rc}")
    print("bill success")    
def biscuits ():
    print("biscuits is avaliable ")
    print("oreao,marigold,cream biscuits")
    brand=input("biscuit brand :")
    one_packet=30
    how_many=int(input("how many biscuits packet : "))
    bc=one_packet*how_many
    print(f"biscuit brande is {brand}\none packet  of biscuits is {one_packet} \n total price of biscits is {bc}")
    f=open("billing.txt","a")
    f.write(f"total price of biscuits is {bc}")
    print("bill success")
def oil ():
    print("oil is avaliable ")
    brand=input("oil brand name  :")
    one_lit=150
    how_many=int(input("how many litters : "))
    oi=one_lit*how_many
    print(f"oil brand name is {brand}\none litter of oil is {one_lit} \n total price of oil is {oi}")
    f=open("billing.txt","a")
    f.write(f"total price of oil is {oi}")
    print("bill success")
def shampoo ():
    print("shampoo is avaliable ")
    print("dove,all clear,karthika")
    brand=input("shampoo brand name  :")
    one_sham=5
    how_many=int(input("how many backet : "))
    sp=one_sham*how_many
    print(f"shampoo brand name is {brand}\none backet of shampoo is {one_sham}\n total price of shampoo is {sp}")
    f=open("billing.txt","a")
    f.write(f"total price of shampoo is {sp}")
    print("bill success")
def soap ():
    print("soap is avaliable ")
    print("lux,cinthal")
    brand=input("soap brand name  :")
    one_soap=45
    how_many=int(input("how many backet : "))
    so=one_soap*how_many
    print(f"soap brand name is {brand}\none  of shampoo is {one_soap}\n total price of soap is {so}")
    f=open("billing.txt","a")
    f.write(f"total price of soap is {so}")
    print("bill success")
def fruits ():
    print("fruits is avaliable ")
    print('apple,orenge,grapes')
    brand=input(" type of fruit  name  :")
    one_kg_fruit=45
    how_many=int(input("how many kg : "))
    frut=one_kg_fruit*how_many
    print(f"type of fruit name is {brand}\none  kg of fruits is {one_kg_fruit}\n total price of fruits is {frut}")
    f=open("billing.txt","a")
    f.write(f"total price of fruits is {frut}")
    print("bill success")
def vegetables ():
    print("vegetables  is avaliable ")
    print('onion,geek,potato')
    brand=input(" type of vegetable name  :")
    one_kg_vege=30
    how_many=int(input("how many kg : "))
    veg=one_kg_vege*how_many
    print(f"type of vegetable name is {brand}\none  kg of vegetable is {one_kg_vege}\n total price of vegetables is {veg}")
    f=open("billing.txt","a")
    f.write(f"total price of vegetables is {veg}")
    print("bill success")
def nuts ():
    print("nuts is avaliable ")
    print('almonds,pili nuts,butternuts')
    brand=input(" type of nuts name  :")
    one_kg_nuts=135
    how_many=int(input("how many kg : "))
    nut=one_kg_nuts*how_many
    print(f"type of nuts name is {brand}\none kg of nuts is {one_kg_nuts}\ntotal price of nuts is {nut}")
    f=open("billing.txt","a")
    f.write(f"total price of nut is {nut}")
    print("bill success")
def masala ():
    print("masala is avaliable ")
    print('chiken masala,mutton masala,fish masala')
    brand=input(" type of masala name  :")
    one_masala=45
    how_many=int(input("how many kg : "))
    sal=one_masala*how_many
    print(f"type of masala name is {brand}\none  kg of masala is {one_masala}\n total price of masala is {sal}")
    f=open("billing.txt","a")
    f.write(f"total price of masala is{sal}")
    print("bill success")
def juice ():
    print("juice is avaliable ")
    print("lemon juice,apple juice,carrot joice")
    brand=input(" type of juice name  :")
    one_juice=20
    how_many=int(input("how many juice : "))
    jus=one_juice*how_many
    print(f"type of juice name is {brand}\none juice is {one_juice}\n total price of juice is {jus}")
    f=open("billing.txt","a")
    f.write(f"total price of juices is{jus}")
    print("bill success")
    

 