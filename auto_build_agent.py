#!/usr/bin/env python3

# Author       : Dipankar Achinta -> dipankar.achinta@supervalu.com
# Build Version: 0.1.0
# Timeline     : October, 2016 - November, 2016

'''
   Summary:
   
           *  The purpose of the `agent` is to automate the entire Apache HTTPD
              server build.
           *  The process includes automating the entire dependency builds,
              required for compiling and installing Apache HTTPD web server.
           *  The HTTPD server installation requires APR* (Apache Portable Run-
              time) and PCRE (PERL Compatible Regular Expressions) library,
              to be built, compiled and installed first.
           *  Each of the dependent task has been given a seperate namespace,
              and the entire build is supervised by the `Agent` Process.
'''

# Module Import Section
# Don't clutter the entire script with imports
# Make all imports here and here only
import subprocess
import tarfile
import os

# Configuration Options
WGET = {
        'apr_uri'     : 'wget http://mirror.fibergrid.in/apache//apr/apr-1.5.2.tar.bz2',
        'apr_util_uri': 'wget http://mirror.fibergrid.in/apache//apr/apr-util-1.5.4.tar.bz2',
        'httpd_uri'   : 'wget http://mirror.fibergrid.in/apache//httpd/httpd-2.4.23.tar.bz2'
       }

# Function Definition for downloading Apache HTTPD build dependencies
def download_apr():
    try:
        subprocess.check_call(WGET['apr_uri'], shell=True)
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

    print('APR downloaded!!!')

def download_apr_util():
    try:
        subprocess.check_call(WGET['apr_util_uri'], shell=True)
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

    print('APR-UTIL downloaded!!!')

# Function Definition for downloading Apache HTTPD source tree
def download_httpd():
    try:
        subprocess.check_call(WGET['httpd_uri'], shell=True)
    except CalledProccessError as CPEErr:
        print('ERROR::', CPEErr)

    print('HTTPD downloaded!!!')



# Function Definition for untaring of compressed tar files
def untar(fname):
    if fname.endswith("tar.bz2"):
        tar = tarfile.open(fname)
        tar.extractall()
        tar.close()
        print("Extracted `%s` in Current Directory!!!\n" % fname)
    else:
        print("Not a `tar.bz2` file: '%s'..." % fname)

def install_pcre():
    try:
        subprocess.check_call('sudo apt-get install libpcre3 libpcre3-dev', shell=True)
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

    print('PCRE Installed!!!\n\n')

# Tar file list
tar_packages = ['apr-1.5.2.tar.bz2', 'apr-util-1.5.4.tar.bz2', 'httpd-2.4.23.tar.bz2']

# Download the compressed tar packages first
download_apr()
download_apr_util()
download_httpd()

# Decompress and untar the packages
for compressed_tar in tar_packages:
    untar(compressed_tar)

# Building APR and APR-UTIL for Apache HTTPD Installation
BASE_DIR = '/home/vagrant/downloads/apache_download/'

# Initiate PCRE Installation
# Delegate it to Ubuntu's default Package Manager
# install_pcre()

os.chdir(BASE_DIR + 'apr-1.5.2')
print('Changed to APR source directory\nRunning APR steps\n')
try:
    subprocess.check_call('sudo ./configure', shell=True)
    subprocess.check_call('sudo make', shell=True)
    subprocess.check_call('sudo make install', shell=True)
except CalledProcessError as CPEErr:
    print('ERROR::', CPEErr)

print('APR Installed!!!\n')

os.chdir(BASE_DIR + 'apr-util-1.5.4')
print('Changed to APR-UTIL source directory\nRunning APR-UTIL steps\n')
try:
    subprocess.check_call('sudo ./configure --with-apr=/usr/local/apr', shell=True)
    subprocess.check_call('sudo make', shell=True)
    subprocess.check_call('sudo make install', shell=True)
except CalledProcessError as CPEErr:
    print('ERROR::', CPEErr)

print('APR-UTIL Installed!!!\n')

os.chdir(BASE_DIR + 'httpd-2.4.23')
print('Changed to HTTPD source directory\nRunning HTTPD steps\n')
try:
    subprocess.check_call('sudo ./configure --enable-ssl --enable-so', shell=True)
    subprocess.check_call('sudo make', shell=True)
    subprocess.check_call('sudo make install', shell=True)
    # p = Popen(['sudo', 'make', 'install'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)    
    # grep_stdout = p.communicate(input=b'y\n')[0]
except CalledProcessError as CPEErr:
    print('ERROR::', CPEErr)

print('HTTPD Installed!!!\n')
