#author: Shahed Mohammad Hridoy
from math import sqrt
while True:
      print("Options:")
      print("Enter 'add' to add two numbers")
      print("Enter 'subtract' to subtract two numbers")
      print("Enter 'multiply' to multiply two numbers")
      print("Enter 'divide' to divide two numbers")
      print("Enter 'sqrt' to square root a number")
      print("Enter 'quit' to end the program")
      

      user_input = input(": ")
      
      if user_input =="quit":
            break
      elif  user_input =="add":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(a+b)
      elif  user_input =="subtract":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(a-b)
      elif  user_input =="multiply":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(a*b)
      elif  user_input =="divide":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(a/b)
      elif user_input == "sqrt":
            a = float(input("Enter a number to root"))
            print(sqrt(a))
      else:
            print ("invalid Input")
