# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# cleung,6.13.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    import ProcessingClasses as Fp
    from IOClasses import EmployeeIO as IO
else:
    raise Exception("This file was not created to be imported")
# Main Body of Script  ---------------------------------------------------- #
file_name = "EmployeeData.txt"
lstTable = []
try:
    # Load data from file into a list of employee objects when script starts
    load_file = Fp.FileProcessor.read_data_from_file(file_name)
    for line in lstTable:
        lstTable.append(Emp(line[0],line[1],line[2].strip()))
    # Show user a menu of options
    while True:
        IO.print_menu_items()
    # Get user's menu option choice
        user_choice = IO.input_menu_options()
        # Show user current data in the list of employee objects
        if user_choice.strip() == '1':
            IO.print_current_list_items(lstTable)
            continue
        # Let user add data to the list of employee objects
        elif user_choice.strip() == '2':
            lstTable.append(IO.input_employee_data())
            IO.print_current_list_items(lstTable)
        # Let user save current data to file
        elif user_choice.strip() == '3':
            Fp.FileProcessor.save_data_to_file(file_name,lstTable)
            print("Data Saved to File.")
        # Let user exit program
        elif user_choice.strip() == '4':
            input("Press Enter key to exit.")
            print("Thank you, bye!")
            break
except Exception as e:
    print("Error Occured:")
    print(e)
# Main Body of Script  ---------------------------------------------------- #
