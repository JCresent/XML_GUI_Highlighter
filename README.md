# GUI Highlighter

A tool to search Android application screenshots by parsing and processing metadata (in the form of xml files) that describes the hierarchical screen structure then highlighting these leaf level GUI-components.


## Usage 
Run this command from the terminal
``` 
python main.py .\Programming-Assignment-Data
```
or wherever the directory is stored with your XMLs and PNGs. 

## Description 
In this project, the ElementTree and PIL libraries were used to implement XML parsing and to draw on images. The ElementTree library made it simple to run through the XML files and identify correct leaf elements to highlight. The PIL library, specifically the Image and ImageDraw functions, made it seamless to annotate the images and draw the yellow rectangles around elements.  

Helper functions were also used to make separation of tasks more apparent. One was created to parse the directory and store the files in a list, while the other was  made to draw the rectangles given input path, file and coordinates for the box. 
