import functions
import time



while True:
    user_input = input("type add, show, edit, complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todo = user_input[4:] + '\n'

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_input.startswith("show"):

        todos = functions.get_todos()

        for index, x in enumerate(todos):
            x = x.strip('\n')
            print(f"{index + 1}: {x}")

    elif user_input.startswith("edit"):
        number = int(input("Number of to do to edit? ")) - 1

        todos = functions.get_todos()

        todos[number] = input("What do you want to replace it with? ") + '\n'

        functions.write_todos(todos)

    elif user_input.startswith('exit'):
        break

    elif user_input.startswith('complete'):
        number = int(input("Number of to do to complete? ")) - 1

        todos = functions.get_todos()

        removed_todo = todos[number].strip('\n')
        print(f'"{removed_todo}" to do item is marked complete.')
        todos.pop(number)

        functions.write_todos(todos)

    else:
        print("Please give the right command")

print("Bye!")
