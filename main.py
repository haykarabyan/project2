###THIS IS A PROJECT TO DELIVER YOU YOUR DAILY TASKS IN A VERY FRIENDLY WAY, YOU CAN ADD OR REMOVE EVERYDAY TASKS EASILY
from file import File, Answer
from datetime import datetime

def main():
    print("Welcome to our task manager, here you can add, remove and save your tasks")
    x = input("Would you like to create a new task ")
    a = Answer(x)
    main_file = File('tasklistfile.json')



    if a.answer_is_yes():
        print("Ok, now you can add a task")
        taskname = input("Enter your task name ")
        taskdate = datetime(int(input('year ')),int(input('month ')), int(input('date ')))
        new_task = {taskname:taskdate}

        d = main_file.writeFile(new_task)
    else:
        print("Here you can read your tasks")
        print("Here you can see your top five upcoming tasks")


main()
