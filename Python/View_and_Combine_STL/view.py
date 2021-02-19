from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

def view_stl(file_dir):
	figure = pyplot.figure(figsize=(30,30))
	axes = mplot3d.Axes3D(figure)

	view_mesh = mesh.Mesh.from_file(file_dir)
	axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

	scale = view_mesh.points.flatten()
	axes.auto_scale_xyz(scale, scale, scale)

	pyplot.show()