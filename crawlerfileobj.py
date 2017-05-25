import os

#TODO -> Create a classs for file functions
class FileHandler:
    'First version of the file handler class'
    def __init__(self):
        'File/Crawler class constructor. Every new instance has its own copy'
        self.filename = ""      #+ filename
        self.counter = 0        #+ initially used to track how many files was created
        self.i = 0              #+ loop variable
        self.possible_link = []     #+ Will be used by page_crawler to add links to list
        self.relative_link_list = []        #+ relative link
        self.final_link_list = []           #+ finished product
        self.duplicates = 0	 #+ number of duplicated links
        self.bad_links = 0	 #+ ...# of bad links
        self.good_links = 0	#+... and good links
        self.base_url = ""	#+ base url we are crawling
        self.links_in_file = 0	#+ total number of links successfully written to file
        self.relative_link = ""
        self.temp_relative_link = ""
        self.use_relative_link = False
        self.link_counter = 0

    #+ Redefined to open one file at a time (instead of multiple)
    def create_file(self, args):
        self.filename = args
        if self.file_exist(str(args)):
            print("\t\t" + args + " already exist. Continue...")
            pass
        else:
            print("Opening / Creating file(s) ...:", args)
            try:
                open(str(args), 'w+')
                print("\t\t" + args + " Opened / Created Successfully")
            except:
                print("Error Opening / Creating file.")

    def delete_file(self, *args):
        self.counter = 0
        self.i = 0
        for _ in args:
            self.counter += 1
        if self.counter == 0:	#+ nothing to delete
            pass
        else:
            while self.i != self.counter:
                try:
                    os.remove(args[self.i])
                    print("File Removed: ", args[self.i])
                except FileNotFoundError as msg:
                    print(str(msg))
                self.i += 1  # + Eventually, self.i == self.counter

    #+ TODO -> implement FILE_EXSIT() method
    """
    ...for now (this version tho), all this function does is checks if
       a file already exist (in the CWD), displays a friendly message
       of the status and either return true of false.
    
    ...Next version of this function will have the added ability to create files 'arg'
       if it does not already exist and return multiple values to it's caller
            
    Function name: file_exist() : bool
               
    """
    def file_exist(self, arg):
        if os.path.isfile(arg):
            return True
        else:
            return False

    #+ Write data to file (in this case, filename[0...n-1] == valid links)
    def write_to_file(self):
        if self.file_exist(str(self.filename)):      #+ File exist. All good !!!
            if len(self.possible_link) == 0:     #+ no link(s)
                print("Crawler got no link!!!. No need writing to file.")
                pass
            else:
                # + DEBUG
                print(self.filename + " was found in the CWD. Opening and writing data...")
                fHandle = open(str(self.filename), 'w+')
                self.possible_link = list(set(self.possible_link))       #+ first attempt to remove duplicates
                for x in self.possible_link:
                    self.links_in_file += 1
                    fHandle.write(x + "\n")
                fHandle.close()
        else:
            #+ File does not already exit.
            pass
