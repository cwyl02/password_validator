import sys
import argparse

from validate import validate_passwords

def main():
    usage = """
        cat input_passwords.txt | ./password_validator weak_password_list.txt
    """
    parser = argparse.ArgumentParser(usage=usage)
    # TODO: handle multiple password list files
    parser.add_argument('weak_pw_list_paths', nargs=1, type=str)
    args = parser.parse_args(sys.argv[1:])
    print(args)
    print(args.weak_pw_list_paths)
    validate_passwords(sys.stdin, args.weak_pw_list_paths)



if __name__ == "__main__":
    main()
