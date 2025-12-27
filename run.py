from commands import (
    add_question_answer,
    clear_questions_answers,
    list_commands,
    list_questions_answers,
    remove_question_answer,
)

running_program = True

print('Slackuh \nType ".help" for a list of commands.')

while running_program:
    sent_text = input(">> ")

    match sent_text:
        case ".exit":
            running_program = False
        case ".help":
            list_commands()
        case ".add":
            add_question_answer()
        case ".remove":
            remove_question_answer()
        case ".clear":
            clear_questions_answers()
        case ".list":
            list_questions_answers()
        case _:
            print(f'Error: command "{sent_text}" doesn\'t exist.')
