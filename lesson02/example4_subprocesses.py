""" Example 4

Subprocesses
"""
import subprocess

subprocess.call(['echo', 'hello call'], shell=True)

PIPE_ECHO = subprocess.Popen(['echo', 'hello Popen'],
                             shell=True,
                             stdout=subprocess.PIPE)

print PIPE_ECHO.communicate()
