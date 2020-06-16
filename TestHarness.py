# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# cleung,6.14.2020, pasted listing 08 and modified code in TestHarness
# ---------------------------------------------------------- #
if __name__ == "__main__":
    from DataClasses import Employee as Emp  # Employee class only!
    import ProcessingClasses as Fp  # processing classes
    from IOClasses import EmployeeIO as Eio

else:
    raise Exception("This file was not created to be imported")

# Test data module
objP1 = Emp(1, "Bob", "Smith")
objP2 = Emp(2, "Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))

# Test processing module
Fp.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
lstFileData = Fp.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))

# Test IO classes
Eio.print_menu_items()
Eio.print_current_list_items(lstTable)
print(Eio.input_employee_data())
print(Eio.input_menu_options())
