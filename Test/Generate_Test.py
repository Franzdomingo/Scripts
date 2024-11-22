import os
import time

def list_existing_folders():
    """
    Lists all existing folders in the test directory.
    
    Returns:
        list: A list of folder names in the test directory
    """
    test_dir = os.path.dirname(os.path.abspath(__file__))
    folders = [d for d in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, d))]
    if folders:
        print("\nExisting folders:")
        for idx, folder in enumerate(folders, 1):
            print(f"{idx}. {folder}")
    return folders

def find_next_test_number(folder_path, folder_name):
    """
    Determines the next sequential test number for a given folder.
    
    Args:
        folder_path (str): Path to the folder containing test files
        folder_name (str): Name of the folder for test file prefix
    
    Returns:
        int: Next available test number in sequence
    """
    # Find all test files with the folder name prefix in the folder
    test_files = [f for f in os.listdir(folder_path) 
                  if f.startswith(f'{folder_name}_test_') and f.endswith('.py')]
    
    if not test_files:
        return 1
    
    # Extract numbers from existing test files
    numbers = []
    prefix = f'{folder_name}_test_'
    for file in test_files:
        try:
            num = int(file.replace(prefix, '').replace('.py', ''))
            numbers.append(num)
        except ValueError:
            continue
    
    # Return next number in sequence
    return max(numbers) + 1 if numbers else 1

def generate_test():
    """
    Main function to generate test files.
    
    This function:
    1. Allows users to create a new folder or select an existing one
    2. Creates a new test file with sequential numbering
    3. Names the test file using the pattern: {folder_name}_test_{number}.py
    4. Places the test file in the selected folder
    """
    test_dir = os.path.dirname(os.path.abspath(__file__))
    
    # List existing folders and get user choice
    existing_folders = list_existing_folders()
    print("\nChoose an option:")
    print("1. Create new folder")
    if existing_folders:
        print("2. Use existing folder")
    
    choice = input("Enter your choice (1" + (" or 2" if existing_folders else "") + "): ")
    
    if choice == '1':
        folder_name = input("Enter the new folder name: ")
        folder_path = os.path.join(test_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created new folder: {folder_name}")
    elif choice == '2' and existing_folders:
        while True:
            folder_idx = input(f"Enter folder number (1-{len(existing_folders)}): ")
            try:
                folder_idx = int(folder_idx) - 1
                if 0 <= folder_idx < len(existing_folders):
                    folder_name = existing_folders[folder_idx]
                    folder_path = os.path.join(test_dir, folder_name)
                    break
                else:
                    print("Invalid folder number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("Invalid choice.")
        return
    
    # Get next test number for the selected folder
    next_num = find_next_test_number(folder_path, folder_name)
    new_filename = f'{folder_name}_test_{next_num}.py'
    
    # Create the test file in the selected folder
    file_path = os.path.join(folder_path, new_filename)
    with open(file_path, 'w') as f:
        f.write(f'''# {new_filename}
# Generated automatically by Generate_Test.py
# Purpose: Test file for {folder_name} functionality
# Created: {time.strftime("%Y-%m-%d %H:%M:%S")}

def test_function():
    """
    Main test function for {folder_name} module.
    Add test cases here.
    """
    pass

if __name__ == '__main__':
    test_function()
''')
    
    print(f"\nCreated {new_filename} in {folder_name}/")

if __name__ == '__main__':
    """
    Main entry point for the script.
    """
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')    
    generate_test()
    os.system('cls' if os.name == 'nt' else 'clear')    
