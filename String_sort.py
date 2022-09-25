import sys
import time
import os

def to_array(string_input):
    """Convert user input to the list"""
    array = []
    for letter in string:
        to_number = ord(letter)
        if 32 < to_number < 127:
            array.append(letter)
    return array

def sort_string(list_of_char):
    """"Use the Quicksort to sort the list in ascending order"""
    less, equle, greater = [], [], []

    if len(list_of_char) > 1:
        pivot = list_of_char[0]
        for item in list_of_char:
            if item < pivot:
                less.append(item)
            elif item > pivot:
                greater.append(item)
            else:
                equle.append(item)
        return sort_string(less) + equle + sort_string(greater)
    else:
        return list_of_char

def write_to_file(file_sorted):
    """Create, if not exists, and write to file"""
    with open("String_Sorted.txt", "w") as file:
        file.write(file_sorted)

if __name__ == "__main__":

    print("Please choose the input type.\nFor file (F) for string (S)")
    choice = input("(F/S?)")

    if choice.upper() == "F":
        #Get the file path
        file = input("file=")
        path = os.path.join(file)
        start_time = time.time()
        # Open file in read mode
        with open(path,'r', encoding='utf-8') as file:
            string = file.read().replace("\n",'')

        start_f__time = time.time()
        #Convert file content to list
        array = to_array(string)
        #Sort list using Quicksort algorthm
        sorted_string = sort_string(array)
        end_f_time = time.time()
        #Convert list to string
        to_string = "".join(map(str,sorted_string))
        #Write result to the file 
        write_to_file(to_string)
        #Timing
        file_access_time = start_f__time - start_time
        sort_time = end_f_time - start_f__time
        #Get file size
        file_size = os.path.getsize("String_Sorted.txt")
        #Print results to the comman prompt
        print(f"File access time: {file_access_time} miliseconds.")
        print(f"Sorting time: {sort_time} miliseconds.")
        print(f"File size: {file_size} bytes.")

    elif choice.upper() == "S":
        #Get user input
        string = input("Enter the string: ")
        start_s_time = time.time()
        # COnvert user input to the list
        array = to_array(string)
        #Sort list using Quicksort algorthm
        sorted_string = sort_string(array)
        strig_e_time = time.time()
        #Convert list to string
        to_string = "".join(map(str,sorted_string))
        #Print results to the comman prompt
        print(to_string)
        print("Sorting time: ", (strig_e_time - start_s_time)," miliseconds")

