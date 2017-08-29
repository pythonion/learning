WORD_DELIM = " "


def grep(search, filename, name=False, line=False):
    matches = ""
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
                matches += misc + l
    fin.close()
    print(matches)
    return matches
