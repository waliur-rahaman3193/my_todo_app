def get_todos(filepath = 'todos.txt'):
    """Read text file and return the to do items"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath = 'todos.txt'):
    """write and update the to do items in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
