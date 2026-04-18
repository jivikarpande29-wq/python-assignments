#Program to open a file and handle exceptions

filename = input("Enter the filename: ")

try:
    file = open(filename, 'r')
    content = file.read()
    print("\nFile opened successfully!\n")
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: You do not have permission to read this file.")

except Exception as e:
    print("An unexpected error occurred:", e)