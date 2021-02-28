import math
import stl
from stl import mesh
import numpy
import glob

def combine_stl():
'''This function combines all the STL file in a directory and merges them together
   Params: data_dir = stores the directory of stl files
   	   stl_dir = list all the stl files
	   data = total number of vertices and their value
	   combine = Combines all the stl files relative to their location as placed originally 
'''
	#storing all the stl file in a directory
	data_dir = "REPLACE WITH DIRECTORY OF THE STL FILES" #example "c:\users\username\..."
	stl_dir = 'data_dir/*.stl'

	#Creating an Empty mesh to concatenate all the stl file in a directory
	data = numpy.zeros(0, dtype=mesh.Mesh.dtype)
	combine = mesh.Mesh(data, remove_empty_areas=False)
	
	files = glob.glob(stl_dir)

	for fl in files:
		stl_fl = mesh.Mesh.from_file(fl)
  		combine = mesh.Mesh(numpy.concatenate([stl_fl.data, combine.data]))

	combine.save('combine.stl', mode=stl.Mode.ASCII)
