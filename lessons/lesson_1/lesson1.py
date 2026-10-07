def main():
    print("Hello world!")

    print(5 + 9) # 14
    print('5' + '9') # 59
    print(20 * 2) # 40
    print(20 / 2) # 10.0
    print(15 // 4) # 3
    print(15 % 4) # 3

    VALUE = "Constant value"
    dynamic_value = VALUE

    # print(input("Enter Value: ") * 2)

    # STRING BELOW
    text = 'Lorem ipsum dolor set amet'
    print(text[0]) # l
    print(text[-1]) # t
    # slice 
    print(text[1:-1]) # orem ... ame ( Without t )
    print(text[1:]) # orem ... amet
    print(text[1:5]) # orem
    print(text[1:2:8]) # wtf
    # slice end

    print(text.lower()) # all lowercase
    print(text.upper()) # all uppercase
    print(text.title()) # First letter capital in each word
    print(text.capitalize()) # Only first letter capital
    print(text.isalpha()) # check if all letters ( space is not a letter )
    print(text.isdigit()) # check if digit ( Obviously )
    print(text.islower()) # lowercase
    print(text.split()) # " " by default
    result = text.split()
    print(result)
    print("".join(result))

    print(min(text)) # min letter code
    print(max(text)) # max letter code
    print(ord(max(text))) 
    print(chr(115))
    print(text.count("i"))
    print(text.index("a", 12))
    # For every iterable; DO not search out of diapason 

    print(text.find("AA"))
    print(text.strip())

main()