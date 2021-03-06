import os

PASSWORD_LEN_MIN = 8
PASSWORD_LEN_MAX = 64

def validate_passwords(pw_source_file, weak_pw_list_path):
    """
        Assumes pw_source_file is new-line delimited file object
    """
    weak_pws = load_weak_pws(weak_pw_list_path)

    for line in pw_source_file:
        password = line.strip('\n')
        response = validate_password(password, weak_pws)
        if not response['valid']:
            print(response['msg'])


def load_weak_pws(weak_pw_file_list_path):
    weak_pws = set()
    # TODO: check file size vs. available space in RAM
    with open(weak_pw_file_list_path, 'r') as f:
        for line in f:
            weak_pws.add(line.strip('\n'))
    
    return weak_pws


def validate_length(password):
    if len(password) < PASSWORD_LEN_MIN or len(password) > PASSWORD_LEN_MAX:
        return False, len(password)

    return True, None


def validate_charset(password):
    to_print = list(password)
    valid = True
    for i, char in enumerate(password):
        char_code = ord(char)
        if int(char_code) > 127:
            valid = False
            to_print[i] = '*'

    if not valid:
        return False, ''.join(to_print)

    return True, None


def validate_common_pw(common_pw_set, password):
    if password in common_pw_set:
        return False

    return True


def validate_password(password, common_pws):
    response = {}
    
    # check length
    valid_len, actual_len = validate_length(password)
    if not valid_len:
        len_err_desc = 'Too Short' if actual_len < PASSWORD_LEN_MIN else 'Too Long'
        msg = '%s -> Error: %s' % (password, len_err_desc)
        return {
            'valid': False, 
            'msg': msg
        }
    # check charset
    valid_charset, pw_to_print = validate_charset(password)
    if not valid_charset:
        return {
            'valid': False,
            'msg': '%s -> Error: Invalid Characters' % pw_to_print
        }

    # check common password
    passed_common_pw_test = validate_common_pw(common_pws, password)
    if not passed_common_pw_test:
        return {
            'valid': False,
            'msg': '%s -> Error: Too Common' % password
        }

    return {
        'valid': True
    }