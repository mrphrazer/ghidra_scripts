#!/usr/bin/python
import os
import sys
import tempfile


def get_ghidra_path():
    """
    Returns Ghidra path
    :return: string
    """
    return "/usr/bin/ghidra-analyzeHeadless"


def check_ghidra():
    """
    Checks if Ghidra executable exists
    """
    if not os.path.exists(get_ghidra_path()):
        print(f"{get_ghidra_path()} does not exist!")
        exit(-1)


def get_ghidra_command(project_path, input_file, script_path, script_arguments):
    """
    Builds the Ghidra command
    :param project_path: name of temp directory
    :param input_file: string, path to binary file
    :param script_path: string, path to script file
    :param script_arguments: string of script arguments
    :return: Ghidra command as string
    """
    ghidra_path = get_ghidra_path()
    project_name = "ghidra_project"
    dir_path = os.path.dirname(script_path)
    return f"{ghidra_path} {project_path} {project_name} -import {input_file} -postscript {script_path} {script_arguments}"


def run_ghidra(input_file, script_path, script_arguments):
    """
    Builds Ghidra command and runs exporter script
    :param input_file: string, path to binary file
    :param script_path: string, path to script file
    :param script_arguments: string of script arguments
    """
    # check if ghidra exists
    check_ghidra()

    # init temp dir
    tmp_dir = tempfile.TemporaryDirectory()

    # init
    project_path = str(tmp_dir.name)

    # gen command
    cmd = get_ghidra_command(project_path, input_file,
                             script_path, script_arguments)

    # execute command
    os.system(cmd)

    # cleanup temp dir
    tmp_dir.cleanup()


# check arguments
if len(sys.argv) < 2:
    print("[*] Syntax: {} <path to binary> <script file> <script arguments>".format(sys.argv[0]))
    exit(0)

# parse arguments
input_file = sys.argv[1]
script_path = sys.argv[2]

# parse script arguments
if len(sys.argv) > 3:
    script_arguments = " ".join(sys.argv[3:])
else:
    script_arguments = ""

# run ghidra script
run_ghidra(input_file, script_path, script_arguments)
