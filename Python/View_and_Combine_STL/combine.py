import math
import stl
from stl import mesh
import numpy
import glob

def combine_stl(data_dir):
	#storing all the stl file in a directory 
	stl_dir = '/content/model/*.stl'

	#Creating an Empty mesh to concatenate all the stl file in a directory
	data = numpy.zeros(0, dtype=mesh.Mesh.dtype)
	combine = mesh.Mesh(data, remove_empty_areas=False)
	
	files = glob.glob(stl_dir)

	for fl in files:
  	stl_fl = mesh.Mesh.from_file(fl)
  	combine = mesh.Mesh(numpy.concatenate([stl_fl.data, combine.data]))

	combine.save('combine.stl', mode=stl.Mode.ASCII)