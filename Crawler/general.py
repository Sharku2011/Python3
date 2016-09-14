import os

#Create Project directory folder if it does not exist.
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project '{}'".format(directory))
        os.makedirs(directory)

#Create queue and crawled files if does not exist.
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

#Create a new data file.
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
#Add data onto an existing file.
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
#Delete the contents of a file
def delete_file_contents(path):
    with open(path, 'a') as file:
        pass
        
#Read a file and convert each line to set items
def file_to_set(filename):
    results = set()
    with open(filename, 'rt') as file:
        for line in file:
            results.add(line.replace('\n',''))
        return results
    
#Iterate through a set, each item will be a new line in the new file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)