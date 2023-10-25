import sys, os
import pytest

passwordDatabase = None
def add_parent_dir_to_path():
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    sys.path.append(parent_directory)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    add_parent_dir_to_path()
    from PasswordDatabase import PasswordDatabase
    global passwordDatabase
    passwordDatabase = PasswordDatabase



def test_example():
    assert 0 == False

def test_exampl2():
    assert 1 == passwordDatabase.get_const()

def test_example3():
    assert 2 == passwordDatabase.get_const2()