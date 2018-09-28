# Assignment 2
#
# Number 1
# def last_name():
#     print("Enter name: ")
#     name = str(input())
#     #Splitting the name and replacing "-" with an empty space
#     words = name.replace('-',' ').split()
#     #Take the first alphabet from a word
#     sen = [word[0] for word in words]
#     print ("".join(sen).upper())
#
# last_name()
#
# Number 2
# list = []
# dict = {}
# count=0
# while count<10:
#     #For the user to enter exactly 10 numbers
#     num=int(input("Enter number: "))
#     #Adding the input numbers to the list
#     list.append(num)
#     count+=1
# for i in list: #For every number
#     #Calculating the remainder
#     mod=i%42
#     dict[mod]=0
#     # Remainders are in the dictionary
#
# print(len(dict.keys()))
#
# Number 3
#
# n = int(input("Enter number of stones: "))
# while n > 0:
#     #Alice takes 2 consecutive stones every turn
#     a = print("Alice takes 2 ")
#     stone = n - 2
#     if stone < 0:
#         print ("0 stones left")
#         break
#     if stone % 2 and stone > 0:
#         #if the stones are odd, Alice wins
#         print("\n""->""Alice")
#         print ("\n",stone, "stone(s) left")
#
#     else:
#         #if the stones are even, Bob wins
#         print("\n""->""Bob")
#         print("\n", stone, "stone(s) left")
#     if stone == 1:
#         print("\n" "->""Alice")
#         break
#     stone = stone - 2
#     #Bob takes 2 consecutive stones every turn
#     b = print("Bob takes 2 ")
#     if stone % 2 and stone != 0:
#         print ("\n""->""Alice")
#         print("\n",stone, "stone(s) left")
#
#     else:
#         print("\n""->""Bob")
#         print("\n",stone, "stone(s) left")
#
#     n = stone
#
#     continue
#
# Number 4
#
# x=input("Movement Pattern: ")
# list=['ball','empty','empty2']
# #The list contains the three cups. "ball" is the cup with the ball.
# a=list.index('ball')
# b=list.index('empty')
# c=list.index('empty2')
# for i in x:
#     if i =='A' or i == "a": #Switches left cup and middle cup (ball in left cup)
#         list[a],list[b]=list[b],list[a]
#     elif i =='B' or i == "b": #Switches middle cup and right cup
#         list[b],list[c]=list[c],list[b]
#     elif i == "C" or i == "c": #Switches left cup with right cup
#         list[a],list[c]=list[c],list[a]
#
# if list.index('ball')==0: #If the ball is on the left
#     print("1")
# elif list.index('ball')==1: #If the ball is in on the middle
#     print("2")
# else: # If the ball is on the right
#     print("3")
#
