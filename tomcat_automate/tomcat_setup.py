#!/usr/bin/env python3

# The module wide `IMPORT` section
# Make all necessary imports here
import subprocess
import os
import shutil

# Install Java via the Ubuntu Package Manager
def install_java():
    try:
        subprocess.check_call('sudo apt-get install default-jdk', shell=True)
    except subprocess.CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

# Download the Tomcat Binary Distribution
def download_tomcat():
    try:
        subprocess.check_call('wget http://redrockdigimark.com/apachemirror/tomcat/tomcat-7/v7.0.73/bin/apache-tomcat-7.0.73.tar.gz', shell=True)
    except subprocess.CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

    print('Tomcat Binary Downloaded!!!\n\n')

# Perform Untaring operation of the Tomcat Binary
def untar(fname):
    if fname.endswith("tar.gz"):
        tar = tarfile.open(fname)
        tar.extractall()
        tar.close()
        print("Extracted `%s` in Current Directory!!!\n\n" % fname)
    else:
        print("Not a `tar.gz` file: `%s`...\n\n" % fname)

# Move the extracted Tomcat package to `/opt/tomcat/`
def move_tomcat_binary():
    if not os.path.isdir('/opt/tomcat/'):
        os.chdir('/opt/')
        os.mkdir('tomcat')
        os.chdir('/home/vagrant/downloads/tomcat_download')

    shutil.move('./apache-tomcat-7.0.73', '/opt/tomcat/')

# Set the Environment Variables for JAVA and TOMCAT_BASE
def configure_bashrc():
    with open('/home/vagrant/.bashrc', 'a') as bashrc_file:
        bashrc_file.write('\n')
        bashrc_file.write('export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-i386\n')
        bashrc_file.write('export CATALINA_HOME=/opt/tomcat\n')

# Start the Tomcat Application Server
def run_tomcat():
    try:
        subprocess.check_call('$CATALINA_HOME/bin/startup.sh', shell=True)
    except subprocess.CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

if __name__ == '__main__':
    # Perform the Operations in a sequential manner
    install_java()
    download_tomcat()
    untar('apache-tomcat-7.0.73')
    move_tomcat_binary()
    configure_bashrc()

    # Reload Bash Profile to reflect the Environment Variable changes
    try:
        subprocess.check_call('sudo source /home/vagrant/.bashrc')
    except subprocess.CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

    # Start tomcat instance
    run_tomcat()
