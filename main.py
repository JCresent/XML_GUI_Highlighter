import sys
import os
import xml.etree.ElementTree as ET
import PIL


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

    #Parsing each file for the xml tree and then marking each element and highlighting the PNG files 
    # Output the annotated PNGs are stored in an Annotated_PNGs directory
    for file in filenames:

        try:
            #Trying to grab the tree of the xml file
            tree = ET.parse(pathDir + file)
        except:
            print("Error parsing file: " + file)
            continue
        root = tree.getroot()
    

if __name__ == "__main__":
    main()  