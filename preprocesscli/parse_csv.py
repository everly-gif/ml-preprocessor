import pandas as pd
class ParseFile:
    def input(self,x):
        try:
            if(x[0]=='parse' and x[1]=='data' and len(x)==3):
                data = pd.read_csv(x[2])
                print("\nData Read successfully")
                print(data)
                return data
            else:
                raise Exception()
        except:
            print("Invalid Argument Length or command, format should be parse data <csv file>")
            exit()

