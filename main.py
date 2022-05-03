class PandP:

    # Definds list
    def __init__(self):
        self.list = []

    # A method that replaces comma's with '\t'
    def replace(self, string):
        # Appends everything in string into list
        for element in range(len(string)):
            self.list.append(string[element])
            # Replaces any comma's with '\t'
            if string[element] == ',':
                self.list[element] = "\t"

    # Prints the elements in list
    def printit(self):
        # Gets the index for each element
        for element in range(len(self.list)):
            # Checks if it's the last element
            if element == len(self.list) - 1:
                # If it is then doesn't have end=""
                print(self.list[element])
            # if not last element then it prints with end=""
            else:
                print(self.list[element], end="")


def main():
    # A while loop
    i = True
    while i:
        # Finds the input
        string = input("Input(Type quit to end program): ")
        # Checks if they want to quit
        if string.lower() == "quit":
            # If so then it makes i false making the while loop fail
            i = False
        # If string does not equal quit then it makes a class and runs replace and printit
        else:
            pandp = PandP()
            pandp.replace(string)
            pandp.printit()
    # Text to show that the program is quiting
    print("Quiting...\nQuit")


main()
