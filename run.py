from commands import list_commands, add_question_answer

running_program = True

print("Slackuh \nType \".help\" for a list of commands.")

while running_program:
    sent_text = input(">> ")

    match sent_text:
        case ".exit":
            running_program = False
        case ".help":
            list_commands()
        case add if sent_text.startswith(".add"):
            add_question_answer(sent_text)
        case _:
            print("Error: Command doesn't exist.")
