import subprocess
import re

def testPython():
    result = subprocess.check_output(['python', '--version']).decode()
    print(result)
    assert re.search("^Python 3", result)

def testJava():
    result = subprocess.check_output(['java', '--version']).decode()
    print(result)
    assert re.search("OpenJDK Runtime Environment Temurin", result)
    result = subprocess.check_output(['javac', '--version']).decode()
    print(result)
    assert re.search("^javac 17", result)

def testNode():
    result = subprocess.check_output(['node', '--version']).decode()
    print(result)
    assert re.search("^v18", result)

def testMaven():
    result = subprocess.check_output(['mvn', '--version']).decode()
    print(result)
    assert re.search("Apache Maven 3", result)

def testGradle():
    result = subprocess.check_output(['gradle', '--version']).decode()
    print(result)
    assert re.search("Gradle 8", result)

def testNpm():
    result = subprocess.check_output(['npm', '--version']).decode()
    print("npm ", result)
    assert re.search("^9.", result)

def testGit():
    result = subprocess.check_output(['git', '--version']).decode()
    print(result)
    assert re.search("^git version", result)

if __name__ == "__main__":
    testPython()
    testJava()
    testNode()
    testMaven()
    testGradle()
    testNpm()
    testGit()
