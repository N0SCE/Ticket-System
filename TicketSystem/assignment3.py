# Berkay Örene 2210356017
import os
import sys

current_dir_path = os.getcwd()
reading_file_name = sys.argv[1]
reading_file_path = os.path.join(current_dir_path, reading_file_name)
writing_file_name = "output.txt"
writing_file_path = os.path.join(current_dir_path, writing_file_name)

output = "" # it for holding all output. I will use it to write into output file


def reading_input_file():
    global number_of_lines
    number_of_lines = 0
    global number_of_create
    number_of_create = 0
    with open(reading_file_name, "r") as f:
        global data
        data = f.readlines()    
        for line in data:
            number_of_lines += 1
            if "CREATECATEGORY" in line:
                number_of_create += 1

reading_input_file()


command = ""
category_name = [] # all category names which they are created
row = [] # all row sizes
column = [] # all column sizes
category_list_3D = [] # it is the multi-dimensional list which I hold the category lists 

alphabet = ["A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ", "I ", "J ", "K ", "L ", "M ", "N ", "O ", "P ", "Q ", "R ", "S ", "T ", "U ", "V ", "W ", "X ", "Y ", "Z "]
def create_category(i):
    global output
    category_list = []
    command = data[i].split(" ")[0]
    if command == "CREATECATEGORY":
        current_category_name = data[i].split(" ")[1]
        if current_category_name not in category_name:
            category_name.append(data[i].split(" ")[1])
            row.append(int(data[i].split(" ")[2].split("x")[0]))
            column.append(int(data[i].split(" ")[2].split("x")[1]))
            index_of_category = category_name.index(current_category_name)
            
            number = int(row[i]) - 26 -1 # it is the index for adding letters from alphabet list to every row
            for x in range(row[i]):
                row_list = []               
                row_list.append(alphabet[number])
                number -= 1
                for y in range(column[i]):
                    row_list.append("X  ")

                category_list.append(row_list) 
            list = []
            for a in range(column[i]):
                if len(str(a)) == 1: # if it has one digit and not 9 i should make two whitespaces
                    if a == 9: # if it is 9 i should make one whitespace
                        list.append(str(a) + " ") 
                    else:
                        list.append(str(a) + "  ")
                elif len(str(a)) == 2:
                    list.append(str(a) + " ")
            list.insert(0, "  ") # there is a whitespace in the lower left corner
            category_list.append(list)
            category_list_3D.append(category_list)
            print(f"The category '{current_category_name}' having {row[i]*column[i]} seats has been created.")
            output = output + f"The category '{current_category_name}' having {row[i]*column[i]} seats has been created." + "\n"
        else:
            print(f"Warning: Cannot create the category for the second time. The stadium has already {current_category_name}.")
            output = output + f"Warning: Cannot create the category for the second time. The stadium has already {current_category_name}." + "\n"


