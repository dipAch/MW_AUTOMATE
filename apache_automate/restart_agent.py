#!/usr/bin/env/ python3
# Author: Dipankar Achinta, [dipankar.achinta@supervalu.com]

# This is the module wide `IMPORT` Section
# Make all necessary imports here
# Don't clutter the entire module with imports here and there
import subprocess
import os
import sys

HTTPD_BIN = '/usr/local/apache2/bin/'

# The function to perform `HTTPD` restart
# This function is to be invoked, to change the state of `HTTPD`
# Usage: python3 restart_agent.py [ start | stop | restart ]
def perform_httpd_restart(control_cmd='restart'):
    supported_cmd = ['start', 'restart', 'stop']
    if control_cmd not in supported_cmd:
        control_cmd = 'restart'
    try:    
        os.chdir(HTTPD_BIN)
        subprocess.check_call(('sudo ./apachectl -k %s' % control_cmd), shell=True)
    except subprocess.CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        perform_httpd_restart(sys.argv[1])
    else:
        perform_httpd_restart()
