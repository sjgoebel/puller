#!/usr/pyenv/shims/python
#usage:  ./puller.py -b <branch_slug> -u <github_username> -p <github_password>

import sys
import optparse
import pexpect
import subprocess
import time
import os

def get_projects():
    if not os.path.isdir("/home/ubuntu/studentwork/"):
        print("Make a directory called 'studentwork' in your workspace.")
        return

    parser = optparse.OptionParser()
    parser.add_option('-b', '--branch', dest='branch', help="assignment slug")


    (options, args) = parser.parse_args()

    if options.branch is None:
        options.branch = input('Assignment Slug:')

    foldername = input("What should I call the folder?")

    #Load Names

    try:
        file = open("names.txt", "r")
    except:
        print("No file names.txt")
        return

    #make the assignment folder.  If it already exists, make a new one with today's date appended.
    subprocess.call("mkdir /home/ubuntu/studentwork/" + foldername, shell=True)


    people = file.readlines()
    for person in people:
        (studentname, githubname) = person.split(",")
        githubname += ".git"
        #git clone the folder.
        githuburl = "git@github.com:me50/" + githubname
        destinationurl = "/home/ubuntu/studentwork/" + foldername + "/" + studentname
        pexpecter = pexpect.spawn("git clone -b " + options.branch + " " + githuburl + " " + destinationurl)
        pexpecter.wait()

get_projects()








