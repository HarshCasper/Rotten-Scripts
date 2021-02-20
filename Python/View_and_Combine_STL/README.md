# View and Combine STL

STL files are an important part of 3D asset creation and management. STL files provide us with basic maps of 3D objects created/edited in applications like Blender/Unreal/Unity

STL are mainly used to create 3D maps of environments like cityscapes and heightmaps of terrain. 

## Running the Script
* Initialize and start a Virtual Environment
* Install the Packages by running the command: pip install -r requirements.txt
* You can use combine.py to concatenate multiple STL files(recommended for assets designed in same 3D space or domain)
* Or you can simply run view.py to view the STL file in a pyplot env.(set the target size to your liking)

## Exploring the STL Space
[City Generator](https://probabletrain.itch.io/city-generator) is a website that uses tensor fields to generate a 3D map, all are created procedurally and this would be a great space if you want to explore STL and basic 3D enviroments.

When you use City Generator, kindly delete or store the domain.stl file before running the combine.py script as it will result in the creation of flat mesh instead of a 3D one.

Further you can use [Blender](https://www.blender.org/) which is one of the most amazing and Open Source 3D asset and animation creation tool out there.

![3D Cityscape in paint3D](https://github.com/HarshCasper/Rotten-Scripts/blob/master/Python/View_and_Combine_STL/images/building_3d.png)
![STL View in Python](https://github.com/HarshCasper/Rotten-Scripts/blob/master/Python/View_and_Combine_STL/images/building_py_view.png)

![Road 3D](https://github.com/HarshCasper/Rotten-Scripts/blob/master/Python/View_and_Combine_STL/images/road_3d.PNG)
![Road Py View](https://github.com/HarshCasper/Rotten-Scripts/blob/master/Python/View_and_Combine_STL/images/road_py_view.PNG)
