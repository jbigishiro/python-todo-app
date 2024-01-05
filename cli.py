
# from functions import get_todos, write_todos
import time
import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, remove or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        """ new_todos = [item.strip('\n') for item in todos]"""

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[5:])
            num = num - 1
            new_todo = input("Enter a todo: ") + "\n"

            todos = functions.get_todos()

            todos[num] = new_todo

            functions.write_todos(todos)

        except ValueError:
            print('Your command is not valid')
            continue

    elif user_action.startswith("remove"):
        try:
            num = int(user_action[7:])

            todos = functions.get_todos()

            todo_to_remove = todos[num - 1].strip('\n')

            todos.pop(num - 1)

            functions.write_todos(todos)

            print(f"'{todo_to_remove}' was removed from the list")

        except IndexError:
            print('There is no item with that number')

            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('Wrong selection, try again')
print('Bye')
