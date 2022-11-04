from sklearn.preprocessing import MinMaxScaler, StandardScaler
import string
import random
import pandas as pd

class Commands:

    data = 0

    def __init__(self,data):
       self.data = data

    def command(self, x ):

        if(x[0]=="drop" and x[1]=="column"):
            extractColumn = x[2].split("=")
            if(extractColumn[0]=='--column'):
                self.data = self.data.drop(columns = extractColumn[1],axis =1)
                print("\n Dropped column "+extractColumn[1]+" Successfully...")
                print(self.data)
                return self.data
            else:
                print("Invalid argument for command drop column")
                return self.data
        elif(x[0]=='describe' and len(x)==1):
            print(self.data.describe())
            return self.data
        elif(x[0]=='describe' and len(x)>1):
            extractColumn = x[1].split("=")
            if(extractColumn[0]=='--column'):
                print(self.data[extractColumn[1]].describe())
                return self.data
            else:
                print("Invalid argument for command describe column")
                return self.data
        elif(x[0]=="show" and x[1]=="data"):
            print(self.data)
            return self.data
        elif(x[0]=="show" and x[1]=="columnNames"):
            for i,j in enumerate(self.data.columns,start=1):
                print("{}.{}".format(i,j), end=" ")
            return self.data
        elif(x[0]=="getInfo"):
            print(self.data.info())
            return self.data
        elif(x[0]=="show" and x[1]=="null" and x[2]=="columns"):
            print("\nThese are the columns where NULL values are present")
            nullColumns = []
            for i in self.data.columns:
                if(self.data[i].isnull().values.any()):
                    nullColumns.append(i)
            print(nullColumns)
            return self.data
        elif(x[0]=="remove" and x[1]=="null" and len(x)==4):
            extractColumn = x[2].split("=")
            extractOption = x[3].split("=")
            extractColumns = extractColumn[1].split(",")
            for i in extractColumns:
                self.data[extractColumns] = self.data[extractColumns].fillna(value=eval(extractOption[1]))
            print(self.data)
            print("\nThese are the columns where NULL values are present")
            nullColumns = []
            for i in self.data.columns:
                if(self.data[i].isnull().values.any()):
                    nullColumns.append(i)
            print(nullColumns)
            return self.data
        elif(x[0]=="remove" and x[1]=="null"):
            extractColumn = x[2].split("=")
            extractColumns = extractColumn[1].split(",")
            for i in extractColumns:
                self.data = self.data.dropna(axis = 0, subset =[i])
            print(self.data)
            return self.data
        # show object columns
        elif(x[0]=="encode" and x[1]=="column"):
            extractColumn = x[2].split("=")
            extractColumns = extractColumn[1].split(",")
            if(extractColumns[0] == "all"):
                categorical_columns = self.data.select_dtypes(include="object")
                for column in categorical_columns:
                    self.data = pd.get_dummies(data=self.data, columns = [column])
                    print(self.data)
                    return self.data
            else:
                categorical_columns = self.data.select_dtypes(include="object")
                for i in extractColumns:
                    if i in categorical_columns:
                        self.data = pd.get_dummies(data=self.data, columns = [i])
                        print(self.data)
                        return self.data
                    else:
                        print("Cannot encode this column")
                        return self.data
        elif(x[0]=="normalize" and x[1]=="columns"):
            try:
                self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data))
                print(self.data)
                return self.data
            except:
                print("String columns are present, not possible")
                return self.data
        elif(x[0]=="normalize" and x[1]=="column"):
            extractColumn = x[2].split("=")
            extractColumns = extractColumn[1].split(',')
            extractOptions = x[3].split("=")
            extractOption = extractOptions[1]
            if(extractOption=="minmax"):
                for i in extractColumns:
                    self.data[i] = (self.data[i] - self.data[i].min())/(self.data[i].max() - self.data[i].min())
                    print(self.data[i])
                    return self.data
            elif(extractOption=="abs"):
                for i in extractColumns:
                    self.data[i] = self.data[i] / self.data[i].abs().max()
                print(self.data[i])
                return self.data
        elif(x[0]=="standardize" and x[1]=="columns"):
            try:
                self.data = pd.DataFrame(StandardScaler().fit_transform(self.data))
                print(self.data)
                return self.data
            except:
                print("String columns are present, not possible")
                return self.data
        elif(x[0]=="standardize" and x[1]=="column"):
            extractColumn = x[2].split("=")
            extractColumns = extractColumn[1].split(',')
            for column in extractColumns:
                self.data[column] = (self.data[column] - self.data[column].mean()) / self.data[column].std() 
                print(self.data)
                return self.data
        elif(x[0]=="download" and x[1]=="data"):
            newFileName = ''.join(random.choices(string.ascii_letters, k=7))
            pd.DataFrame(self.data).to_csv(newFileName+".csv", index = False)
            exit()
        else:
            print("Invalid")
            exit() 
    