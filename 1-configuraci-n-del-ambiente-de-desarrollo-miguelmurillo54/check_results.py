import subprocess
import re

# pipenv run pytest -rA check_results.py -k 'not testFiles'
def testResults():
    file = open('test_results.txt',mode='r')
    results = file.read()
    file.close()
    tests = [
        "testPython",
        "testJava",
        "testNode",
        "testMaven",
        "testGradle",
        "testNpm",
        "testGit"
        ]
    for test in tests:
        assert re.search("PASSED envcheck.py::"+test, results)
    assert re.search("7 passed", results)

import os

# pipenv run pytest -rA check_results.py -k 'testFiles'
def testFiles():
    assert os.path.exists('test_results.txt')