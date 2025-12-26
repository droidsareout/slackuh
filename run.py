from commands import list_commands

running_program = True

print("Entered Slackuh")

while running_program:
    output = input(">> ")

    match output:
        case ".exit":
            running_program = False
        case ".list":
            list_commands()
