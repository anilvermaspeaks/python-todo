todos = []
while True:
    user_action = input("Type action(add,show or edit): ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'edit':
            for item in todos:
                print(item)
            number = int(input("index no of todo to change: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("Hey, Please enter correct command(add/show/exit)")
print("Bye!")


