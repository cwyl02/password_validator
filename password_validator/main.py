#!/usr/bin/env python

import sys
import argparse

from validate import validate_passwords

def main():
    usage = """
        cat input_passwords.txt | ./password_validator weak_password_list.txt
    """
    parser = argparse.ArgumentParser(usage=usage)
    parser.add_argument('weak_pw_list_path', nargs=1, type=str)
    args = parser.parse_args(sys.argv[1:])
    validate_passwords(sys.stdin, args.weak_pw_list_path[0])

if __name__ == "__main__":
    main()
