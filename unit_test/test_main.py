import os
from pathlib import Path

class TestDirectories:
    
    def test_find_root_dir(self):
        PROJECT_ROOT = os.path.basename((os.path.dirname(os.path.dirname(__file__))))
        assert PROJECT_ROOT == "CLI_Tree"

    def test_find_subdirectories(self):
        path = Path(".")
        for subdirectories in path.iterdir():
            if subdirectories.is_dir():
                assert True

    def test_list_files_in_subdirectories(self, path):
        subdirectory_item = list(path.glob("**/*.py"))

        print(subdirectory_item)


# x = TestDirectories()
# x.test_find_root_dir()

class TreeGenerator:
    
    def test_print_trees(self):
        pass