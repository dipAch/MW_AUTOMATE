#!/usr/bin/env python3

import subprocess
import os
import shutil

def install_java():
    try:
        subprocess.check_call('sudo apt-get install default-jdk', shell=True)
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

def download_tomcat():
    try:
        subprocess.check_call('wget http://redrockdigimark.com/apachemirror/tomcat/tomcat-7/v7.0.73/bin/apache-tomcat-7.0.73.tar.gz', shell=True)
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

    print('Tomcat Binary Downloaded!!!')

def untar(fname):
    if fname.endwith("tar.gz"):
        tar = tarfile.open(fname)
        tar.extractall()
        tar.close()
        print("Extracted `%s` in Current Directory!!!\n" % fname)
    else:
        print("Not a `tar.gz` file: `%s`..." % fname)

def move_tomcat_binary():
    if not os.path.isdir('/opt/tomcat/'):
        os.chdir('/opt/')
        os.mkdir('tomcat')
        os.chdir('/home/vagrant/downloads/tomcat_download')

    shutil.move('./apache-tomcat-7.0.73', '/opt/tomcat/')

def configure_bashrc():
    with open('/home/vagrant/.bashrc') as bashrc_file:
        bashrc_file.write()
        bashrc_file.write('export JAVA_HOME=/usr/lib/jvm/default-java')
        bashrc_file.write('export CATALINA_HOME=/opt/tomcat')

def run_tomcat():
    try:
        subprocess.check_call('$CATALINA_HOME/bin/startup.sh', shell=True)
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

if __name__ == '__main__':
    # Perform the Operations one after another
    install_java()
    download_tomcat()
    untar()
    move_tomcat_binary()
    configure_bashrc()

    # Reload Bash Profile to reflect Environment Variable changes
    try:
        subprocess.check_call('sudo source /home/vagrant/.bashrc')
    except CalledProcessError as CPEErr:
        print('ERROR::', CPEErr)

    # Start tomcat instance
    run_tomcat()
