import unittest
import os
import shutil
import tempfile

import numpy as np
import omf
import omfvtk
import vista


DATA_FILE = os.path.join(os.path.dirname(__file__), '../assets/test_file.omf')

class TestProjectIO(unittest.TestCase):
    """
    Test the wrapper for a project file which will iterate over all data types.
    This will then save out a ``vista.MultiBlockDataSet`` and reload it
    """
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.project_filename = os.path.join(self.test_dir, 'project.vtm')

    def tearDown(self):
        # Remove the test data directory after the test
        shutil.rmtree(self.test_dir)

    def test_load_project(self):
        """Test loading a sample project file"""
        data = omfvtk.load_project(DATA_FILE)
        self.assertIsNotNone(data)
        self.assertTrue(isinstance(data, vista.MultiBlock))
        self.assertEqual(data.n_blocks, 9)

    # def test_save_project(self):
    #     """Test saving a sample project file in the VTK format"""
    #     data = omfvtk.load_project(DATA_FILE)
    #     data.save(self.project_filename)
    #     # And reload that project
    #     data = vista.read(self.project_filename)
    #     self.assertTrue(isinstance(data, vista.MultiBlock))
    #     self.assertEqual(data.n_blocks, 9)




if __name__ == '__main__':
    import unittest
    unittest.main()
