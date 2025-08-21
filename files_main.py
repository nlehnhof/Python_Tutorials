try: 
    file = open('test.txt', 'r')
except FileNotFoundError:
    print('File not found.')
    exit()
finally:
    print("Attempted to open the file.")


try:
    num = int(input("Enter a number: "))
except Exception as e:
    print(e)
    print("Invalid input. Please enter a number")
    num = 0
finally:
    print(f'We will use the number: {num}')

# file.read() gives me everything
context = file.read()

# print(context)
file.close()

# print(context.find("baby"))

#.readlines()  list of strings (all the lines of the file)
file = open("test.txt", "r")
lines = file.readlines()

# list comprehension to strip whitespace
lines = [line.strip() for line in lines]

# print(lines)
file.close()

## WRITE ##
# file = open('number1.txt', 'w')
# file.write('1\n')
# file.close()

