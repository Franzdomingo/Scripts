# Organizer Test_test_1.py
# Generated automatically by Generate_Test.py
# Purpose: Test file for Organizer Test functionality
# Created: 2024-11-23 02:22:22

import unittest
import os
import shutil
from pathlib import Path
import sys

# Add the parent directory to the Python path to allow importing from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.Organizer import MediaOrganizer

class TestMediaOrganizer(unittest.TestCase):
    def setUp(self):
        """Create a temporary test directory structure."""
        self.test_dir = Path("test_vault")
        self.test_dir.mkdir(exist_ok=True)
        
        # Create some test files
        (self.test_dir / "test.jpg").touch()
        (self.test_dir / "test.mp4").touch()
        (self.test_dir / "test.mp3").touch()
        (self.test_dir / "test.md").touch()  # Should be ignored
        
        # Create a subdirectory with files
        subdir = self.test_dir / "subdir"
        subdir.mkdir(exist_ok=True)
        (subdir / "subdir_test.png").touch()
        
        self.organizer = MediaOrganizer(str(self.test_dir))

    def tearDown(self):
        """Clean up test directory after tests."""
        if self.test_dir.exists():
            shutil.rmtree(self.test_dir)

    def test_create_media_folders(self):
        """Test if media folders are created correctly."""
        test_dir = self.test_dir / "test_create"
        test_dir.mkdir(exist_ok=True)
        self.organizer.create_media_folders(test_dir)
        
        self.assertTrue((test_dir / "files").exists())
        self.assertTrue((test_dir / "files" / "images").exists())
        self.assertTrue((test_dir / "files" / "videos").exists())
        self.assertTrue((test_dir / "files" / "audio").exists())

    def test_get_media_files(self):
        """Test if media files are correctly identified."""
        media_files = self.organizer.get_media_files()
        
        # Convert paths to strings for easier comparison
        file_names = {str(f.name) for f in media_files}
        expected_files = {"test.jpg", "test.mp4", "test.mp3", "subdir_test.png"}
        
        self.assertEqual(file_names, expected_files)
        self.assertNotIn("test.md", file_names)

    def test_get_media_type(self):
        """Test if media types are correctly identified."""
        self.assertEqual(self.organizer.get_media_type(".jpg"), "images")
        self.assertEqual(self.organizer.get_media_type(".mp4"), "videos")
        self.assertEqual(self.organizer.get_media_type(".mp3"), "audio")
        self.assertEqual(self.organizer.get_media_type(".unknown"), "other")

    def test_organize_files(self):
        """Test if files are organized correctly."""
        self.organizer.organize_files()
        
        # Check if files were moved to correct directories
        self.assertTrue((self.test_dir / "files" / "images" / "test.jpg").exists())
        self.assertTrue((self.test_dir / "files" / "videos" / "test.mp4").exists())
        self.assertTrue((self.test_dir / "files" / "audio" / "test.mp3").exists())
        self.assertTrue((self.test_dir / "subdir" / "files" / "images" / "subdir_test.png").exists())
        
        # Check if original files were moved
        self.assertFalse((self.test_dir / "test.jpg").exists())
        self.assertFalse((self.test_dir / "test.mp4").exists())
        self.assertFalse((self.test_dir / "test.mp3").exists())
        
        # Check if .md file remains untouched
        self.assertTrue((self.test_dir / "test.md").exists())

if __name__ == '__main__':
    unittest.main()
