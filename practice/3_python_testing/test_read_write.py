"""
Write tests for python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
import tempfile
import os

from practice.python_part_2.task_read_write import *
import pytest


def test_input_output(tmp_path):
    # create temp directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        # create temp files
        f1 = tempfile.TemporaryFile(mode = 'w+', dir=tmpdirname)
        f1.write('56')
        f1.seek(0)

        f2 = tempfile.TemporaryFile(mode='w+', dir=tmpdirname)
        f2.write('99')
        f2.seek(0)

        f3 = tempfile.TemporaryFile(mode='w+', dir=tmpdirname)
        f3.write('14')
        f3.seek(0)

        results = tempfile.TemporaryFile(mode="w+", dir=tmpdirname)

        read_write(tmpdirname, f"{tmpdirname}/{results}")

        assert results.read() == '56'

