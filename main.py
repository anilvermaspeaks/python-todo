todos = []
while True:
    user_action = input("Type action(add or show): ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break
        case _:
            print("Hey, Please enter correct command(add/show/exit)")
print("Bye!")


