# #1.	Write a Python program to create a text file named data.txt and write the following information into it:
# # •	Student Name
# # •	Roll Number
# # •	Course Name
# def create_student_file():
#     with open("data.txt", "w") as file:
#         file.write(f"Student Name: Ujjawal Patel\n")
#         file.write(f"Roll Number: 44\n")
#         file.write(f"Course Name: Electronics\n")
#         print("Data written to data.txt successfully.")

# create_student_file()       
 
# #2.	Write a Python program to read the contents of a text file and display them on the screen.

# with open("data.txt", "r") as file:
#     content = file.read()
#     print("\nContents of data.txt:")
#     print(content)

# # 3.Write a Python program to append a new line of text to an existing file without overwriting the previous content.    

# with open("data.txt", "a") as file:
#     file.write(f"Gender: Male")

# print("Data Appended Sucessfully")    

# # 4.	Write a Python program to count and display:
# # a.	Number of lines
# # b.	Number of words
# # c.	Number of characters in a given text file.

# line_count = 0
# word_count = 0
# char_count = 0
# with open("data.txt", "r") as file:
#     for line in file:   
#         line_count += 1

#         words = line.split()
#         word_count += len(words)
#         char_count += len(line)

# print(f"Number of lines: {line_count}")    
# print(f"Number of words: {word_count}")    
# print(f"Number of characters: {char_count}")
        
# 5.	Write a Python program to search for a word entered by the user in a text file and display whether it is found or not.
# search_word = input("Enter a word to search: ")
# found = False
# with open("data.txt", "r") as file:
#     for line in file:
#         if search_word in line:
#             found = True
#             break

# if found:
#     print(f"The word '{search_word}' is found in the file.")
# else:
#     print(f"The word '{search_word}' is not found in the file.")


# 6.	Write a Python program to create a CSV file named employees.csv 
# and store the following details as Employee ID, Employee Name, Department, Salary. Further, 
# add a new employee, display all employees, search a employee by name.

# import csv
# def create_employee_file():
#     with open("employees.csv", "w", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Employee ID", "Employee Name", "Department", "Salary"])
#         writer.writerow([1, "Ujjawal", "BEI", 50000])
#         writer.writerow([2, "Yugal", "IT", 60000])
#         writer.writerow([3, "Kiran", "Finance", 55000])
#     print("employees.csv created successfully.")
# create_employee_file()
# def add_employee(emp_id, emp_name, department, salary):
#     with open("employees.csv", "a", newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([emp_id, emp_name, department, salary])
#     print(f"Employee {emp_name} added successfully.")
# add_employee(4, "Ashish", "IT", 62000)
# def display_employees():
#     with open("employees.csv", "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(row)
# print("\nList of Employees:")
# display_employees()
# def search_employee_by_name(name):
#     found = False
#     with open("employees.csv", "r") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             if row[1] == name:
#                 print(f"Employee found: {row}")
#                 found = True
#                 break
#     if not found:
#         print(f"Employee with name '{name}' not found.")
# search_name = "Ashish"
# print(f"\nSearching for employee with name: {search_name}")
# search_employee_by_name(search_name)

# 7.	Imagine you have a CSV file with three columns: Product, Price, Quantity.
# 1. Create this file using the csv.writer.
# 2. Read the file back. For each row, calculate the "Total Value" (Price * Quantity).
# 3. Print a summary: "Product [Name] has a total stock value of [Total Value]".

import csv
def create_product_file():
    with open("products.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Product", "Price", "Quantity"])
        writer.writerow(["Laptop", 800, 5])
        writer.writerow(["Smartphone", 500, 10])
        writer.writerow(["Tablet", 300, 7])
    print("products.csv created successfully.")
create_product_file()
def calculate_total_value():
    with open("products.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            total_value = price * quantity
            print(f"Product {product} has a total stock value of {total_value}.")
calculate_total_value()









