# import required modules
from ppadb.client import Client
from PIL import Image
import pytesseract
import copy
from sudoku import solve, print_board

# connect to local adb server
adb = Client()
devices = adb.devices()
if len(devices) == 0:
	print("No devices attached")
	quit()
device = devices[0]

# save a screenshot & load it using PIL
result = device.screencap()
with open("screen.png", "wb") as fp:
    fp.write(result)
im = Image.open("screen.png")

# starting position of the grid on screen
x, y = 3, 285

# width & height of single cell
dx, dy = 112, 114

# grid contains the incomplete sudoku (9x9 matrix)
# touch is also a 9x9 matrix where each element is a tuple containing pixel coordinate
grid, touch = [], []

for j in range(1,10):
	grid_row, t_row = [], []
	xcopy = x

	for i in range(1,10):
		# crop & zoom into individual cells
		imcrop = im.crop((x,y,x+dx,y+dy)).crop((16,13,98,104))

		t_row.append( ((2*x+dx)//2, (2*y+dy)//2) )

		# every third vertical line is thicker
		x += 11 if i%3==0 else 7
		
		# extract the number from a cell
		temp = pytesseract.image_to_string(imcrop, config='--psm 10')
		temp = int(temp[0]) if temp[0].isnumeric() else 0
		
		grid_row.append(temp)
		x += dx
	x = xcopy

	# every third horizontal divider is thicker
	y += dy + (12 if j%3==0 else 8)

	grid.append(grid_row)
	touch.append(t_row)

# solve & print the board
orig_grid = copy.deepcopy(grid)
solve(grid)
print_board(grid)

def click(i, j):
	device.shell(f'input touchscreen tap {touch[i][j][0]} {touch[i][j][1]}')

def select(n):
	arr = [123, 212, 314, 410, 515, 623, 724, 839, 937]
	device.shell(f'input touchscreen tap {arr[n-1]} 1453')

# update values on screen
for i in range(len(grid)):
	for j in range(len(grid[0])):
		# only click on cells that were empty initially
		if (orig_grid[i][j] == 0):
			select(grid[i][j])
			click(i, j)