"""
File Organizer for Obsidian Vault
Organizes media files into structured folders based on their extensions.

Created by: Franz Phillip G. Domingo
Date: 2024-11-23
Version: 0.0.2
"""

import os
import shutil
from pathlib import Path
from typing import Dict, List, Set
from tkinter import filedialog, Tk

class MediaOrganizer:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.media_extensions: Dict[str, Set[str]] = {
            'images': {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', 
                      '.webp', '.svg', '.ico', '.heic', '.heif', '.avif'},
            'videos': {'.mp4', '.webm', '.ogg'},
            'audio': {'.mp3', '.wav', '.flac', '.aac', '.m4a', '.wma'}
        }
        
    def create_media_folders(self, directory: Path) -> None:
        """Creates organized folder structure within specified directory."""
        files_folder = directory / "files"
        files_folder.mkdir(exist_ok=True)
        
        for folder in self.media_extensions.keys():
            folder_path = files_folder / folder
            folder_path.mkdir(exist_ok=True)
            
    def get_media_files(self) -> List[Path]:
        """Returns a list of all media files in the root directory, excluding .md files."""
        all_extensions = set().union(*self.media_extensions.values())
        return [f for f in self.root_dir.rglob('*') 
                if f.suffix.lower() in all_extensions
                and f.is_file()
                and not f.suffix.lower() == '.md'
                and 'files' not in f.parts  # Exclude files already in 'files' directory
                and not f.name.startswith('.')]  # Exclude hidden files

    def get_media_type(self, file_extension: str) -> str:
        """Determines the media type based on file extension."""
        for media_type, extensions in self.media_extensions.items():
            if file_extension.lower() in extensions:
                return media_type
        return 'other'

    def organize_files(self) -> None:
        """Organizes media files into their respective folders within each directory."""
        # Get all subdirectories in the vault
        directories = [d for d in self.root_dir.rglob('*') 
                      if d.is_dir() 
                      and not d.name.startswith('.')
                      and not any(parent.name == 'files' for parent in d.parents)]

        # Add root directory to the list
        directories.append(self.root_dir)

        for directory in directories:
            self.create_media_folders(directory)
            
            # Get media files in current directory only
            media_files = [f for f in directory.glob('*') 
                          if f.is_file() 
                          and f.suffix.lower() in set().union(*self.media_extensions.values())
                          and not f.name.startswith('.')]

            files_folder = directory / "files"
            for file_path in media_files:
                media_type = self.get_media_type(file_path.suffix)
                if media_type != 'other':
                    destination = files_folder / media_type / file_path.name
                    
                    # Handle duplicate filenames
                    if destination.exists():
                        base = destination.stem
                        counter = 1
                        while destination.exists():
                            new_name = f"{base}_{counter}{destination.suffix}"
                            destination = destination.with_name(new_name)
                            counter += 1
                    
                    try:
                        shutil.move(str(file_path), str(destination))
                        print(f"Moved {file_path.name} to {destination.relative_to(self.root_dir)}")
                    except Exception as e:
                        print(f"Error moving {file_path.name}: {str(e)}")

def select_directory() -> str:
    """Opens a directory selection dialog and returns the selected path."""
    root = Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory(title="Select your Obsidian Vault directory")
    root.destroy()
    return directory

def main():
    # Prompt user to select Obsidian vault directory
    vault_dir = select_directory()
    
    if not vault_dir:
        print("No directory selected. Exiting...")
        return
    
    print(f"Selected directory: {vault_dir}")
    
    # Create and run the organizer
    organizer = MediaOrganizer(vault_dir)
    organizer.organize_files()
    print("\nOrganization complete!")

if __name__ == "__main__":
    main()
