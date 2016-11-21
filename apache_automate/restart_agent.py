#!/usr/bin/env/ python3

import subprocess

def perform_restart():
    try:    
        subprocess.check_call('sudo service apache2 restart', shell=True)
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

if __name__ == '__main__':
    perform_restart()
