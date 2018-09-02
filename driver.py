import logging
import os
import spacy
nlp = spacy.load('en')
#Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def create_knowledge_graph(contents_of_input_file, name_of_input_file):
    # Through this function you have to use the contents of each file to create a knowledge graph
    # The output has to be saved in the data/output folder with the same name as data/input file
    # Note the writing to file has to be handled by you.
    c = []
    k = read_directory(name_of_input_file)
    r = k.split('.\n')
    for l in r:
        b = []
        doc = nlp(l)
        for nc in doc.noun_chunks:
            b.append(nc.text)
        b.append(l.split(b[0]+ ' ')[1].split(' '+b[1])[0])
        c.append(b)
    for i in range():
        if c[][2] not in j:
            j.append(c[][2])
        elif c[][2] in j:
            continue

    
    g =[]
    f =[]
    g.append(c[0][1])
    f.append(c[0][0])
    for i in range(len(c)-1):
        if c[0][0] in c[i+1][0] or c[0][0] in c[i+1][1]:
            g.append(c[i+1][0])
            c.remove(c[i+1])
        if c[0][1] in c[i+1][0] or c[0][0] in c[i+1][1]:
            f.append(c[i+1][0])
            c.remove(c[i+1])
    for i in range(len(c)-1):
        if c[i][0] in g:
            f.append(c[i][1])
            c.remove(c[i])
        if c[i][1] in f:
            g.append(c[i][0])
            remove(c[i])
    
    for i in range(len(g)):
        print(f[i] + j[0] + g[i])
    for i in range(len(g)-1):
        print(f[i] + j[1] + f[0])
    for i in range(len(g)-1):
        print(g[i] + j[1] + g[0])
    pass
#Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    #Folder where the input files are present
    mypath = "data//input"
    list_of_input_files = read_directory(mypath)
    logging.debug(list_of_input_files)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath,each_file), "r") as f:
            file_contents = f.read()

            create_knowledge_graph(file_contents, each_file)
            # end of code
