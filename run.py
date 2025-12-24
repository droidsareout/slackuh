running = 1

while running:
    output = input(">>")

    match output:
        case ".exit":
            running = 0
        case ""
