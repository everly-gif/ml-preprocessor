import pyfiglet
from preprocesscli.parse_csv import ParseFile
from preprocesscli.commands import Commands

class Preprocessor:

    data = 0

    def __init__(self):
        result = pyfiglet.figlet_format("ML PREPROCESSOR", font = "slant"  )
        print(result)

        print("""Welcome to the ML Preprocessor CLI Tool. This tool will help you save time by helping you in preprocessing all your data..""")

        print("\nThis tool is going to parse your data , do you agree with that? [y/n]")

        try:

            agree_choice = input("ml-preprocessor>").lower()
        
        except KeyboardInterrupt:
                print("Shutting down...")
                exit()

        if(agree_choice != 'y'):
            exit()
        else:
            try:
                print("\nPlease input your data to begin ...")
                command = input("ml-preprocessor>")
            except KeyboardInterrupt:
                print("Shutting down...")
                exit()
            x = command.split()
            self.data = ParseFile.input(self,x)
    
    def preprocessMain(self):
        while(1):
            try:
                command = input("\nml-preprocessor>")
            except KeyboardInterrupt:
                print("Shutting down...")
                exit()
            x = command.split()
            self.data = Commands(self.data).command(x)


obj = Preprocessor()
obj.preprocessMain()
