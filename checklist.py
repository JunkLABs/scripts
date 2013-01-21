'''
checklist.py

This script takes a directory path as an argument, searches it recursively, and outputs the files in a PlainTasks 
checklist, except for folder and files that start with a period. If I can ever figure out the magic of encoding 
I'll add the checkbox, but for now it uses a *. Yes this requires Python 3. If you can't use 3 just change the print 
functions, but you really should be using 3.
'''

import os, sys, locale

if sys.version_info < (3, 0): # Checks the Python version
    raise "You must use Python 3 or change the script."

try:
    rootdir = sys.argv[1].rstrip() #Expects an argument, strips whitespace from it.
except IndexError:
    print("This script requires a path to run on.")

def checklist(rootdir):
    filenames = []
    outfileName = os.path.join(rootdir, "checklist.tasks") #Creates the output file in the directory

    print("Folders searched:") #Python 2 = print "Folders searched:"

    for root, subFolders, files in os.walk(rootdir):
        with open(outfileName, 'w') as fileOut:
            fileOut.write("Replace the * with checkboxes. Remember, the script excludes folders \
                            and files that start with a period. \n")

            for folder in subFolders:
                if folder.find('.') != -1 or root.find('.') != -1: #Checks if the folder name has a period, drops it if so.
                    subFolders.remove(folder)
                    print("Ignoring %s." % (folder))
                else:
                    print("Checking %s." % os.path.join(root, folder))  #Python 2 = print os.path.join(root, folder)

            for filename in files:
                if filename[0] == '.': #Checks if the file name starts with a period, drops it if so.
                    files.remove(filename)
                else:
                    filenames.append(os.path.join(root, filename))

            for filename in filenames:
                short_filename = filename[len(rootdir):] #Shortens the output, don't need the entire directory on every line.
                fileOut.write(chr(9744) + " %s \n" % short_filename) #If everything check out, this writes it to the file.

    print("Completed. The output file is %s" % outfileName) #Python 2 = print "Completed. The output file is " + outfileName

checklist(rootdir)