
from organizer import *
organizer = Organizer()
print("Downloads Folder Cleaner")
print(30*"-")
print("Searching for downloads folder")
print("Is %s path to Downloads Folder?" %organizer.pathname)
if input("y/n: ") != "y":
    organizer.pathname = input("Specify your folder path: ")
    print(organizer.pathname)

print("Scanning for files...")
organizer.fileContainers()
print("Making folders..")
organizer.makeFolders()
print("Moving files to folders..")
organizer.moveToFolders(organizer.archives, "archives")
organizer.moveToFolders(organizer.images, "images")
organizer.moveToFolders(organizer.movies, "movies")
organizer.moveToFolders(organizer.documents, "documents")
print("Done, moved %s files" %organizer.movedfilescount)
