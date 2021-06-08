# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# MKarumuhinzi,6.7.2021,Modified Listing13.py pseudo-code to complete assignment 9
# MKarumuhinzi,6.7.2021,Provided codes used are: DataClasses.py, IOClasses.py & ProcessingClasses.py
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #

strFileName = "EmployeeData.txt"
lstOfEmployeeObjects = []
strChoice = ""  # Captures the user option selection

# Load data from file into a list of employee objects when script starts
lstFileData = Fp.read_data_from_file(strFileName)
lstOfEmployeeObjects.clear()
for line in lstFileData:
    lstOfEmployeeObjects.append(Emp(line[0], line[1], line[2].strip()))

while(True):
    # Show user a menu of options
    Eio.print_menu_items()
    # Get user's menu option choice
    strChoice = Eio.input_menu_options()
    
    if strChoice.strip() == '1':
        # Show user current data in the list of employee objects
        Eio.print_current_list_items(lstOfEmployeeObjects)
        
    elif strChoice == '2':
        # Let user add data to the list of employee objects
        is_success = False
        
        try:
            current_emp = Eio.input_employee_data()
            lstOfEmployeeObjects.append(current_emp)
            is_success = True
        except Exception as e:
            print(e)
        
        print()
        if is_success == True:
            print('Employee added')
        else:
            print("Operation failed")
            
        continue  # to show the menu
    
    elif strChoice == '3':
        # let user save current data to file
        data_saved = Fp.save_data_to_file(strFileName, lstOfEmployeeObjects)
        print()
        if data_saved == True:
            print("Data saved.")
        else:
            print("Data not saved.")
        
        continue  # to show the menu
    
    elif strChoice == '4':
        # Let user exit program
        print("Goodbye!")
        break  # and Exit    

# Main Body of Script  ---------------------------------------------------- #