def sell(i):
    global output
    command = data[i].split(" ")[0]
    if command == "SELLTICKET":
        name_of_person = data[i].split(" ")[1]
        kind_of_ticket = data[i].split(" ")[2]
        category_name_of_ticket = data[i].split(" ")[3]
        index_of_category = category_name.index(category_name_of_ticket)
        number_of_arguments = len(data[i].split(" ")) 
        ticket_of_place = data[i].split(" ")[4:]
    
        for x in ticket_of_place:
            current_number_of_student_tickets = 0
            current_number_of_full_tickets = 0
            current_number_of_season_tickets = 0
            if "-" in x:
                arbitrart_tickets = x.split("-")
                letter = arbitrart_tickets[0][0] # it is the letter of row                                
                number_of_first_arbitrary = arbitrart_tickets[0].split(letter)
                number_of_first_arbitrary.remove(number_of_first_arbitrary[0])
                number_of_first_arbitrary = int(number_of_first_arbitrary[0])
                number_of_last_arbitrary = int(arbitrart_tickets[1])
                if number_of_first_arbitrary <= column[index_of_category] and number_of_last_arbitrary <= column[index_of_category]:
                    letter = letter + " "
                    index_of_row = row[index_of_category] - alphabet.index(letter) -1
                    letter = letter[0] # removing the whitespace
                    counter_for_seats = 0
                    for number in range(number_of_first_arbitrary, number_of_last_arbitrary + 1):                        
                        index_of_column = number + 1
                       
                        if  "X" not in category_list_3D[index_of_category][index_of_row][index_of_column]: 
                            counter_for_seats += 1 # it is looking for if some of the seats have been sold
                    if counter_for_seats == 0: # if it is not equal to zero it means some of the seats have been sold 
                        for number in range(number_of_first_arbitrary, number_of_last_arbitrary + 1):                        
                            index_of_column = number + 1                                 
                            if kind_of_ticket == "student":
                                current_number_of_student_tickets += 1
                                category_list_3D[index_of_category][index_of_row][index_of_column] = "S  "
                            elif kind_of_ticket == "full":
                                current_number_of_full_tickets += 1
                                category_list_3D[index_of_category][index_of_row][index_of_column] = "F  "
                            elif kind_of_ticket == "season":
                                current_number_of_season_tickets += 1
                                category_list_3D[index_of_category][index_of_row][index_of_column] = "T  "
                        print(f"Success: {name_of_person} has bought {letter}{number_of_first_arbitrary}-{number_of_last_arbitrary} at {category_name_of_ticket}")
                        output = output + f"Success: {name_of_person} has bought {letter}{number_of_first_arbitrary}-{number_of_last_arbitrary} at {category_name_of_ticket}" + "\n"
                        number_of_student_tickets[index_of_category].append(current_number_of_student_tickets)
                        number_of_full_tickets[index_of_category].append(current_number_of_full_tickets)
                        number_of_season_tickets[index_of_category].append(current_number_of_season_tickets)
                    else:
                        print(f"Warning: The seats {letter}{number_of_first_arbitrary}-{number_of_last_arbitrary} cannot be sold to {name_of_person} due some of them have already been sold!")
                        output = output + f"Warning: The seats {letter}{number_of_first_arbitrary}-{number_of_last_arbitrary} cannot be sold to {name_of_person} due some of them have already been sold! "+ "\n"
                else:
                    print(f"Error: The category '{category_name_of_ticket}' has less column than the specified index {letter}{number_of_first_arbitrary}-{number_of_last_arbitrary}!")
                    output = output + f"Error: The category '{category_name_of_ticket}' has less column than the specified index {letter}{number_of_first_arbitrary}-{number_of_last_arbitrary}!" + "\n"

            else: 
                letter = x[0] + " "
                single_number = int(x[1:])
                if single_number <= column[index_of_category] and (alphabet.index(letter) + 1) <= row[index_of_category]:                                        
                    index_of_row = row[index_of_category] - alphabet.index(letter) -1
                    index_of_column = single_number + 1
                    letter = letter[0]
                    if  "X" in category_list_3D[index_of_category][index_of_row][index_of_column]:
                        if kind_of_ticket == "student":
                            number_of_student_tickets[index_of_category].append(1)
                            category_list_3D[index_of_category][index_of_row][index_of_column] = "S  "
                        elif kind_of_ticket == "full":
                            number_of_full_tickets[index_of_category].append(1)
                            category_list_3D[index_of_category][index_of_row][index_of_column] = "F  "
                        elif kind_of_ticket == "season":
                            number_of_season_tickets[index_of_category].append(1)
                            category_list_3D[index_of_category][index_of_row][index_of_column] = "T  "
                        print(f"Success: {name_of_person} has bought {letter}{single_number} at {category_name_of_ticket}")
                        output = output + f"Success: {name_of_person} has bought {letter}{single_number} at {category_name_of_ticket}" + "\n"
                    else:
                        print(f"Warning: The seat {single_number} cannot be sold to {name_of_person} since it was already sold!")
                        output = output + f"Warning: The seat {single_number} cannot be sold to {name_of_person} since it was already sold!" + "\n"
                else:
                    letter = letter[0]
                    if single_number <= column[index_of_category]:                        
                        print(f"Error: The category '{category_name_of_ticket}' has less column than the specified index {letter}{single_number}!")
                        output = output + f"Error: The category '{category_name_of_ticket}' has less column than the specified index {letter}{single_number}!" + "\n"
                    elif (alphabet.index(letter) + 1) <= row[index_of_category]:
                        print(f"Error: The category '{category_name_of_ticket}' has less row than the specified index {letter}{single_number}!")
                        output = output + f"Error: The category '{category_name_of_ticket}' has less row than the specified index {letter}{single_number}!" + "\n"


def cancel(i):
    global output
    command = data[i].split(" ")[0]
    if command == "CANCELTICKET":
        name_of_category = data[i].split(" ")[1]
        ticket_of_place = data[i].split(" ")[2:]
        index_of_category = category_name.index(name_of_category)
        for x in ticket_of_place:
            letter = x[0] + " "
            number = int(x[1:])
            if number <= column[index_of_category] and (alphabet.index(letter) + 1) <= row[index_of_category]:
                index_of_row = row[index_of_category] - alphabet.index(letter) -1
                index_of_column = number + 1
                letter = letter[0]
                if "X" not in category_list_3D[index_of_category][index_of_row][index_of_column]: # if X is not in the seat it means the seat has been sold and you cancel it
                    if "S" in category_list_3D[index_of_category][index_of_row][index_of_column]:
                        number_of_student_tickets[index_of_category].append(-1)
                        category_list_3D[index_of_category][index_of_row][index_of_column] = "X  "
                    elif "F" in category_list_3D[index_of_category][index_of_row][index_of_column]:
                        number_of_full_tickets[index_of_category].append(-1)
                        category_list_3D[index_of_category][index_of_row][index_of_column] = "X  "                 
                    elif  "T" in category_list_3D[index_of_category][index_of_row][index_of_column]:                      
                        number_of_season_tickets[index_of_category].append(-1)
                        category_list_3D[index_of_category][index_of_row][index_of_column] = "X  "
                        
                    print(f"Success: The seat {letter}{number} at {name_of_category} has been canceled and now ready to sell again.")
                    output = output + f"Success: The seat {letter}{number} at {name_of_category} has been canceled and now ready to sell again." + "\n"
                else:
                    print(f"Error: The seat {letter}{number} at {name_of_category} has already been free! Nothing to cancel.")
                    output = output + f"Error: The seat {letter}{number} at {name_of_category} has already been free! Nothing to cancel." + "\n"
            else:
                if number <= column[index_of_category]:
                    letter = letter[0]
                    print(f"Error: The category '{name_of_category}' has less column than the specified index {letter}{number}")
                    output = output + f"Error: The category '{name_of_category}' has less column than the specified index {letter}{number}" + "\n"
                elif (alphabet.index(letter) + 1) <= row[index_of_category]:
                    letter = letter[0]
                    print(f"Error: The category '{name_of_category}' has less row than the specified index {letter}{number}")
                    output = output + f"Error: The category '{name_of_category}' has less row than the specified index {letter}{number}" + "\n"


