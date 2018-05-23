import os, shutil

def main():
    print("Starting directory is: {}".format(os.getcwd()))
    directory = os.chdir('FilesToSort')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    folder_name = ''
    folder_name_dict = {}
    for filename in os.listdir('.'):
        head, sep, tail = filename.partition(".")

        folder_name = input("What category would you like to sort {} files into?".format(tail))
        if folder_name not in folder_name_dict:
            folder_name_dict[folder_name] = tail
            os.mkdir(folder_name)
            shutil.move(filename, folder_name)
            os.listdir('.')

        else:
            shutil.move(filename, folder_name)

main()

