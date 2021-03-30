# View and Combine STL

STL files are an important part of 3D asset creation and management. STL files provide us with basic maps of 3D objects created/edited in applications like Blender/Maya/Unreal/Unity

STL are mainly used to create 3D maps of environments like cityscapes and heightmaps of terrain. 

## Running the Script
* Initialize and start a Virtual Environment
* Install the Packages by running the command: `pip install -r requirements.txt`
* Running `Combine.py` will combine all the STL files present in the drectory referred to.
* Running `View.py` will let you view the any STL file in a 3D PyPlot Space.

## Exploring STL and 3D renders
STL is a file format that was introduced with CAD or AutoCAD and has become extremely popular when it comes to the transport and scale representation of 3D renders between softwares. STL allows 1:1 scale representation between different 3D render solutions and used extensively is CGI and Animation. 

STL is the earliest representation of Vector based Mesh designs that revolutionized how 3D space and objects interacted with each other. To read and understand more about STL you can go [here](https://en.wikipedia.org/wiki/STL_(file_format))
This [Link](https://www.youtube.com/watch?v=ji8-3rr10lM) also might be handy if you want to understand the purpose of STL.

## Running and Understanding how the script works

Firstly you would need STL files before you can run the script. To get those I would suggest [City Generator](https://probabletrain.itch.io/city-generator), which is a website that uses tensor fields to generate a 3D map, all are created procedurally and this would be a great place if you want to explore STL and basic 3D enviroments.
When ever you open the website a city is pre-rendered for you, and you can download all the related STL files and proceed to running the script.

**Remember:** When you use City Generator, kindly delete or store the domain.stl file before running the combine.py script as it will result in the creation of flat mesh with no volume.

The scripts make it easier to view and combine STL files on the go with one click with the need of heavy 3D render engines, sometimes which can cost a lot.

```python
#in combine.py remember to replace the directory
data_dir = "REPLACE WITH DIRECTORY OF THE STL FILES" #example "c:\users\username\..."
```
```python
#in view.py remember to replace the directory
file_dir = "REPLACE WITH THE LOCATION OF THE FILE" #example "c:\users\username\..."
```

**Running** 

``` $python3 view.py```

``` $python3 combine.py```


Further you can use [Blender](https://www.blender.org/) which is one of the most amazing and Open Source 3D asset and animation creation tool out there.


![STL Buildings](https://imgur.com/0kUJV5f.png)
![STL Buildings Py](https://imgur.com/XWux4Q3.png)
![STL Paths](https://imgur.com/X98x8sl.png)
![STL Paths Py](https://imgur.com/Ezjrv2M.png)
