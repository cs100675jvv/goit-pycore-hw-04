import sys
from data import visualize_dir_structure

def main():
    # Check if the directory path is provided as a command-line argument
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        visualize_dir_structure(directory_path)
    else:
        print("Please provide the directory path as a command-line argument.")

if __name__ == "__main__":
    main()