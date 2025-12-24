running_program = 1

while running_program:
    output = input(">>")

    match output:
        case ".exit":
            running_program = 0
        case ""
