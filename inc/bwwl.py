# -*- coding: utf-8 -*-
from inc import func as fu
from inc import shared_code

# Name + Sprache (0 = DE, 1 = EN)
users = {
    'bwwl': 1,
    'sebipwned': 0,
    'edwardxelric': 0,
    'perlibug': 1,
    'Klozy': 0
}

# Hauptnutzer = erster Key
main_user = list(users.keys())[0]

def main():
    shared_code.run_main(users, main_user)
            
if __name__ == "__main__":
    fu.func()