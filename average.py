numbers = input("Enter numbers separated by spaces: ")
number_list = [float(n) for n in numbers.split()]
average = sum(number_list) / len(number_list)
print(f"The average is: {average}")