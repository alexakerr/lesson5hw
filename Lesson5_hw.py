# Problem One

num1 = int(input("Please enter a number. "))
operation = input("Please choose an operation. + - * / ")
num2 = int(input("Please enter a second number. "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    if num2 == 0:
            print("Sorry, you can't divide by zero!")
    else:
            print(num1 / num2)
else:
    print("Please enter acceptable inputs.")



# Problem - Two
shopping_list = []
while True:
    shopping_list_item = input("Please add an item to your shopping list. Say 'quit' to quit: ")
    if shopping_list_item == "quit":
        break
    shopping_list.append(shopping_list_item)
    print(f"You have added {shopping_list_item} to your list.")

shopping_list_remove = input("If you would like to remove an item, please enter which item. If not, enter 'no': ")
if shopping_list_remove != "no":
    if shopping_list_remove in shopping_list:
        shopping_list.remove(shopping_list_remove)
        print(f"You have removed {shopping_list_remove} from your list.")
    else:
        print(f"{shopping_list_remove} is not in your list.")

print(f"Your shopping list: {shopping_list}")





# Problem Three
def analyze_grades(grades):
    total = 0
    highest_grade = grades[0]
    lowest_grade = grades[0]
    letter_grades = []
    for grade in grades:
        total += grade
        if grade > highest_grade:
            highest_grade = grade
        if grade < lowest_grade:
            lowest_grade = grade
 # *grades into letter grades*            
        if grade >= 90:
            letter_grades.append('A')
        elif grade >= 80:
            letter_grades.append('B')
        elif grade >= 70:
            letter_grades.append('C')
        elif grade >= 60:
            letter_grades.append('D')
        else:
            letter_grades.append('F')

    average_grade = total / len(grades)
    print("Average Grade:", average_grade)
    print("Highest Grade:", highest_grade)
    print("Lowest Grade:", lowest_grade)
    print("Letter Grades:", letter_grades)
grades = [85, 100, 95, 65, 72, 90, 60, 50]
analyze_grades(grades)
