from commands import list_commands, add_question_answer, command_list

running_program = True

print("Slackuh \nType \".help\" for a list of commands.")

while running_program:
    sent_text = input(">> ")

    if sent_text not in command_list.keys():
        print(f"\"{sent_text}\" is not a command.")

    match sent_text:
        case ".exit":
            running_program = False
        case ".help":
            list_commands()
        case add if sent_text.startswith(".add"):
            add_question_answer(sent_text)
