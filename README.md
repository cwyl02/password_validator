# password_validator - A CLI tool

password_validator is a CLI tool that validates your input of passwords(from STDIN in newline delimited format) against the following requirements per NIST guidelines:

* 8 character minimum
* 64 character maximum
* All characters must be ASC-II characters
* Not a common password

# Prerequisites

 1. python3.6+ is in your $PATH
 2  you have a common password text file, delimited by newline. [Here is one example.](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)
 3. (Optional) you have installed git

# Installation
My the debian 9 in my chromebook doesn't let me run setuptools probably due to it's not a full-blown OS. So, we only have poor man's version now. 😂 

For now

	# substitute ~ with whatever path you want to put this project to
    cd ~
    git clone https://github.com/cwyl02/password_validator.git

Or go to [releases page](https://github.com/cwyl02/password_validator/releases) and download the zip file and unpack it to the location you like.

TODO: make it available through pip

# Usage

    # Linux environment
    cd password_validator
    cat passwords.txt | ./password_validator/main.py <PATH_TO_COMMON_PASSWORD_FILE>

    # Windows environment
    # TODO

# Run Testcases

    cd passwod_validator 
    python3 -mv unittest -v tests.test_validate
