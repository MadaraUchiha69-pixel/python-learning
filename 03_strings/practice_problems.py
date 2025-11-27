# 1
a = input("Enter The Required User Name:  " )
print(a , "\nGood Morning") # also can be written as print(f"Good Morning, {a}")

#2
letter = '''Dear <|Name|>
            You Re selected!
            <|Date|>
            '''
b = input("Enter The Name You Required : ")
c = input("Enter The Date You are sending msg : ")
print(letter.replace("<|Name|>" ,b ).replace("<|Date|>" ,c ))# method 1

#d = letter.replace("<|Name|>" ,b ) method 2
#d = d.replace("<|Date|>" ,c )
#print(d)

# 3 
third = "Nothing Goes Planned  In this Cursed World"
print(third.find("  "))

# 4
third = "Nothing Goes Planned  In this Cursed World"
print(third.replace("  " , " "))

#5
fifth = "Dear Naruto ,\n \t My eyes are on you from childhood .\n You are the best "
print(fifth)