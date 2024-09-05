import sys
import os
import xml.etree.ElementTree as ET
from PIL import ImageDraw, Image

#Helper function to grab all files in the input directory
def grabFiles(pathDir):
    filenames = []
    for file in os.listdir(pathDir):
        if file.endswith(".xml"):
            filenames.append(file)
    return filenames

#Helper function to draw rectangles around elements in the xml file
def drawRectangles(pathDir, file, rectangle_coords):
    #Take file name without xml extension and adding .png
    with Image.open(pathDir + file[:-4] + ".png") as img:
            draw = ImageDraw.Draw(img)
            for coords in rectangle_coords:
                print(f"Drawing rectangle: {coords}")
                draw.rectangle(xy=coords, outline="yellow", width=6)
            img.save("Annotated_PNGs/" + file[:-4] + "_annotated.png", "PNG")

def main():
    #Check to make sure correct amount of args were passed 
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_dir>")
        exit(1) #Exit with error code 1
    pathDir = sys.argv[1]

    #Grabbing and storing all file names from the input dir
    filenames = grabFiles(pathDir)

    #Parsing each file for the xml tree and then marking each element and highlighting the PNG files 
    #Output the annotated PNGs are stored in an Annotated_PNGs directory
    for file in filenames:
        try:
            #Trying to grab the tree of the xml file
            tree = ET.parse(pathDir + file)
        except:
            print("Error parsing file: " + file + " skipping file")
            #Keep going if there is an error parsing the file (fixed bug in apalon XML)
            continue

        root = tree.getroot()
        #Variable to store coordinates for drawing rectangle
        rectangle_coords = []
        #Marking nodes as leaf nodes, skip if it is not a leaf
        for neighbor in root.iter():
            leaf = True
            for _ in neighbor:
                leaf = False
                break
            if not leaf:
                continue
            
            #Setting bounds to draw rectangle around leaf elements 
            bounds = neighbor.attrib.get("bounds")
            if bounds is None:
                print("No bounds attribute found for this element, continuing...")
                continue
            
            bounds = bounds.replace('][', ',')
            bounds = eval(bounds)

            #Appending coordinates to draw rectangle
            rectangle_coords.append(bounds)

        #Drawing rectangles around elements 
        drawRectangles(pathDir, file, rectangle_coords)

    print("Annotated PNGs saved in Annotated_PNGs directory")
    

if __name__ == "__main__":
    main()  