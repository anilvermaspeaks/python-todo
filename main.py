todos = []
while True:
    user_action = input("Type action(add,show, done or edit): ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'edit':
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
            number = int(input("index no of todo to change: "))
            number = number -1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index +1}-{item}"
                print(row)
        case 'done':
            number = int(input("index no of todo to make complete: "))
            todos.pop(number)
        case 'exit':
            break
        case _:
            print("Hey, Please enter correct command(add/show/exit)")
print("Bye!")


