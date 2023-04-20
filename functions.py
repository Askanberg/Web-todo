FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Reads a text-file and returns the contents
    in the list of to-dos.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """
    Writes/alter the contents in the list of to-dos
    in the text file.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_local)



