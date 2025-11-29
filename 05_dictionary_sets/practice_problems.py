#1 
dcito = {"Aloo" : "Potatao" , "Kela" : "Banana" ,"Sona" : "Sleep" , "chumi" : "kissy" }
words = input("Enter the word to get meaning :")
print(dcito[words])

# 2
N1 = int(input("Enter the desired Number : "))
N2 = int(input("Enter the desired Number : "))
N3 = int(input("Enter the desired Number : "))
N4 = int(input("Enter the desired Number : "))
N5 = int(input("Enter the desired Number : "))
N6 = int(input("Enter the desired Number : "))
N7 = int(input("Enter the desired Number : "))
N8 = int(input("Enter the desired Number : "))
set1 = {N1 , N2 , N3 , N4 , N5 , N6 , N7 , N8}
print(set1)

#3
set2 = { 18 , "18"} 
print(set2)

#4
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

#5
s1 ={}
print(type(s1))

#6
lang_dict = {}
F1 = input("Enter Your  Name: ")
F2 = input("Enter Your  Name: ")
F3 = input("Enter Your  Name: ")
F4 = input("Enter Your  Name: ")
L1 = input("Enter Your Favourite Language Name: ")
L2 = input("Enter Your Favourite Language Name: ")
L3 = input("Enter Your Favourite Language Name: ")
L4 = input("Enter Your Favourite Language Name: ")
lang_dict.update({F1 : L1 , F2 : L2 , F3 : L3 , F4 : L4})
print(lang_dict)

