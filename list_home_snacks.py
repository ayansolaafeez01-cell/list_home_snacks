
import random
random_numbers = []


for number in range (10):
	random_numbers.append(random.randint(1,50))
	
print(random_numbers)


def get_list_length(list):
	count = 0
	for content in list:
		count = count + 1
	return count
	
	
print(get_list_length([19, 9, 47, 3, 13, 27, 13, 44, 25, 47]))


def sum_even_index_in_list(list):
	count = 0
	for number in range(len(list)):
		if number % 2 == 0 and number != 0:
			count = count + list[number]
	return count


	
print(sum_even_index_in_list([19, 9, 47, 3, 13, 27, 13, 44, 28, 47]))


def sum_odd_index_in_list(list):
	count = 0
	for number in range(len(list)):
		if number % 2 == 1 and number != 0:
			count = count + list[number]
	return count

	
print(sum_odd_index_in_list([19, 9, 47, 3, 13, 27, 13, 44, 28, 47]))


def multiply_from_third_position(list):
	product = 1
	for content in list[2:len(list):3]:
		product = product * content
	return product
	
print(multiply_from_third_position([1,2,3,4,5,6,7,8,9,10]))



def average_of_list_elememts(list):
	sum_of_elements = 0
	for content in list:
		sum_of_elements = sum_of_elements + content
	average = sum_of_elements / len(list)
	return average
	
print(average_of_list_elememts([1,2,3,4,5,6,7,8,9,10]))


def largest_element_in_list(list):

	largest = list[0]
	
	for number in list:
		if number > largest:
			largest = number
	return largest

	
print(largest_element_in_list([1,2,3,4,5,6,7,8,9,10]))
def smallest_element_in_list(list):




	smallest = list[0]
	
	for number in list:
		if number < smallest:
			smallest  = number
	return smallest
	
print(smallest_element_in_list([1,2,3,4,5,6,7,8,9,10]))	




def list_of_strings(strings):
    count = 0

    for strings in strings:
        if len(strings) >= 2 and strings[0] == strings[-1]:
            count += 1

    return count


strings = ['abc', 'xyz', 'aba', '1221', 'aa']

print(list_of_strings(strings))


def sequential_list_from_1_to_15():
	sequential_list = []
	for numbers in range(1,16):
		sequential_list.append(numbers)
	return sequential_list
	
print (sequential_list_from_1_to_15())


def add_third_in_list(list):
	sum_of_numbers = 0
	for numbers in list[2: :3]:
		sum_of_numbers = sum_of_numbers + numbers 
	return sum_of_numbers	
		
print(add_third_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))



def sum_of_first_middle_last_number(list):
	first_index = list[0]
	last_index = list[-1]
	middle = len(list) // 2
	
	if len(list) % 2 == 0:
		middle_index = (list[middle - 1] + list[middle])/2
	else:
		middle_index = list[middle]
		
	return first_index + middle_index + last_index
	
print(sum_of_first_middle_last_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(sum_of_first_middle_last_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
