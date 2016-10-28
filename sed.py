def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    
    f_in = open(source, 'r')
    f_out = open(dest, 'w')

    for line in f_in:
        new_line = line.replace(pattern, replace)
        f_out.write(new_line)

    f_in.close()            #make sure you close the file
    f_out.close()
    






def main():
    pattern = 'Hey Jude'
    replace = 'Hi Jerry'
    source = 'sed_tester.txt'
    dest = 'new_' + source
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()