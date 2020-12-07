###THIS IS A PROJECT TO DELIVER YOU YOUR DAILY TASKS IN A VERY FRIENDLY WAY, YOU CAN ADD OR REMOVE EVERYDAY TASKS EASILY
from file import File, Answer
from datetime import datetime
import json
from tasks import*

def main():
    while True:
        print("Welcome to our task manager, here you can add, remove and save your tasks")
        x = input("Would you like to create a new task ")
        a = Answer(x)
        main_file = File('tasklistfile.json')
        file_dict = main_file.readFile()
        tasklist1 = TaskList()
        for task_i in file_dict:
            for key in task_i:

                task_obj = Task(task_i[key], datetime.strptime(key, "%Y-%m-%d %H:%M:%S"))
                tasklist1.addatask(task_obj)     

        i = tasklist.llist.head
        #while True:
        #    if i:
        #        print(i.value)
        #        i = i.next
        #    else:
        #        break




        #print(file_dict)

        if a.answer_is_yes():
            print("Ok, now you can add a task")
            taskname = input("Enter your task name ")
            taskdate = str(datetime(int(input('year ')), int(input('month ')), int(input('date '))))
            new_task = {taskdate: taskname}
            file_dict.append(new_task)
            main_file.writeFile(file_dict)

        if a.answer_is_no():
            print("Here you can read your tasks")
            print("Here you can see your top five upcoming tasks")
            for i in file_dict:
                if not tasklist1.Queuelist.isFull():
                    tasklist1.Queuelist.append(i)
            do_the_latest = input("Do you want to complete the latest task? ")
            do_the_latest_answer = Answer(do_the_latest)
            if do_the_latest_answer.answer_is_yes():
                tasklist1.Queuelist.pop()

        if a.answer_is_exit():
            return





main()
