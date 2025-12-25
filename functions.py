FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
    Read a text file and return a list of todos items.
    """
    with open(filepath, "r") as file_local:  # this function automatically closes so no need to use file.close()
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write a list of todos items to a text file.
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":  # Executes only if file names 'main' is run
    print("Hello")
    print(get_todos())