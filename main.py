import os

def rename(path,extension):
    
    list_of_files = os.listdir(path)  #make the list of all the files present in the directory
    count = 0  #add the counter to rename.
    if os.path.exists(path):
        
        for file in list_of_files:
            old_path = os.path.join(path,file) #make the connection between file name and path
            old_path_extension = old_path[-1:-4:-1] #I used to check whether the file is our required extension or not by using slicing.
            old_pather = old_path_extension[::-1] # reverse it because it was not in original condition.
            if old_pather == extension:
                count+=1  #making counter which will increse after every iteration.
                new_name = f"{count}.{extension}" #making the new name
                new_path = os.path.join(path,new_name) #
                os.rename(old_path,new_path) #renaming the file.
                
            else:
                print(f"There is no file with the extension .{extension}")
                
        
    else:
        print("Invalid path")
        print("Write a valid path.")



path = input("Enter the path of the directory: ") # taking input the path and extension
extension = input("Enter the extension: ")
rename(path,extension) #calling the function.
