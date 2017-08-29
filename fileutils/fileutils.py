import os

WORD_DELIM = " "

def grep(search, filename, name=False, line=False):

    """ This module is similar to grep in UNIX. It searches a string in a file and
        returns all the lines that search string contains. We can specify filename
        and linenumber if we want them in the grep results
    """

    matches = []
    count = 0
    file = filename+":" if name else ""
    lstr = ""
    with open(filename, "r") as fin:
        for l in fin:
            count += 1
            if search in l:
                if line:
                    lstr = str(count)
                misc = file + lstr + WORD_DELIM
                matches.append(misc + l)
    fin.close()
    return matches

def listfiles(path):
    """ This module lists all the files under the given directory. It recursively goes
        through all the directories under the given directory and returns a list
    """
    files = []
    __list_dir__(path, files)
    return files
    
def __list_dir__(path,files):
    """ Don't call this function directory. Its acts as a support function for "listfiles"
    """
    l = os.listdir(path)
    for i in l:
        fp = os.path.join(path,i)
        if(os.path.isdir(fp)):
            __list_dir__(fp,files);
        else:
            files.append(fp)
