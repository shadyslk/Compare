import pandas as pd

##########################################3######
# function for extracting file contents to list #
#################################################

def file_to_list(filename : str):
    print(f"Converting '{filename}' to list...")
    with open(filename, "r") as file:
        return [line.rstrip().lower() for line in file]

########################################################
# function for comparing lists and outputing to a list #
########################################################

def compare_lists(list_1 : list, list_2 : list):
    print("Comparing files...")
    return [item for item in list_1 if item in list_2]

#####################
# gather user input #
#####################

print("Select files to compare.")

try:
    file_1 : str = str(input("Name of file 1: "))
    file_2 : str = str(input("Name of file 2: "))
    output_name : str = str(input("Name of output file name (no extension): "))
except:
    print("Exception: User input error.")

####################################
# compare lists and output to list #
####################################

try:
    output_list : list = compare_lists(file_to_list(file_1), file_to_list(file_2))
except:
    print("Exception: Files could not be compared.")

###################
# output to files #
###################

print("Outputting list to file...")

output_df = pd.DataFrame(output_list, columns=["Similarities"])
output_df.to_csv(f"{output_name}.csv", index=False)

print(f"'{output_name}.csv' created!")