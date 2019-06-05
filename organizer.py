#!/usr/bin/env python3
from platform import system
from pathlib import Path
from glob import glob
import os
import shutil
class Organizer:

    def __init__(self):
        self.systemversion = system() 
        self.pathname = self.downloadsFolder() 
        self.folderlist = ["archives", "images", "movies", "documents", "misc"]
        self.movedfilescount = 0

    def downloadsFolder(self):
        homepath = str(Path.home())
        homepath += "/Downloads/"
        return homepath

    def makeFolders(self):
        for folder in self.folderlist:
            try:
                os.mkdir(self.pathname + folder)
            except FileExistsError:
                pass

    def fileContainers(self):
        self.archives = self.scanFiles("archives")
        self.images = self.scanFiles("images")
        self.movies = self.scanFiles("movies")
        self.documents = self.scanFiles("documents")

    def scanFiles(self, filetype):
        with open("./extensions/%s" %filetype, "r") as file:
            self.files = file.read()
            self.files = self.files.split(",")
            self.files.pop()
        filelist = []
        for extension in self.files:
            downloadspath = self.pathname
            downloadspath += extension
            filelist += glob(downloadspath)
        return filelist


    def moveToFolders(self, filetype, foldername):
        for f in filetype:
            shutil.move(f, self.pathname + foldername + "/")
            self.movedfilescount += 1
        pass



