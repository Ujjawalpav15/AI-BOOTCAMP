
# name=input("Enter the student's name: ")
# roll_no=input("Enter the roll number: ")
# x=int(input(f"Enter the marks of 1st subject : "))
# y=int(input(f"Enter the marks of 2nd subject : "))
# z=int(input(f"Enter the marks of 3rd subject : ")) 
# average=(x+y+z)/3
# print(f"Student Name: {name}")
# print(f"Roll Number: {roll_no}")    
# print(f"Average Marks: {average:.2f}")

# year=int(input("Enter year to check if it's leap year or not: "))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# number=int(input("Enter a number: "))
# if number%2==0 and number%3==0 and number%5==0:
#     print(f"{number} is superdivisible")
# elif number%2==0 and number%3==0:
#     print(f"{number} is divisible by 2 and 3")
# elif number%2==0 and number%5==0:
#     print(f"{number} is divisible by 2 and 5")
# elif number%3==0 and number%5==0:
#     print(f"{number} is divisible by 3 and 5")      
# elif number%2==0:
#     print(f"{number} is divisible by 2")
# elif number%3==0:
#     print(f"{number} is divisible by 3")    
# elif number%5==0:
#     print(f"{number} is divisible by 5")
          
# else:
#     print(f"{number} is not divisible by 2, 3 or 5")        

#WAP to print number from 1 to 50 the program should skip all numbers that are divisible by 5 using the continue statemnet

# for i in range(1,51):
#     if i%5==0:
#         continue
#     print(i)


#WAP that takes number continously from the user until the user enters 0, for each number entered display whether it is even or odd

# while True:
#     num=int(input("Enter a number:"))
#     if num==0:
#         break
#     elif num%2==0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd") 



# while True:
#     password=input("Enter your password:  ")
#     if password=="admin123":
#         print("Access Granted")
#         break

# while True:
#     a=int(input("Enter 1st numbers:  "))
#     b=int(input("Enter 2nd number:  "))
#     if a!=0 and b!=0:
#         if(a>b):
#             print(f"{b}")
#         else:
#             print(f"{a}")  
#     else:
#         break        


#WAP that keeps asking the users to enter anumber until 0 is entered print("Valid range" if 1-100 else "Out of Range")

# while True:
#     num=int(input("Enter a number: "))
#     if num==0:
#         break
#     elif 1<=num<=100:
#         print("Valid Range")
#     else:
#         print("Out of Range")

#WAP that prints all characters of a given string except vowels. Use a loop with the continue statement to skip vowels and print only constants


# text = input("Enter a string: ")

# # Loop through each character in the string
# for ch in text:
#     # Check if the character is a vowel
#     if ch in "aeiouAEIOU":
#         continue   # Skip vowels

#     # Print consonants
#     print(ch, end="")


#WAP that prints numbers from 1 to 20. For numbers divisibe by 3 , do nothing
#use the pass statement . For other numbers   print the number

# for i in range(1,21):
#     if i%3==0:
#         pass
#     else:
#         print(i, end=" ")


numbers=[1,2,3,4,5]
print(numbers[-1:])
print(numbers[::-1])
print(numbers[-2:])

