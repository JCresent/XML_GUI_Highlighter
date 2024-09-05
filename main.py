import sys
import os

def main():
    #Check to make sure correct amount of args were passed 
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_dir>")
        exit(1)

    pathDir = sys.argv[1]
    filenames = []
    for file in os.listdir(pathDir):
        if file.endswith(".xml"):
            filenames.append(file)
    #print(filenames)
    


if __name__ == "__main__":
    main()  