import random

random_list = random.sample(range(0, 1000), 100)  # create the list of 100 random numbers from range 0, 1000

for i in range(len(random_list)):  # iterate through len of random_list
    for j in range(i+1, len(random_list)):  # iterate through random_list starting from second element
        if random_list[i] > random_list[j]:  # compare elements
            random_list[i], random_list[j] = random_list[j], random_list[i]  # if i>j then swap these two elements

odd_numbers = []  # create empty list for odd numbers
even_numbers = []  # create empty list for even numbers

for i in random_list:  # iterate through random_list
    if i % 2 == 0:  # find even numbers
        even_numbers.append(i)  # if it is even number then add it to the even_numbers list
    else:
        odd_numbers.append(i)  # else it is odd number and add it to the odd_numbers list

sum_odd_numbers = 0  # create variable to calculate sum of odd numbers
for odd in odd_numbers:  # iterate through list of odd_numbers
    sum_odd_numbers += odd  # add each number of odd_number list to the sum_odd_numbers variable
try:
    odd_average = sum_odd_numbers / len(odd_numbers)  # calculate average of odd numbers
    print(f"The average for odd numbers is {odd_average:.2f}")  # print the result to console
except ZeroDivisionError:  # if the odd_numbers list is empty then the error is thrown
    print("Division by zero")


sum_even_numbers = 0  # create variable to calculate sum of even number
for even in even_numbers:  # iterate through list of even_numbers
    sum_even_numbers += even  # add each number of even_number list to the sum_even_numbers variable
try:
    even_average = sum_even_numbers/len(even_numbers)  # calculate average of add numbers
    print(f"The average for odd numbers is {even_average:.2f}")  # print the result to console
except ZeroDivisionError:  # if the even_numbers list is empty then the error is thrown
    print("Division by zero")
