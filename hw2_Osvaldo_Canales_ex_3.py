'''
Homework 2, Excercise 3
Osvaldo Canales
February 14, 2023
Create a list and modify it  
'''

#Create a list and print using a single line of code 
pocketGoods = ['Wallet','Phone','Keys']
print(pocketGoods)

#Sort the list then print again
pocketGoods.sort()
print(pocketGoods)

#Print the first item in the list
print(pocketGoods[0])

#Print everything besides the first item in the list
print(pocketGoods[1:3])

#Print the last item in the list using negative index
print(pocketGoods[-1])

#Print the index of 'Keys' using index()
print(pocketGoods.index('Keys'))

#Append 'Tablet' to the list, then print the list
pocketGoods.append('Tablet')
print(pocketGoods)

#Insert 'Mask' to the list as the second item in the list, then print the list
pocketGoods.insert(1,'Mask')
print(pocketGoods)

#Remove 'Phone' from the list, then print the list
pocketGoods.remove('Phone')
print(pocketGoods)

#Reverse the list, then print the list
pocketGoods.reverse()
print(pocketGoods)

#11
def strList(list):
    list.insert(-1,'and')
    for index, item in enumerate(list):
        print(item, end = ", ")

strList(pocketGoods)