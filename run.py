running_program = True

while running_program:
    output = input(">>")

    match output:
        case ".exit":
            running_program = False
