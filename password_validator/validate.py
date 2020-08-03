PASSWORD_LEN_MIN = 8
PASSWORD_LEN_MAX = 64

def validate_passwords(pw_source_file, weak_pw_list_paths):
    """
        Assumes pw_source_file is new-line delimited file object
    """
    weak_pws = _load_weak_pws(weak_pw_list_paths)

    for line in pw_source_file:
        password = line.strip('\n')
        _validate_password(password, weak_pws)

def _validate_length(password):
    if len(password) < PASSWORD_LEN_MIN or len(password) > PASSWORD_LEN_MAX:
        return False, len(password)

    return True, None

def _validate_charset(password):
    to_print = list(password)
    valid = True
    for i, char in enumerate(password):
        char_code = str.encode(char)
        if int(char_code) > 127:
            valid = False
            to_print[i] = '*'
    
    if not valid:
        return False, to_print
    
    return True, None

def _validate_common_pw(common_pw_list, password):
    pass


def _validate_password(password, weak_pws):
    response = {}
    
    # check length
    valid_len, actual_len = _validate_length(password)
    if not valid_len:
        len_err_desc = 'Too Short' if actual_len < PASSWORD_LEN_MIN else 'Too Long'
        msg = '%s -> Error: %s' % (password, len_err_desc)
        return {
            'valid': False, 
            'msg': msg
        }
    # check charset
    valid_charset, pw_to_print = _valid_charset(password)
    if not valid_charset:
        return {
            'valid': False,
            'msg': '%s -> Error: Invalid Characters' % password
        }

    # check common password
    passed_common_pw_test = _validate_common_pw(weak_pws, password)
    if not passed_common_pw_test:
        return {
            'valid': False,
            'msg': '%s -> Error: Too Common' % password
        }

    pass