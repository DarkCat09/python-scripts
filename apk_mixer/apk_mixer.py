# encoding: utf-8
# https://habr.com/ru/post/422885/
import re
import codecs
import os 
from os import listdir
import shutil
import subprocess
import datetime

pwd = os.getenv("PWD", os.getcwd())
apkFolder1=pwd+"/tmp/1"
apkFolder2=pwd+"/tmp/2"
logfile = open(pwd + "apk_mixer.log", 'wb')

try:
    print("Decompiling " + pwd + "/apk/1.apk ...")
    result = subprocess.run("java -jar " + pwd + "/tools/apktool.jar d " + pwd + "/apk/1.apk -f -o " + pwd + "/tmp/1", \
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    if (result.returncode == 0):
        print("OK\n")
    else:
        print("Error")
        logfile.write(result.stdout)
        print("View log for details\n")
        raise Exception("Error happenned while mixing apks")

    print("Decompiling " + pwd + "/apk/2.apk ...")
    result = subprocess.run("java -jar " + pwd + "/tools/apktool.jar d " + pwd + "/apk/2.apk -f -o " + pwd + "/tmp/2", \
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    if (result.returncode == 0):
        print("OK\n")
    else:
        print("Error")
        logfile.write(result.stdout)
        print("View log for details\n")
        raise Exception("Error happenned while mixing apks")

    print("Creating new manifest ...")
    mainfest1 = open(apkFolder1 + "/AndroidManifest.xml", "r").read()
    service1 = mainfest1[(mainfest1.find("</activity>") + len("</activity>")):mainfest1.find("</application>")]
    permission1 = mainfest1[mainfest1.find("<uses-permission"):mainfest1.find("<application ")]
    mainfest2 = open(apkFolder2 + "/AndroidManifest.xml", "r").read()

    new_mainfest2 = mainfest2[0:mainfest2.find("<application")] + permission1 + mainfest2[mainfest2.find("<application"):mainfest2.find("</application")] + \
                    service1 + mainfest2[mainfest2.find("</application>"):mainfest2.find("</manifest>") + len("</manifest>")]
    new_mainfest = open(apkFolder2+"/AndroidManifest.xml", "w")
    new_mainfest.write(new_mainfest2)
    new_mainfest.close()
    print("OK\n")

    print("Copying Smali and Unknown files ...")
    subprocess.call("cp -r " + apkFolder1 + "/smali " + apkFolder2, shell=True)
    subprocess.call("cp -r " + apkFolder1 + "/unknown " + apkFolder2, shell=True)
    ##if (result.returncode == 0):
    ##    print("OK\n")
    ##else:
    ##    print("Error")
    ##    logfile.write(result.stdout)
    ##    print("View log for details\n")
    ##    raise Exception("Error happenned while mixing apks")

    print("Compiling APK to " + pwd + "/tmp/3.apk ...")
    result = subprocess.run("java -jar " + pwd + "/tools/apktool.jar b " + pwd + "/tmp/2 -o " + pwd + "/tmp/3.apk", \
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    if (result.returncode == 0):
        print("OK\n")
    else:
        print("Error")
        logfile.write(result.stdout)
        print("View log for details\n")
        raise Exception("Error happenned while mixing apks")

    print("Signing file " + pwd + "/tmp/3.apk ...")
    subprocess.call("java -jar " + pwd + "/tools/testsign.jar " + pwd + "/tmp/3.apk --override", \
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    if (result.returncode == 0):
        print("OK\n")
    else:
        print("Error")
        logfile.write(result.stdout)
        print("View log for details\n")
        raise Exception("Error happenned while mixing apks")
finally:
    logfile.close()
    input("")
    quit()
