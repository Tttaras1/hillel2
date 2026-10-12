color = "yellow"

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Wait or Get ready")
elif color == "green":
    print("Go if safe")
else:
    print("Unknown signal")

# match color:
#     case "red":
#         print("Stop")
#     case "yellow":
#         print("Wait or Get ready")
#     case "green":
#         print("Go if safe")
#     case _:
#         print("Unknown signal")