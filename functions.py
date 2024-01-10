def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list
    of the to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filename="todos.txt", ):
    """ Write the to-do items list in the text file."""
    with open(filename, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from the functions")
    print(get_todos())
