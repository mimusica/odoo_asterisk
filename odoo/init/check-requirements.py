#!/usr/bin/env python3
"""
Written by Christophe Langenberg  <Christophe@Langenberg.be> 04/07/2020

This script will update pip3 to the most recent version and
checks a requirements.txt file for missing libraries.
If there is one or more libraries missing, it will do a 'pip3 install -r requirements.txt'.
"""
from subprocess import Popen, PIPE, run, CalledProcessError
import os

def upgrade_pip():
    """
    upgrade pip to the latest version
    """
    run(['pip3', 'install', '--upgrade', 'pip'])

def check_requirements_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        to_install = []

        pip = pip_list()
        for line in lines:
            lib = check_git(line)
            if lib not in pip:
                to_install.append(lib)

        return to_install

def check_git(lib):
    """
    This function checks if a library comes from a git repository.
    If it does, then it will extract the library name from the url
    """
    if lib[:3] == 'git':
        # get the last part of the url
        libr = lib.rsplit('/', 1)[-1]
        # cut off the extention and strip the newline char
        return os.path.splitext(libr)[0].rstrip()
    else:
        return lib.rstrip()

def pip_list():
    """
    This enumerates all installed python3 libraries
    """
    cmd1 = Popen(['pip3', 'list'], stdout=PIPE, stderr=PIPE)
    output, error = cmd1.communicate()
    # making sure that we only get the library names, without the version number
    clean_output = output.decode('utf-8').split()[4::2]
    return clean_output

def install_requirements(file):
    """
    Installs the missing libraries.
    """
    try:
        run(['pip3','install','-r', file], stdout=PIPE, stderr=PIPE)
    except CalledProcessError as err:
        print(err)

if __name__=='__main__':
    upgrade_pip()

    file='/requirements.txt'

    if check_requirements_file(file):
        print('The following libraries need to be installed: \n>>> {}'.format(check_requirements_file(file)))
        install_requirements(file)