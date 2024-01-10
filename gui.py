import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme('DarkBlue10')

clock = sg.Text(key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
remove_button = sg.Button('Remove')
exit_button = sg.Button('Exit')

window = sg.Window("My To-Do App",
                   layout=[[clock], [label], [input_box, add_button],
                           [list_box, edit_button, remove_button], [exit_button]],
                   font=('Helvetica', 12))
while True:
    event, values = window.read(timeout=500)
    window['clock'].update(value=time.strftime('%b %d %Y %H:%M:%S'))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            if values["todo"] == '':
                sg.popup("You cannot add an empty item", font=('Helvetica', 20))
            if values['todo'] in values['todos']:
                sg.popup("You cannot add an existing todo", font=('Helvetica', 20))
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Remove':
            try:
                todo_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=('Helvetica', 15))
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()
