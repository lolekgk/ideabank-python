# Put your code here
import os
import sys

def clear_terminal():
    os.system('cls' if os.name =='nt' else 'clear')


def add_ideas(ideas_list):
    new_ideas = []
    while True:
        try:
            idea = input("What is your new idea?\n")
            ideas_list.append(idea)
            new_ideas.append(idea)
            print_ideas(ideas_list)
        except KeyboardInterrupt:
            print("\r", end="")
            print("Closing...")
            return new_ideas


def save_to_file(filename, ideas_list, mode):
    with open(filename, mode) as f:
        for element in ideas_list:
            f.write(element + '\n')


def get_ideas_list_from_file(filename):
    ideas_list = []
    with open(filename) as f:
        list_from_file = f.readlines()
        for element in list_from_file:
            ideas_list.append(element.strip())
        return ideas_list


def print_ideas(ideas_list):
    clear_terminal()
    print("")
    for i in range(0, len(ideas_list)):
        print(i+1, end = "")
        print('.', ideas_list[i])
    print("")
        

def list_ideas(ideas_list):
    if sys.argv[1] == '--list':
        print("Saved ideas")

        print_ideas(ideas_list)


def check_for_command_line_arguments(ideas_list):
    if len(sys.argv) > 1:
        list_ideas(ideas_list)
        delete_idea(ideas_list)
        

def delete_idea(ideas_list):
    if sys.argv[1] == '--delete':
        if len(sys.argv) != 3 or not sys.argv[2].isnumeric():
            print_error_message("Specify a number after '--delete'.")
        else:
            del ideas_list[int(sys.argv[2]) - 1]
            save_to_file('ideas.txt', ideas_list, 'w')
            print_ideas(ideas_list)
   

def print_error_message(message):
    print("Error:", message)
    return None    


if __name__ == "__main__":
    old_ideas_list = get_ideas_list_from_file('ideas.txt')
    check_for_command_line_arguments(old_ideas_list)
    new_ideas_list = add_ideas(old_ideas_list)
    save_to_file('ideas.txt', new_ideas_list, 'a')
