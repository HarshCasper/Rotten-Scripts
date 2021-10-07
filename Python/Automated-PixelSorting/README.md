## Automated Pixel Sorting :

### Description :
- Pixel sorting images using the [Pixelsort](https://github.com/satyarth/pixelsort) library.
- Running the code randomly generates 'N' number of images.
- Everything, from count and choice of paramters to the values they hold, is randomly generated.

### Try it out yourself :
- Install the Pixelsort library using : ```pip install pixelsort```
- The few paramters that are to be passed through the terminal are :
    * Image Name with extension : ```-i image.ext```  [png or jpg]
    * Number of outputs to be generated : ```-n 10```  [any number]
- To try it out, place your image in the "images" folder.
- Run the script from the terminal : ```python autosort.py -i image.jpg -n 5```
- The parameters and their values for each instance on each run are printed out in your terminal.
- The results can be found in the "generated" folder which gets empty at each fresh run.

### Sample Results :
![Sample Results](https://i.imgur.com/Bhxz1pX.png)
