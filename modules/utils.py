import csv, os

def print_file_content(file):
    """Print contents of a file to stdout.

        :param file: str
            Name of file to print.
    """
    
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(str(row))
    
def write_list_to_file(output_file, lst):
    """Write a list of items to a file.

        :param output_file: str
            Name of file to save the list to.

        :param lst: List
            The list object to save.
    """
    
    with open(output_file, 'w') as f:
        for item in lst:
            f.write(item+'\n')
    
def read_file(input_file):
    """Print contents of a file line by line.

        :param input_file: str
            The file to read from.
    """
    
    with open(input_file, 'r') as f:
        return f.read().split('\n')
        
def get_file_names(folderpath, out="output.txt"):
    """Takes a path to a folder and writes all filenames
in the folder, to a specified output file.
    
        :param folderpath: str
            The folder which contents are going to be 
            written to the output file.
    
        :param out: str
            The file to write to. Defaults to 
            "output.txt" in the current directory.
            If the file exists, it will be overwritten,
            else it will be created.
    """
    
    file_name_list = [f+'\n' for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]
    with open(out, 'w') as file:
        file.writelines(file_name_list)
        
def get_all_file_names(folderpath, out="output.txt"):
    """Takes a path to a folder and writes all filenames
recursively including subfolders.

        :param folderpath: str
            The folder which contens are going to be
            written to the output file.
            
        :param out: str
            The file to write to. Defaults to
            "output.txt" in the current directory.
            If the file exists, it will be overwritten,
            else it will be created.
    """
    
    file_name_list = [os.path.join(os.path.abspath(dirpath), f)+'\n' for dirpath, dirnames, filenames in os.walk(folderpath) for f in filenames]
    with open(out, 'w') as file:
        file.writelines(file_name_list)
        
