'''
FindFileType.py
Copyright 2013 Wohlfe
Licensed under the WTFPLv2

Find file types by extension and size on a local volume or mapped drive. Requires Python 3 and access to the folders/files.

I'll be OOP-ing this shortly.
'''

import os
import sys

if sys.version_info < (3, 0): 
    raise "You must use Python 3 or change the script." #Checks the Python version

try:
    rootdir = sys.argv[1].rstrip() #Expects an argument, strips whitespace from it.
except IndexError:
    sys.exit("This script requires a path to run on.") #Exits if no path is given.

def file_type_search(dir):
    output_filename = "C:\Temp\FileTypeSearch.txt" #Log file
    extensions = ('.exe', '.vmdk', '.pst', '.mp3') #Extensions to be searched for
    large_extensions = ('.zip', '.txt', '.rar', '.doc', '.xls', '.docx', '.xlsx', '.jpg', '.png', '.ppt', '.pptx') #Extensions to be searched for only if bigger than size_limit
    size_limit = 100000000 #Size limit for large_extensions in bytes, default 100MB
    filenames = []

    for r, d, f in os.walk(rootdir):
            for files in f:
                try:
                    if files.endswith(extensions):
                        filenames.append(os.path.join(r, files)) #Adds files with extensions being searched for

                    elif files.endswith(large_extensions) and os.path.getsize(os.path.join(r, files)) >= size_limit:
                        filenames.append(os.path.join(r, files)) #Adds files with extensions being searched for only if bigger than size_limit

                    #elif os.path.getsize(os.path.join(r, files)) >= size_limit:
                        #filenames.append(os.path.join(r, files)) #Optional check for all file types if bigger than size_limit, disabled by default

                except OSError as err:
                    print("Access Denied: ", err) #Catches OS errors for locked files
    
    filenames_sorted = sorted(set(filenames)) 

    with open(output_filename, 'w') as file_out:
        for filename in filenames_sorted:
            short_filename = filename[len(rootdir):] #Shortens the output, don't need the entire directory on every line.

            try:
                file_out.write(short_filename + '\n') #If everything check out, this writes it to the file.
            
            except UnicodeEncodeError:
                file_out.write(short_filename.encode('ascii', 'ignore') + '\n') #Catches Unicode errors caused by files with names Windows can't handle

    file_out.close() #Flushes the buffer to the file

    print("Completed. The output file is ", output_filename)

file_type_search(rootdir)