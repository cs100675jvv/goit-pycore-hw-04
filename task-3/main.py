import sys
from pathlib import Path
from colorama import Fore

'''
function visualize_dir_structure receive path to directori from command line
as an argument we give an indent for included files and directory and variable print_root
for definition if root directory should be printed 
'''

def visualize_dir_structure(dir_path, indent="    ", print_root=True): 
    dir_path = Path(dir_path)
    # check if derectory exists
    if not dir_path.exists():
        print(f"The path {dir_path} does not exist.")
        return
    # check if it is not derectory
    if not dir_path.is_dir():
        print(f"The path {dir_path} is not a directory.")
        return

    if print_root: # if root directory should be printed for awoidind double printing directory in the tree
        print(f"{Fore.YELLOW}Structure visualisation for directory\n {dir_path}/{Fore.RESET}\n")
        print(f"{Fore.BLUE}{dir_path.name}/{Fore.RESET}")
    for item in dir_path.iterdir(): #go throug the cicle to check all files or directories in current dir
        if item.is_dir(): #if we found included dir we go through with recursion
            print(f"{indent}{Fore.BLUE}{item.name}/{Fore.RESET}")
            visualize_dir_structure(item, indent=indent + "    ", print_root=False)
            
        else:
            print(f"{indent}{Fore.GREEN}{item.name}{Fore.RESET}")

# Check if the directory path is provided as a command-line argument
if len(sys.argv) > 1:
    directory_path = sys.argv[1]
    visualize_dir_structure(directory_path)
else:
    print("Please provide the directory path as a command-line argument.")