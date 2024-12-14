import os

def create_folders(base_path, folder_structure):
    for folder, subfolders in folder_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if subfolders:
            create_folders(folder_path, subfolders)

# Define folder structure
folder_structure = {
    "01 - Inbox": {},
    "02 - Areas": {
        "Personal": {},
        "Professional": {},
        "Health & Fitness": {},
        "Hobbies": {},
        "Finance": {}
    },
    "03 - Projects": {},
    "04 - Resources": {
        "Books": {},
        "Courses": {},
        "Templates": {},
        "Tools": {},
        "Articles": {}
    },
    "05 - Knowledge": {
        "Notes": {},
        "FAQs & Tutorials": {},
        "Personal Lessons": {}
    },
    "06 - Archive": {},
    "Templates": {}
}

# Set base path
base_path = r"G:\\My Drive\\secondbrain\\second_brain"

# Create folder structure
create_folders(base_path, folder_structure)

print("Folder structure created successfully at", base_path)
