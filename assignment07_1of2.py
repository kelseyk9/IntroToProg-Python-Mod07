# ------------------------------------------------- # 
# Title: Assignment 07 
# Description: An example of pickling  
# ChangeLog: (Who, When, What) 
# Kelsey Kawaguchi,11.24.2019,Created Script 
# ------------------------------------------------- # 
import pickle 
# This imports code from another code file! 
# Data -------------------------------------------- # 
strFileName = 'AppData.dat' 
lstStudent = [] 
strName = ""
strID = ""
objFile = ""
# Processing -------------------------------------- # 
def save_data_to_file(file_name, list_of_data): 
    """ A function to save data to a file 
    
    :param file_name: (string) with name of file
    :param list_of_data: (string) with data to save
    :return: (string) with data to save
    """
    objFile = open(file_name, "wb")
    pickle.dump(list_of_data, objFile)
    objFile.close()
   
    
def read_data_from_file(file_name): 
    """ A function to read data from a file
    
    :param file_name: (string) with name of file
    :return: (string) with data to save
    """
    objFile = open(file_name, "rb")
    list_of_data = pickle.load(objFile)
    objFile.close()
    return list_of_data 
    

# Presentation ------------------------------------ # 
# TODO: Get ID and NAME From user, then store it in a list object
strName = str(input("Enter your name: "))
strID = str(input("Enter your GPA: ")) 
lstStudent = [strID, strName] 


# TODO: store the list object into a binary file 
save_data_to_file(strFileName, lstStudent)

# TODO: Read the data from the file into a new list object and display the contents
print(read_data_from_file(strFileName))