def balance(i):
    global output
    command = data[i].split(" ")[0]
    if command == "BALANCE":
        name_of_category = data[i].split(" ")[1]
        
        if name_of_category in category_name or name_of_category[:-1] in category_name:
            if name_of_category in category_name: # This part for preventing a error. There can be error if name of category has \n at the end
                index_of_category = category_name.index(name_of_category)
            elif name_of_category[:-1] in category_name:
                name_of_category = name_of_category[:-1]
                index_of_category = category_name.index(name_of_category)
            global number_of_student_tickets
            sum_of_students = 0
            for element in number_of_student_tickets[index_of_category]:
                sum_of_students = sum_of_students + element # it finds out sum of students tickets 

            global number_of_full_tickets
            sum_of_full_pay = 0
            for element in number_of_full_tickets[index_of_category]:
                sum_of_full_pay = sum_of_full_pay + element

            global number_of_season_tickets
            sum_of_season_tickets = 0
            for element in number_of_season_tickets[index_of_category]:
                sum_of_season_tickets = sum_of_season_tickets + element

            print(f"Category report of '{name_of_category}'")
            print("-"*(len(name_of_category)+21))
            print(f"Sum of students = {sum_of_students}, Sum of full pay = {sum_of_full_pay}, Sum of season tickets = {sum_of_season_tickets}, and Revenues = {(sum_of_students*10) + (sum_of_full_pay*20) + (sum_of_season_tickets*250)} Dollars")
            output = output + f"Category report of '{name_of_category}'" + "\n"
            output = output + "-"*(len(name_of_category)+21) + "\n"
            output = output + f"Sum of students = {sum_of_students}, Sum of full pay = {sum_of_full_pay}, Sum of season tickets = {sum_of_season_tickets}, and Revenues = {(sum_of_students*10) + (sum_of_full_pay*20) + (sum_of_season_tickets*250)} Dollars" + "\n"
        else:
            print(f"ERROR: There is no category named {name_of_category}")
            output = output + f"ERROR: There is no category named {name_of_category}"


def show(i):
    global output
    command = data[i].split(" ")[0]
    if command == "SHOWCATEGORY":
        name_of_category = data[i].split(" ")[1] 
        if name_of_category in category_name or name_of_category[:-1] in category_name:
            if name_of_category in category_name: # This part for preventing a error. There can be error if name of category has \n at the end
                index_of_category = category_name.index(name_of_category)
            elif name_of_category[:-1] in category_name:
                name_of_category = name_of_category[:-1]
                index_of_category = category_name.index(name_of_category)

            print(f"Printing category layout of {name_of_category}")
            output = output + f"Printing category layout of {name_of_category}" + "\n"

            for row in category_list_3D[index_of_category][:-1]:          
                counter = 0
                for element in row:  
                    counter += 1                  
                
                    if counter == (column[index_of_category] + 1): # it means you are at the end of the row and you should go to a new line
                        print(element, end="\n")                    
                        output = output + element + "\n"
                    else:
                        print(element, end="")
                        output = output + element

            for row in category_list_3D[index_of_category][-1:]: # it prints the numbers 
                    for number in row:
                        print(number, end="")
                        output = output + number
            output = output + "\n"
            print("\n")
        else:
            print(f"ERROR: There is no category named {name_of_category}")
            output = output + f"ERROR: There is no category named {name_of_category}"


def write():
    with open(writing_file_path, "w") as f:       
        f.write(output)


for i in range(number_of_lines):
    if data[i].split(" ")[0] == "CREATECATEGORY":
        create_category(i)

        # This is for finding out how many tickets there are 
        number_of_student_tickets = []
        for x in range(len(category_name)):
            number_of_student_tickets.append([])

        number_of_full_tickets = [] 
        for x in range(len(category_name)):
            number_of_full_tickets.append([])

        number_of_season_tickets = [] 
        for x in range(len(category_name)):
            number_of_season_tickets.append([])

    elif data[i].split(" ")[0] == "SELLTICKET":
        sell(i)
    elif data[i].split(" ")[0] == "CANCELTICKET":
        cancel(i)
    elif data[i].split(" ")[0] == "BALANCE":
        balance(i)
    elif data[i].split(" ")[0] == "SHOWCATEGORY":
        show(i)
write()
