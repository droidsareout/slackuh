from commands import list_commands, commands

running_program = True

print("Slackuh \nType \".help\" for a list of commands.")

while running_program:
    sent_text = input(">> ")

    if sent_text not in commands.keys():
        print(f"\"{sent_text}\" is not a command.")

    match sent_text:
        case ".exit":
            running_program = False
        case ".list":
            list_commands()
