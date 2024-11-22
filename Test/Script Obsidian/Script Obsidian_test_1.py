# Script Obsidian_test_1.py
# Generated automatically by Generate_Test.py
# Purpose: Test file for Script Obsidian functionality
# Created: 2024-11-23 02:24:43

import unittest
import os
import shutil
from pathlib import Path

class TestScriptObsidian(unittest.TestCase):
    """Test suite for Script Obsidian functionality"""
    
    def setUp(self):
        """Set up test environment before each test"""
        self.test_dir = Path("test_output")
        self.test_dir.mkdir(exist_ok=True)
        
        # Test directory structure
        self.test_dirs = [
            "docs/notes",
            "docs/images",
            "templates/default",
            "templates/custom"
        ]
        
        # Test files
        self.test_files = [
            "docs/notes/test1.md",
            "docs/notes/test2.md",
            "templates/default/basic.md",
            "README.md"
        ]

    def tearDown(self):
        """Clean up test environment after each test"""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_directory_creation(self):
        """Test creation of directory structure"""
        for directory in self.test_dirs:
            dir_path = self.test_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            self.assertTrue(dir_path.exists())
            self.assertTrue(dir_path.is_dir())

    def test_file_creation(self):
        """Test creation of files"""
        for file in self.test_files:
            file_path = self.test_dir / file
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.touch()
            self.assertTrue(file_path.exists())
            self.assertTrue(file_path.is_file())

    def test_structure_cleanup(self):
        """Test cleanup of existing structure"""
        # Create initial structure
        test_path = self.test_dir / "temp"
        test_path.mkdir(parents=True)
        (test_path / "test.md").touch()
        
        # Verify existence
        self.assertTrue(test_path.exists())
        
        # Clean up
        shutil.rmtree(test_path)
        
        # Verify removal
        self.assertFalse(test_path.exists())

if __name__ == '__main__':
    unittest.main(verbosity=2)
