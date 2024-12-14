# obsidian-create-second-brain-test_test_1.py
# Generated automatically by Generate_Test.py
# Purpose: Test file for obsidian-create-second-brain-test functionality
# Created: 2024-12-14 20:26:51

import sys
import os
import unittest
import tempfile
import shutil

# Add the project's root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.ObsidianScript_secondbraininitialformat import create_folders, folder_structure

class TestCreateFolders(unittest.TestCase):
    def setUp(self):
        """
        Initialize a temporary directory before each test.
        """
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        """
        Remove the temporary directory after each test.
        """
        shutil.rmtree(self.temp_dir)

    def test_create_folders_structure(self):
        """
        Verify that the folder structure is created correctly within the temporary directory.
        """
        create_folders(self.temp_dir, folder_structure)
        for folder, subfolders in folder_structure.items():
            folder_path = os.path.join(self.temp_dir, folder)
            self.assertTrue(os.path.isdir(folder_path), f"Folder {folder} was not created.")
            self._check_subfolders(folder_path, subfolders)

    def _check_subfolders(self, parent_path, subfolders):
        """
        Recursively check the presence of subfolders.
        """
        for subfolder, nested_subfolders in subfolders.items():
            subfolder_path = os.path.join(parent_path, subfolder)
            self.assertTrue(os.path.isdir(subfolder_path), f"Subfolder {subfolder} was not created in {parent_path}.")
            if nested_subfolders:
                self._check_subfolders(subfolder_path, nested_subfolders)

if __name__ == '__main__':
    unittest.main()
