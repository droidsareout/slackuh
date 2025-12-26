from commands import list_commands

running_program = True

print("Slackuh \nType \".help\" for a list of commands.")

while running_program:
    sentText = input(">> ")

    match sentText:
        case ".exit":
            running_program = False
        case ".list":
            list_commands()
