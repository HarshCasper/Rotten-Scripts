from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def view_stl(file_dir):
'''The following function renders a 3D geometry mesh in Matplotlib, if helps you visualize a 3D object in a simple and fast way''''
	figure = pyplot.figure(figsize=(30,30))
	axes = mplot3d.Axes3D(figure)

	view_mesh = mesh.Mesh.from_file(file_dir)
	axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))
	
	#Here we calculated the total number of flat vertices, that are present in a 3D object and then scale it according to the total Figsize of the plot
	#Autoscale allows us to fit the object within the constraints of a PyPlot Graph, and also fixes the object at 0,0,0 coordinates which 
	#can help us understand the true dimensions of the object in inches
	scale = view_mesh.points.flatten()
	axes.auto_scale_xyz(scale, scale, scale)

	pyplot.show()
