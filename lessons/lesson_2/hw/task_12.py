command = "save"

match command:
    case "save":
        print("Save")
    case "new":
        print("New")
    case "open":
        print("Open")
    case "close":
        print("Close")
    case "quit" | "exit":
        print("Stop execution")
    else:
        print("Unknown command")

if command == "save":
    print("Save")
elif command == "new":
    print("New")
elif command == "open":
    print("Open")
elif command == "close":
    print("Close")
elif command == "quit" or command == "exit":
    print("Stop execution")
else:
    print("Unknown command")

# part 2
command = ("move", 100, 200)

match command:
    case ("move", *coords):
        print(f"Move element to {coords}")
    case ("stop", *_):
        print("Stop execution")
    case ("resize", width, height):
        print(f"Resize width {width} and height to {height}")
    case _:
        print("Unknown command")
