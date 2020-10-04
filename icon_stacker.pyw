#!/usr/bin/env python
# Filename : icon_stacker.py

__version__ = "1.0"


#-----Statement of Authorship----------------------------------------#
#
# This is an individual assessment item. By submitting this
# code I agree that it represents my own work. I am aware of
# the University rule that a student must not act in a manner
# which constitutes academic dishonesty as stated and explained
# in QUT's Manual of Policies and Procedures, Section C/5.3
# "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#	Student no: n9099816
#	Student name: Michael Bedford
#
# NB: Files submitted without a completed copy of this statement
# will not be marked. All files submitted will be subjected to
# software plagiarism analysis using the MoSS system
# (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#

#-----Task Description-----------------------------------------------#
#
# ICON STACKING
#
# This task tests your skills at defining functions, processing
# data stored in lists and performing the arithmetic calculations
# necessary to display a complex visual image. The incomplete
# Python script below is missing a crucial function, "draw_icons".
# You are required to complete this function so that when the
# program is run it produces an image of multiple icons packed into
# a rectangular frame, using data stored in a list to determine the
# positions and orientations of the icons. See the instruction
# sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#

#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the grid. You should not change any of
# the code in this section.
#

# Import the functions needed to complete this task. You should
# not need to import any other modules for your solution.

from turtle import *

# Define constant values used in the main program that sets up
# the drawing window. Do not change any of these values.

frame_width = 900 # The width of the grid frame in pixels
frame_height = 600 # The height of the grid frame in pixels
margin = 100 # Size of the margin around the frame in pixels
window_height = frame_height + margin
window_width = frame_width + 2 * margin
num_columns = 6 # Number of columns in the grid frame
num_rows = 4 # Number of rows in the grid frame
square_width = int(frame_width / num_columns) # Width of each square
square_height = int(frame_height / num_rows) # Height of each square

#--------------------------------------------------------------------#

#-----Functions for Drawing the Grid---------------------------------#
#
# The functions in this section are called by the main program to
# draw the grid. You should not change any of the code in this
# section. Note that each of these functions leaves the pen up.


def draw_frame(frame_on=True):
	"""Draw the the rectangular frame that contains all the icons"""

	# Only draw the rectangle if the argument is True
	if frame_on:

		penup()
		# Start at the bottom-left
		goto(int(-frame_width / 2), int(-frame_height / 2))
		pendown()

		setheading(90) # Face north
		forward(frame_height)

		right(90) # Face east
		forward(frame_width)

		right(90) # Face south
		forward(frame_height)

		right(90) # Face west
		forward(frame_width)

		penup()


def draw_squares(squares_on=True):
	"""Draw the individual squares in the grid"""

	# Only draw the squares if the argument is True
	if squares_on:

		dot_size = 3 # The size of the dots, in pixels
		dot_gap = 15 # Separation of dots, in pixels

		# Setup for loop ranges
		r1 = (int(-(frame_width / 2 - square_width)),
			int(frame_width / 2), square_width)

		r2 = (int(-frame_height / 2 + dot_gap),
			int(frame_height / 2), dot_gap)

		r3 = (int(-(frame_height / 2 - square_height)),
			int(frame_height / 2), square_height)

		r4 = (int(-frame_width / 2 + dot_gap),
			int(frame_width / 2), dot_gap)

		penup() # Don't draw connecting lines
		color("yellow")

		# Draw dotted vertical grid lines
		for x_coord in range(*r1):
			# Draw a dotted vertical line
			for point in range(*r2):
				goto(x_coord, point)
				dot(dot_size)

		# Draw dotted horizontal grid lines
		for y_coord in range(*r3):
			# Draw a dotted horizontal line
			for point in range(*r4):
				goto(point, y_coord)
				dot(dot_size)

		# Draw a black dot in the exact centre of the grid
		# to mark the "home" coordinate
		color("black")
		home()
		dot(dot_size)


def draw_labels(labels_on=True):
	"""Draw the numeric x-y labels"""

	# Only draw the labels if the argument is True
	if labels_on:

		label_gap = 15 # Separation of labels from the frame, in pixels
		font_size = 16 # Size of characters for the labels

		penup() # Don't draw connecting lines

		# Draw the x axis labels
		goto(
			int(-(frame_width - square_width) / 2),
			int(-(frame_height / 2 + label_gap + font_size))
			)
		setheading(0) # Face east

		for x_label in range(num_columns):
			write(
				str(x_label), align="center", font=("Arial", font_size, "bold")
				)

			forward(square_width)

		# Draw the y axis labels
		goto(
			int(-(frame_width / 2 + label_gap)),
			int(-(frame_height - square_height) / 2)
			)
		setheading(90) # Face north

		for y_label in range(num_rows):
			write(
				str(y_label), align="center", font=("Arial", font_size, "bold")
				)

			forward(square_width)


#--------------------------------------------------------------------#

#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list containing the specifications
# for the position and orientation of several icons to display
# in the grid. Each data set element specifies how to display
# one icon using four values:
#
#	[icon_style, bottom_left_column, bottom_left_row, orientation]
#
# There are four icon styles, named 'A', 'B', 'C' and 'D'. The
# icons each have different x-y sizes, expressed in grid squares:
#
#	A - 1x1
#	B - 1x2
#	C - 2x2
#	D - 2x3
#
# The column and row coordinates say in which grid square to place
# the bottom-left corner of the icon (taking into consideration its
# orientation). The orientation specifies the direction in which
# the top of the icon should point, 'N', 'S', 'E' or 'W'. For
# instance, an icon pointing North should appear upright, whereas
# the same icon pointing South should appear upside-down.

# The following data set doesn't specify drawing any icons at
# all. You may find it useful as a dummy argument when you
# first start developing your "draw_icons" function.

data_set_00 = [
	["A", 0, 0, "N"], ["B", 1, 0, "N"], ["C", 2, 0, "N"], ["D", 4, 0, "N"]]

# The following data sets each draw just one of the icons but with
# different orientations. You can use them to test your icon drawing
# code individually. (There are two data sets for the 2x3 icon D
# because it's too big to fit in the frame in all four orientations.)

data_set_01 = [
	["A", 1, 0, "N"], ["A", 2, 1, "E"], ["A", 3, 2, "S"], ["A", 4, 3, "W"]
	]

data_set_02 = [
	["B", 2, 0, "W"], ["B", 2, 3, "E"], ["B", 1, 1, "N"], ["B", 4, 1, "S"]
	]

data_set_03 = [
	["C", 0, 0, "N"], ["C", 1, 2, "E"], ["C", 3, 0, "S"], ["C", 4, 2, "W"]
	]

data_set_04a = [
	["D", 0, 0, "N"], ["D", 2, 2, "E"], ["D", 3, 0, "W"]
	]

data_set_04b = [
	["D", 0, 2, "E"], ["D", 1, 0, "W"], ["D", 4, 1, "S"]
	]

# The next group of data sets completely fill the grid with icons of
# different types and orientations. You will need to have all of your
# icon drawing code working to use them. If your code is working
# correctly using any of these data sets will completely fill the
# frame with non-overlapping icons.

# All four icons, arranged symmetrically, all upright (pointing North)
data_set_05 = [
	["A", 0, 2, "N"], ["A", 0, 3, "N"], ["A", 2, 0, "N"], ["A", 3, 0, "N"],
	["A", 5, 2, "N"], ["A", 5, 3, "N"], ["B", 1, 2, "N"], ["B", 4, 2, "N"],
	["C", 0, 0, "N"], ["C", 4, 0, "N"], ["D", 2, 1, "N"]
	]

# All four icons, asymmetric arrangement, all upright (pointing North)
data_set_06 = [
	["A", 1, 3, "N"], ["A", 2, 3, "N"], ["A", 3, 1, "N"], ["A", 3, 0, "N"],
	["A", 5, 2, "N"], ["A", 5, 3, "N"], ["B", 0, 0, "N"], ["B", 0, 2, "N"],
	["C", 3, 2, "N"], ["C", 4, 0, "N"], ["D", 1, 0, "N"]
	]

# The same as above but with all icons upside down (pointing South)
data_set_07 = [
	["A", 1, 3, "S"], ["A", 2, 3, "S"], ["A", 3, 1, "S"], ["A", 3, 0, "S"],
	["A", 5, 2, "S"], ["A", 5, 3, "S"], ["B", 0, 0, "S"], ["B", 0, 2, "S"],
	["C", 3, 2, "S"], ["C", 4, 0, "S"], ["D", 1, 0, "S"]
	]

# All four icons in different orientations
data_set_08 = [
	["A", 5, 0, "N"], ["A", 5, 1, "S"], ["A", 5, 2, "E"], ["A", 5, 3, "W"],
	["B", 2, 0, "S"], ["B", 3, 0, "E"], ["C", 0, 0, "W"], ["D", 0, 2, "E"],
	["D", 3, 1, "N"]
	]

# Another arrangement with all four icons in different orientations
data_set_09 = [
	["A", 0, 0, "E"], ["A", 0, 1, "N"], ["A", 1, 3, "S"], ["A", 2, 3, "W"],
	["B", 0, 2, "N"], ["B", 5, 2, "S"], ["B", 5, 0, "N"], ["C", 3, 0, "N"],
	["C", 3, 2, "E"], ["D", 1, 0, "S"]
	]

# Yet another arrangement with all four icons in different orientations
data_set_10 = [
	["A", 0, 0, "E"], ["A", 0, 1, "N"], ["A", 2, 2, "S"], ["A", 2, 3, "W"],
	["B", 0, 3, "E"], ["B", 0, 2, "W"], ["B", 5, 2, "N"], ["C", 1, 0, "N"],
	["C", 3, 2, "E"], ["D", 3, 0, "W"]
	]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#--------------------------------------------------------------------#

#   /$$$$$$            /$$             /$$     /$$
#  /$$__  $$          | $$            | $$    |__/
# | $$  \__/  /$$$$$$ | $$ /$$   /$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$
# |  $$$$$$  /$$__  $$| $$| $$  | $$|_  $$_/  | $$ /$$__  $$| $$__  $$
#  \____  $$| $$  \ $$| $$| $$  | $$  | $$    | $$| $$  \ $$| $$  \ $$
#  /$$  \ $$| $$  | $$| $$| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$
# |  $$$$$$/|  $$$$$$/| $$|  $$$$$$/  |  $$$$/| $$|  $$$$$$/| $$  | $$
#  \______/  \______/ |__/ \______/    \___/  |__/ \______/ |__/  |__/

#--------------------------------------------------------------------#

# Each Icon design has been made by registering a list of vertices
# as a turtle shape. The shapes can then be called and stamped to screen.
# Turtle supports the ability to rotate the shapes before stamping.

# The hierarchy of the data structures is thusly:
# Vertex -> Polygon -> Aspect -> Design -> Icon

# Each Vertex is a tuple of an 'x' and 'y' coordinate.
# A tuple of Vertices defines a Polygon\Turtle Shape.
# Combining multiple Shapes of like pen settings, forms an Aspect.
# A list of Aspects constitutes a Design.
# An Icon draws its image from the Design pool based on passed parameters.

# I've used three classes to store this information. Though, if I could
# import the collections module, I'd replace the Polygon class with a
# namedtuple (among several other things).


class Polygon(object):
	"""A simple class for a storing a polygon.

	Keyword arguments:
	name -- string which the polygon will be registered as
	vertices -- array of coordinates forming a polygon
	"""

	def __init__(self, name, vertices):
		self.name = name
		self.vertices = vertices


class Aspect(object):
	"""Registers and stores multiple shapes of like pen settings.

	Keyword arguments:
	polygons -- accepts an array of Polygons of like pen settings
	pencolor -- array of rgb integers defining a shape's outline color
	fillcolor -- array of rgb integers defining a shape's fill color
	pensize -- takes an integer as a pixel width for the shape's outline
	"""

	colors = {"black": (0, 0, 0), "white": (255, 255, 255)}

	def __init__(
		self,
		polygons,
		pencolor=None,
		fillcolor=None,
		pensize=1
		):

		self.pencolor = pencolor if pencolor else Aspect.colors["black"]
		self.fillcolor = fillcolor if fillcolor else Aspect.colors["white"]
		self.pensize = pensize
		self.shape_names = Aspect.register_shapes(polygons)

	@staticmethod
	def register_shapes(polygons):
		"""Registers polygons as turtle shapes."""

		shape_names = []
		for polygon in polygons:
			register_shape(polygon.name, polygon.vertices)
			shape_names.append(polygon.name)

		return shape_names


class Icon(object):
	"""Stores an icon's parameters and processes draw calls.

	style -- string key to call designs, added to the class's design pool
	column -- set column index, integer
	row -- set row index, integer
	orientation -- takes a cartesian abbreviation for rotating the design
	"""

	# Static class variable to store designs and their style key.
	designs = {}

	# Convenient dict. Converts compass directions to angles. Can be extended.
	rotate = {"N": 0, "E": 270, "S": 180, "W": 90}

	def __init__(self, style, column, row, orientation):
		self.design = Icon.designs[style][0]
		self.size = Icon.designs[style][1]
		self.column = column
		self.row = row
		self.orientation = orientation

		# Scale not cleanly implemented, but not important to task
		try:
			self._scale_factor = Icon.designs[style][2]
		except IndexError:
			self._scale_factor = 1000

		self._scale_ratio = float(square_width) / self._scale_factor

	@property
	def angle(self):
		"""Converts Cardinal direction into Degree angle."""
		return Icon.rotate[self.orientation]

	@property
	def col_offset(self):
		"""Corrects the column to account for icon rotation."""
		if self.orientation in "S":
			return self.size[0]
		elif self.orientation in "W":
			return self.size[1]
		else:
			return 0

	@property
	def row_offset(self):
		"""Corrects the row to account for icon rotation."""
		if self.orientation in "E":
			return self.size[0]
		elif self.orientation in "S":
			return self.size[1]
		else:
			return 0

	@property
	def start_pos(self):
		"""Returns the pixel coordinates of the row & column."""
		x = -(frame_width / 2) +(self.column + self.col_offset) * square_width
		y = -(frame_height / 2) +(self.row + self.row_offset) * square_height
		return x, y

	def draw(self):
		"""Draws the icon to the screen, then restores turtle settings."""

		# Save turtle's settings.
		_color = color()
		_color_mode = colormode()
		_pen_down = isdown()

		# Move into position and prep turtle.
		penup()
		colormode(255)
		goto(self.start_pos)
		setheading(90)
		settiltangle(self.angle)
		shapesize(self._scale_ratio, self._scale_ratio)

		# Cycle through the design's aspects..
		for aspect in self.design:
			pen(pencolor=aspect.pencolor,
				fillcolor=aspect.fillcolor,
				outline=aspect.pensize)

			# ..and stamp all of its shapes to screen.
			for shape_name in aspect.shape_names:
				shape(shape_name)
				stamp()

		# Restore turtle's settings.
		colormode(_color_mode)
		pen(pendown=True if _pen_down else False,
			pensize=1,
			pencolor=_color[0],
			fillcolor=_color[1])
		shape("arrow")
		shapesize(1, 1)
		settiltangle(0)
		home()


def setup_design_a():
	"""Style A, Meta Knight (1x1)"""

	size = (1, 1)
	scale = 150

	Aspect.colors["meta_collar"] = (45, 138, 162)
	Aspect.colors["meta_collar_light"] = (133, 200, 200)
	Aspect.colors["meta_knight"] = (45, 70, 140)
	Aspect.colors["meta_mantle"] = (65, 50, 53)
	Aspect.colors["meta_mantle_light"] = (120, 92, 120)
	Aspect.colors["meta_gild"] = (230, 160, 30)
	Aspect.colors["meta_gild_outline"] = (187, 115, 13)
	Aspect.colors["meta_black"] = (20, 20, 45)
	Aspect.colors["meta_eyes"] = (240, 200, 40)
	Aspect.colors["meta_mask"] = (170, 200, 240)
	Aspect.colors["meta_mask_shadow"] = (140, 128, 165)
	Aspect.colors["meta_eye_slot"] = (95, 110, 145)
	Aspect.colors["meta_cape"] = (15, 20, 65)
	Aspect.colors["meta_cape_light"] = (12, 48, 132)

	meta_collar = Aspect(
		pencolor=Aspect.colors["meta_collar"],
		fillcolor=Aspect.colors["meta_collar"],
		pensize=3,
		polygons=[

		Polygon("meta_collar",
			((30,106), (24,117), (24,120), (28,118), (31,117), (34,117),
			(37,119), (44,127), (52,134), (64,138), (75,139), (86,138),
			(98,134), (106,127), (113,119), (116,117), (119,117), (122,118),
			(126,120), (126,117), (120,106))
			)
		])

	meta_collar_light = Aspect(
		pencolor=Aspect.colors["meta_collar_light"],
		fillcolor=Aspect.colors["meta_collar_light"],
		polygons=[

		Polygon("meta_collar_light",
			((43,122), (38,117), (34,115), (31,116), (31,117), (34,117),
			(37,119), (44,127), (52,134), (64,138), (75,139), (86,138),
			(98,134), (107,125), (103,112), (55,116), (63,127), (73,137),
			(65,136), (55,133), (49,129))
			)
		])

	meta_knight = Aspect(
		fillcolor=Aspect.colors["meta_knight"],
		polygons=[

		Polygon("meta_knight",
			((75,120), (66,119), (50,114), (41,108), (37,104), (37,96),
			(113,96), (113,104), (109,108), (100,114), (84,119))
			)
		])

	meta_mantle = Aspect(
		pencolor=Aspect.colors["meta_mantle"],
		fillcolor=Aspect.colors["meta_mantle"],
		polygons=[

		Polygon("meta_mantle_L",
			((24,85), (17,93), (12,100), (9,109), (8,117), (9,125), (13,119),
			(17,114), (19,113), (27,112), (34,109), (39,105), (42,99),
			(42,93), (38,85), (31,83))
			),

		Polygon("meta_mantle_R",
			((126,85), (133,93), (138,100), (141,109), (142,117), (141,125),
			(137,119), (133,114), (131,113), (123,112), (116,109), (111,105),
			(108,99), (108,93), (112,85), (119,83))
			)
		])

	meta_mantle_light = Aspect(
		pencolor=Aspect.colors["meta_mantle"],
		fillcolor=Aspect.colors["meta_mantle_light"],
		polygons=[

		Polygon("meta_mantle_light_L",
			((30,89), (22,94), (17,99), (12,106), (11,111), (12,116),
			(13,117), (17,114), (19,113), (27,112), (34,109), (39,105),
			(42,99), (38,88), (34,88))
			),

		Polygon("meta_mantle_light_R",
			((131,103), (132,106), (129,108), (125,109), (120,109), (116,109),
			(111,105), (108,99), (117,85))
			)
		])

	meta_gild = Aspect(
		pencolor=Aspect.colors["meta_gild_outline"],
		fillcolor=Aspect.colors["meta_gild"],
		polygons=[

		Polygon("meta_gild_L",
			((24,85), (17,93), (12,100), (9,109), (8,117), (9,125), (9,128),
			(7,129), (4,124), (3,119), (3,111), (5,102), (10,94), (16,86),
			(23,81), (28,79), (31,83))
			),

		Polygon("meta_gild_R",
			((126,85), (133,93), (138,100), (141,109), (142,117), (141,125),
			(141,128), (143,129), (146,124), (147,119), (147,111), (145,102),
			(140,94), (134,86), (127,81), (122,79), (119,83))
			)
		])

	meta_black = Aspect(
		fillcolor=Aspect.colors["meta_black"],
		polygons=[

		Polygon("meta_black",
			((111,72), (103,90), (75,80), (47,90), (39,72), (75,53))
			)
		])

	meta_eyes = Aspect(
		pencolor=Aspect.colors["meta_black"],
		fillcolor=Aspect.colors["meta_eyes"],
		polygons=[

		Polygon("meta_eyes",
			((95,90), (96,83), (96,74), (94,69), (92,66), (90,66), (88,69),
			(86,74), (86,79), (86,84), (64,84), (64,79), (64,74), (62,69),
			(60,66), (58,66), (56,69), (54,74), (54,83), (55,90))
			)
		])

	meta_mask = Aspect(
		pencolor=Aspect.colors["meta_mask_shadow"],
		fillcolor=Aspect.colors["meta_mask"],
		polygons=[

		Polygon("meta_mask_L",
			((75,114), (66,113), (54,109), (44,101), (36,90), (33,79),
			(35,67), (75,46), (75,58), (69,59), (56,65), (43,74), (49,88),
			(75,77))
			),

		Polygon("meta_mask_R",
			((75,114), (84,113), (96,109), (106,101), (114,90), (117,79),
			(115,67), (75,46), (75,58), (81,59), (94,65), (107,74), (101,88),
			(75,77))
			)
		])

	meta_mask_shadow = Aspect(
		pencolor=Aspect.colors["meta_mask_shadow"],
		fillcolor=Aspect.colors["meta_mask_shadow"],
		polygons=[

		Polygon("meta_mask_shadow",
			((75,114), (66,113), (54,109), (44,101), (36,90), (33,79),
			(36,67), (39,87), (46,98), (56,106), (66,109), (69,108),
			(72,105), (75,100), (78,106), (81,110), (84,113))
			)
		])

	meta_eye_slot = Aspect(
		pencolor=Aspect.colors["meta_black"],
		fillcolor=Aspect.colors["meta_eye_slot"],
		polygons=[

		Polygon("meta_eye_slot",
			((75,55), (70,56), (51,66), (41,74), (46,88), (49,88), (43,74),
			(56,65), (69,59), (75,58), (81,59), (94,65), (107,74), (101,88),
			(104,88), (109,74), (99,66), (80,56), (75,55))
			)
		])

	meta_notch = Aspect(
		pencolor=Aspect.colors["meta_mask_shadow"],
		fillcolor=Aspect.colors["meta_mask"],
		polygons=[

		Polygon("meta_notch_1",
			((63,98), (62,102), (61,111), (59,113), (57,113), (56,111),
			(57,106), (60,101))
			),

		Polygon("meta_notch_2",
			((53,95), (49,97), (45,100), (44,102), (44,104), (47,104),
			(50,99))
			),

		Polygon("meta_notch_3",
			((87,98), (88,102), (89,111), (91,113), (93,113), (94,111),
			(93,106), (90,101))
			),

		Polygon("meta_notch_4",
			((97,95), (101,97), (105,100), (106,102), (106,104), (103,104),
				(100,99))
			)
		])

	meta_cape = Aspect(
		pencolor=Aspect.colors["meta_black"],
		fillcolor=Aspect.colors["meta_cape"],
		polygons=[

		Polygon("meta_cape",
			((11,8), (21,13), (28,20), (32,28), (27,37), (23,49), (21,60),
			(21,71), (23,78), (26,83), (28,85), (31,85), (34,78), (42,70),
			(54,61), (67,54), (74,51), (76,51), (83,54), (96,61), (106,72),
			(111,81), (116,85), (122,85), (124,83), (127,78), (129,71),
			(129,60), (127,49), (123,37), (118,28), (122,20), (129,13),
			(139,8))
			)
		])

	meta_cape_light = Aspect(
		pencolor=Aspect.colors["meta_cape"],
		fillcolor=Aspect.colors["meta_cape_light"],
		polygons=[

		Polygon("meta_cape_light",
			((31,74), (37,63), (47,53), (61,44), (77,36), (90,33), (103,34),
			(113,38), (118,44), (109,39), (99,36), (91,36), (84,38), (83,42),
			(90,43), (98,48), (118,63), (125,73), (116,64), (105,57), (93,51),
			(80,47), (78,48), (81,51), (89,54), (105,62), (122,74), (126,78),
			(128,71), (128,60), (126,49), (122,37), (117,28), (112,18),
			(111,15), (113,13), (118,14), (121,17), (121,20), (124,17),
			(129,12), (134,10), (122,9), (98,9), (86,10), (83,12), (96,13),
			(106,17), (113,24), (117,30), (104,24), (92,22), (77,23), (62,28),
			(51,34), (39,45), (32,56), (28,70), (28,76), (29,81), (41,69),
			(53,60), (73,50), (68,50), (61,53), (47,61))
			)
		])

	return (
		meta_collar, meta_collar_light, meta_knight, meta_mantle,
		meta_mantle_light, meta_gild, meta_black, meta_eyes, meta_mask,
		meta_mask_shadow, meta_eye_slot, meta_notch, meta_cape,
		meta_cape_light), size, scale


def setup_design_b():
	"""Style B, Charmander (1x2)"""

	size = (1, 2)

	Aspect.colors["char_pipe"] = (96, 48, 0)
	Aspect.colors["char_belly"] = (255, 200, 128)
	Aspect.colors["char_skin"] = (255, 155, 80)

	char_pipe = Aspect(
		fillcolor=Aspect.colors["char_pipe"],
		pensize=2,
		polygons=[

		Polygon("char_pipe",
			((703,1212), (839,1155), (839,1225), (902,1208), (967,1200),
			(961,1156), (934,1116), (902,1097), (841,1114), (689,1195),
			(689,1211))
			)
		])

	char_skin = Aspect(
		fillcolor=Aspect.colors["char_skin"],
		pensize=3,
		polygons=[

		Polygon("char_skin",
			((190,917), (191,895), (213,875), (190,782), (168,713), (144,687),
			(141,712), (127,690), (122,723), (101,711), (75,723), (108,748),
			(128,780), (69,819), (34,881), (67,967), (136,1084), (225,1180),
			(225,1214), (199,1261), (140,1520), (145,1691), (203,1830),
			(305,1887), (427,1920), (526,1900), (638,1836), (690,1758),
			(707,1694), (673,1619), (713,1551), (752,1513), (773,1459),
			(774,1339), (745,1271), (712,1229), (682,1206), (720,1173),
			(735,1093), (764,1057), (819,1048), (819,1072), (809,1108),
			(835,1101), (848,1070), (865,1086), (869,1123), (883,1103),
			(892,1078), (897,1095), (894,1127), (917,1096), (917,1063),
			(889,1028), (880,989), (828,934), (777,912), (717,907),
			(646,1118), (713,906), (754,762), (802,541), (799,404), (775,307),
			(735,265), (723,232), (751,223), (815,159), (817,125), (800,108),
			(735,110), (705,127), (604,128), (577,144), (564,175), (570,250),
			(592,286), (584,368), (542,405), (498,399), (428,402), (383,423),
			(362,405), (351,364), (385,180), (367,124), (337,83), (221,79),
			(171,85), (164,130), (204,184), (241,214), (194,265), (141,390),
			(134,540), (177,715), (238,945), (261,959), (242,958))
			)
		])

	char_belly = Aspect(
		fillcolor=Aspect.colors["char_belly"],
		pensize=2,
		polygons=[

		Polygon("char_belly",
			((377,1174), (400,1174), (449,1155), (490,1156), (541,1171),
			(570,1143), (633,989), (683,784), (684,664), (663,519), (617,439),
			(556,407), (449,399), (405,410), (370,450), (351,547), (344,671),
			(364,857), (416,1126), (427,1159), (400,1170))
			)
		])

	char_outlines = Aspect(
		fillcolor=Aspect.colors["black"],
		polygons=[

		Polygon("char_outline_1",
			((766,1692), (677,1688), (653,1682), (642,1666), (664,1665),
			(666,1637), (690,1592), (719,1548), (738,1537), (754,1540),
			(761,1615), (760,1661), (744,1682), (765,1685))
			),

		Polygon("char_outline_2",
			((307,1637), (337,1666), (408,1676), (435,1668), (453,1644),
			(449,1525), (435,1479), (407,1456), (341,1462), (322,1483),
			(306,1534))
			),

		Polygon("char_outline_3",
			((430,1677), (442,1677), (410,1762), (374,1789), (320,1790),
			(294,1780), (270,1760), (259,1743), (256,1728), (272,1729),
			(272,1738), (287,1758), (308,1772), (326,1777), (359,1779),
			(385,1763), (404,1742))
			),

		Polygon("char_outline_4",
			((571,1348), (571,1365), (586,1360), (603,1341), (608,1322),
			(592,1322), (591,1332), (581,1346))
			),

		Polygon("char_outline_5",
			((680,1358), (681,1329), (696,1327), (696,1340), (690,1340),
			(691,1358))
			),

		Polygon("char_outline_6",
			((690,1212), (640,1195), (598,1186), (517,1185), (442,1213),
			(360,1248), (308,1249), (361,1238), (437,1201), (512,1176),
			(607,1176), (644,1186))
			)
		])

	char_reflection = Aspect(
		pencolor=Aspect.colors["white"],
		polygons=[

		Polygon("char_reflection_L",
			((316,1623), (354,1646), (354,1589), (342,1569), (324,1556),
			(316,1563), (315,1582), (321,1589))
			),

		Polygon("char_reflection_R",
			((682,1670), (696,1670), (695,1647), (681,1631), (675,1651))
			)
		])

	return (
		char_pipe, char_skin, char_belly, char_outlines, char_reflection
		), size


def setup_design_c():
	"""Style C, Samus Aran (2x2)"""

	size = (2, 2)

	Aspect.colors["samus_outline"] = (228, 27, 35)
	Aspect.colors["samus_orange"] = (255, 150, 15)
	Aspect.colors["samus_tubes_outline"] = (40, 40, 40)
	Aspect.colors["samus_tubes"] = (60, 60, 60)
	Aspect.colors["samus_visor_outline"] = (200, 255, 0)
	Aspect.colors["samus_visor"] = (35, 190, 0)

	helmet_polygons = [
		Polygon("helmet",
			((1060,294), (1127,648), (1536,921), (1555,1142), (1580,1183),
			(1296,1140), (1296,1260), (1429,1354), (1429,1688), (1499,1629),
			(1574,1534), (1634,1423), (1676,1298), (1645,1261), (1620,1185),
			(1610,1091), (1619,972), (1627,1120), (1653,1230), (1683,1271),
			(1683,1250), (1849,1090), (1875,1011), (1886,898), (1874,772),
			(1838,665), (1782,631), (1763,596), (1697,535), (1567,440),
			(1574,485), (1568,538), (1540,591), (1501,631), (1451,667),
			(1623,788), (1676,797), (1709,844), (1740,871), (1766,880),
			(1788,871), (1802,856), (1813,839), (1808,860), (1791,883),
			(1767,893), (1739,884), (1707,856), (1669,804), (1624,798),
			(1444,675), (1428,655), (1419,631), (1191,508), (1089,180),
			(911,180), (809,508), (581,631), (572,655), (556,675), (376,798),
			(331,804), (293,856), (261,884), (233,893), (209,883), (192,860),
			(187,839), (198,856), (212,871), (234,880), (260,871), (291,844),
			(324,797), (377,788), (549,667), (499,631), (460,591), (432,538),
			(426,485), (433,440), (303,535), (237,596), (218,631), (162,665),
			(126,772), (114,898), (125,1011), (151,1090), (317,1250),
			(317,1271), (347,1230), (373,1120), (381,972), (390,1091),
			(380,1185), (355,1261), (324,1298), (366,1423), (426,1534),
			(501,1629), (571,1688), (571,1354), (704,1260), (704,1140),
			(420,1183), (445,1142), (464,921), (873,648), (940,294))
			),

		Polygon("helmet_top_L",
			((983,1827), (983,1212), (835,1212), (792,1127), (726,1137),
			(726,1271), (594,1364), (594,1705), (677,1755), (770,1793),
			(876,1818))
			),

		Polygon("helmet_top_R",
			((1015,1827), (1015,1212), (1163,1212), (1206,1127), (1272,1137),
			(1272,1271), (1404,1364), (1404,1705), (1321,1755), (1228,1793),
			(1122,1818))
			)
		]

	samus_helmet_outline = Aspect(
		pencolor=Aspect.colors["samus_outline"],
		fillcolor=Aspect.colors["samus_outline"],
		pensize=10,
		polygons=helmet_polygons)

	samus_helmet = Aspect(
		pencolor=Aspect.colors["samus_outline"],
		fillcolor=Aspect.colors["samus_orange"],
		polygons=helmet_polygons)

	samus_tubes = Aspect(
		pencolor=Aspect.colors["samus_tubes_outline"],
		fillcolor=Aspect.colors["samus_tubes"],
		pensize=2,
		polygons=[

		Polygon("tube_L",
			((542,612), (565,598), (608,540), (662,453), (730,382), (795,342),
			(847,332), (887,198), (825,187), (759,200), (693,234), (626,290),
			(565,364), (512,446), (466,490), (468,531), (482,566), (510,595))
			),

		Polygon("tube_R",
			((1458,612), (1435,598), (1392,540), (1338,453), (1270,382),
			(1205,342), (1153,332), (1113,198), (1175,187), (1241,200),
			(1307,234), (1374,290), (1435,364), (1488,446), (1534,490),
			(1532,531), (1518,566), (1490,595))
			),

		Polygon("mouth_1",
			((914,519), (1086,519), (1078,474), (922,474))
			),

		Polygon("mouth_2",
			((1076,463), (1069,421), (931,421), (924,463))
			),

		Polygon("mouth_3",
			((1067,411), (1060,367), (940,367), (933,411))
			),

		Polygon("mouth_4",
			((1058,357), (1050,310), (950,310), (942,357))
			)
		])

	samus_visor = Aspect(
		pencolor=Aspect.colors["samus_visor_outline"],
		fillcolor=Aspect.colors["samus_visor"],
		pensize=2,
		polygons=[

		Polygon("visor",
			((1082,547), (1100,668), (1246,749), (1509,928), (1523,1120),
			(1535,1155), (1190,1094), (1147,1184), (853,1184), (810,1094),
			(465,1155), (477,1120), (491,928), (754,749), (900,668),
			(918,547))
			)
		])

	samus_reflection = Aspect(
		pencolor=Aspect.colors["samus_visor_outline"],
		fillcolor=Aspect.colors["samus_visor_outline"],
		polygons=[

		Polygon("visor_reflection_1",
			((580,1135), (580,868), (591,860), (591,1133))
			),

		Polygon("visor_reflection_2",
			((624,1127), (683,1117), (683,798), (624,838))
			)
		])

	return (
		samus_helmet_outline, samus_tubes, samus_helmet, samus_visor,
		samus_reflection), size


def setup_design_d():
	"""Style D, Bowser Jr. (2x3)"""

	size = (2, 3)

	Aspect.colors["spikes"] = (232, 212, 160)
	Aspect.colors["shell"] = (55, 152, 103)
	Aspect.colors["hands"] = (243, 200, 70)
	Aspect.colors["clown"] = (230, 237, 240)
	Aspect.colors["teeth"] = (45, 45, 70)
	Aspect.colors["mouth"] = (105, 10, 23)
	Aspect.colors["tongue"] = (195, 43, 60)
	Aspect.colors["headband"] = (63, 43, 45)
	Aspect.colors["head"] = (132, 190, 83)
	Aspect.colors["clown_makeup"] = (225, 113, 52)
	Aspect.colors["cuffs"] = (142, 142, 137)
	Aspect.colors["cuffs_highlights"] = (175, 192, 185)
	Aspect.colors["hair"] = (230, 57, 50)

	spikes = Aspect(
		fillcolor=Aspect.colors["spikes"],
		pensize=3,
		polygons=[

		Polygon("spikes",
			((1622,1749), (1677,1812), (1702,1847), (1710,1866), (1698,1881),
			(1663,1906), (1520,1973), (1538,2125), (1539,2175), (1532,2189),
			(1515,2192), (1479,2188), (1376,2163), (824,2536), (764,2563),
			(733,2572), (720,2571), (714,2561), (707,2536), (691,2454))
			)
		])

	shell = Aspect(
		fillcolor=Aspect.colors["shell"],
		pensize=4,
		polygons=[

		Polygon("shell",
			((1175,2224), (1312,2224), (1398,2176), (1468,2129), (1531,2059),
			(1580,1977), (1614,1881), (1629,1795), (1625,1698), (1175,1698))
			)
		])

	arm = Aspect(
		fillcolor=Aspect.colors["hands"],
		pensize=3,
		polygons=[

		Polygon("arm",
			((449,2003), (615,2028), (668,1798), (537,1782), (443,1781))
			)
		])

	bib = Aspect(
		fillcolor=Aspect.colors["clown"],
		pensize=3,
		polygons=[

		Polygon("bib",
			((680,1705), (642,1826), (632,1894), (636,1947), (1224,2290),
			(1260,2349), (1315,2397), (1373,2417), (1428,2415), (1474,2395),
			(1455,2342), (1408,2266), (1372,2243), (1300,2215), (1377,2162),
			(1430,2106), (1482,2018), (1511,1931), (1526,1817), (1525,1724),
			(1078,1634))
			)
		])

	teeth = Aspect(
		pencolor=Aspect.colors["teeth"],
		fillcolor=Aspect.colors["teeth"],
		polygons=[

		Polygon("teeth",
			((748,1743), (782,1804), (835,1720), (874,1815), (958,1710),
			(985,1857), (1053,1737), (1070,1830), (1117,1785), (1110,1772),
			(1079,1805), (1058,1703), (989,1819), (961,1676), (878,1794),
			(833,1688), (783,1775), (755,1726))
			)
		])

	mouth = Aspect(
		pencolor=Aspect.colors["teeth"],
		fillcolor=Aspect.colors["mouth"],
		pensize=2,
		polygons=[

		Polygon("mouth",
			((742,1824), (735,1802), (734,1779), (740,1755), (757,1725),
			(1072,1716), (1089,1739), (1107,1776), (1114,1807), (1113,1832),
			(1102,1854), (1082,1874), (848,1785), (697,1935), (1063,2094),
			(1156,1893), (1166,1856), (1167,1818), (1160,1778), (1123,1698),
			(713,1724), (697,1758), (687,1790), (685,1818), (690,1843),
			(702,1865))
			)
		])

	tongue = Aspect(
		fillcolor=Aspect.colors["tongue"],
		pensize=3,
		polygons=[

		Polygon("tongue",
			((802,1851), (833,1889), (869,1921), (937,1960), (1007,1953),
			(1063,1933), (924,1784))
			)
		])

	hair = Aspect(
		fillcolor=Aspect.colors["hair"],
		pensize=4,
		polygons=[

		Polygon("hair",
			((990,2543), (1152,2586), (1201,2623), (1237,2669), (1259,2732),
			(1229,2735), (1194,2733), (1245,2770), (1283,2785), (1312,2793),
			(1302,2812), (1264,2837), (1207,2855), (1152,2860), (1101,2850),
			(1056,2834), (1065,2871), (1040,2867), (1001,2845), (966,2803),
			(946,2749), (946,2696))
			)
		])

	headband = Aspect(
		fillcolor=Aspect.colors["headband"],
		pensize=3,
		polygons=[

		Polygon("headband",
			((927,2568), (960,2632), (989,2630), (1033,2617), (1073,2594),
			(1105,2567), (1083,2523))
			)
		])

	head = Aspect(
		fillcolor=Aspect.colors["head"],
		pensize=3,
		polygons=[

		Polygon("head1",
			((1221,2287), (1203,2358), (1182,2412), (1095,2522), (1023,2558),
			(945,2571), (865,2562), (788,2535), (715,2484), (662,2406),
			(638,2343), (911,2184))
			),
		Polygon("head2",
			((1133,276), (1258,241), (1355,226), (1444,224), (1536,240),
			(1592,269), (1613,296), (1592,329), (1525,352), (1439,362),
			(824,367), (684,357), (613,331), (594,300), (607,278), (661,251),
			(738,235), (825,231), (911,240), (1040,270))
			),
		Polygon("head3",
			((999,345), (1015,259), (1028,230), (1049,201), (1078,189),
			(1108,200), (1131,227), (1146,267), (1158,345))
			)
		])

	horn = Aspect(
		fillcolor=Aspect.colors["spikes"],
		pensize=3,
		polygons=[

		Polygon("horn",
			((1106,2513), (1107,2498), (1128,2458), (1165,2426), (1180,2421),
			(1190,2431), (1204,2464), (1213,2501), (1210,2524), (1189,2529),
			(1150,2527), (1120,2519))
			)
		])

	tooth = Aspect(
		fillcolor=Aspect.colors["clown"],
		pensize=3,
		polygons=[

		Polygon("tooth",
			((874,1958), (937,1919), (961,1910), (971,1930), (983,2014))
			)
		])

	clown = Aspect(
		fillcolor=Aspect.colors["clown"],
		pensize=5,
		polygons=[

		Polygon("clown",
			((1936,1098), (1919,949), (1870,806), (1791,674), (1684,558),
			(1555,463), (1408,392), (1248,349), (1082,334), (916,349),
			(757,392), (610,463), (482,558), (377,674), (299,806), (252,949),
			(236,1098), (253,1247), (302,1390), (367,1524), (1795,1522),
			(1873,1390), (1920,1247))
			)
		])

	clown_makeup = Aspect(
		pencolor=Aspect.colors["clown_makeup"],
		fillcolor=Aspect.colors["clown_makeup"],
		polygons=[

		Polygon("clown_makeup1",
			((970,1166), (963,1154), (943,1144), (916,1141), (889,1144),
			(869,1154), (862,1166), (869,1179), (889,1189), (916,1192),
			(943,1189), (963,1179))
			),
		Polygon("clown_makeup2",
			((391,1175), (383,1165), (364,1159), (340,1160), (316,1167),
			(300,1178), (295,1190), (303,1201), (322,1206), (347,1206),
			(370,1199), (387,1188))
			),
		Polygon("clown_makeup3",
			((714,1169), (706,1158), (686,1151), (659,1149), (632,1153),
			(613,1162), (606,1174), (614,1185), (634,1192), (661,1194),
			(688,1190), (707,1181))
			),
		Polygon("clown_makeup4",
			((1352,1190), (1346,1176), (1327,1163), (1298,1156), (1269,1156),
			(1247,1163), (1237,1176), (1243,1190), (1263,1203), (1291,1210),
			(1321,1210), (1343,1203))
			)
		])

	clown_mouth = Aspect(
		fillcolor=Aspect.colors["clown_makeup"],
		pensize=4,
		polygons=[

		Polygon("clown_mouth",
			((534,884), (584,879), (634,851), (688,828), (768,811), (853,813),
			(926,828), (998,846), (1061,853), (1110,843), (1152,819),
			(1181,775), (1188,730), (1178,688), (1149,641), (1106,607),
			(1040,580), (951,562), (850,556), (751,559), (674,574), (599,600),
			(542,631), (497,668), (464,715), (447,755), (444,799), (461,838),
			(495,871))
			)
		])

	clown_opening = Aspect(
		fillcolor=Aspect.colors["head"],
		pensize=5,
		polygons=[

		Polygon("clown_opening",
			((302,1523), (377,1491), (528,1461), (740,1440), (1065,1428),
			(1383,1435), (1609,1459), (1772,1494), (1859,1524), (1870,1573),
			(1856,1714), (1832,1753), (1750,1739), (1525,1713), (1078,1695),
			(720,1707), (459,1730), (307,1753), (294,1698), (293,1569))
			)
		])

	hands = Aspect(
		fillcolor=Aspect.colors["hands"],
		pensize=3,
		polygons=[

		Polygon("hands1",
			((387,1769), (286,1758), (263,1762), (227,1745), (191,1741),
			(158,1754), (148,1776), (150,1796), (121,1804), (103,1825),
			(104,1852), (132,1890), (80,1900), (29,1921), (18,1937),
			(30,1957), (86,1987), (159,2012), (234,2026), (405,2016))
			),
		Polygon("hands2",
			((1341,2005), (1371,1987), (1392,1952), (1409,1882), (1413,1779),
			(1387,1601), (1396,1536), (1399,1482), (1397,1447), (1388,1419),
			(1336,1461), (1318,1407), (1307,1385), (1290,1375), (1273,1390),
			(1244,1451), (1195,1414), (1171,1406), (1159,1427), (1161,1510),
			(1100,1509), (1082,1515), (1087,1537), (1112,1580), (1142,1622),
			(1192,1823), (1219,1895), (1249,1956), (1286,1995), (1312,2006))
			)
		])

	cuffs = Aspect(
		fillcolor=Aspect.colors["cuffs"],
		pensize=3,
		polygons=[

		Polygon("cuffs1",
			((1118,1626), (1111,1646), (1163,1779), (1198,1795), (1241,1805),
			(1281,1805), (1327,1796), (1370,1778), (1411,1746), (1427,1725),
			(1424,1591), (1407,1572), (1386,1609), (1346,1637), (1302,1656),
			(1252,1667), (1203,1666), (1169,1653), (1148,1630), (1133,1620))
			),
		Polygon("cuffs2",
			((285,2033), (310,2045), (416,2041), (448,2033), (476,2008),
			(496,1966), (506,1921), (505,1870), (492,1813), (466,1765),
			(373,1736), (331,1732), (304,1746), (339,1778), (360,1819),
			(364,1872), (359,1941), (342,1988), (318,2009), (293,2019))
			)
		])

	cuffs_highlights = Aspect(
		fillcolor=Aspect.colors["cuffs_highlights"],
		pensize=3,
		polygons=[

		Polygon("cuffs_highlights1",
			((293,2033), (308,2042), (325,2042), (348,2027), (376,2000),
			(395,1958), (404,1916), (405,1859), (395,1804), (382,1773),
			(358,1738), (332,1734), (304,1746), (339,1778), (360,1819),
			(364,1872), (359,1941), (342,1988), (318,2009), (293,2019))
			),
		Polygon("cuffs_highlights2",
			((1115,1633), (1114,1655), (1150,1683), (1186,1702), (1230,1709),
			(1270,1707), (1316,1696), (1359,1678), (1397,1651), (1416,1629),
			(1425,1603), (1409,1576), (1386,1609), (1346,1637), (1302,1656),
			(1252,1667), (1203,1666), (1169,1653), (1148,1630), (1132,1621))
			)
		])

	lips = Aspect(
		fillcolor=Aspect.colors["spikes"],
		pensize=4,
		polygons=[

		Polygon("lips",
			((964,2249), (1018,2281), (1083,2304), (1124,2309), (1172,2305),
			(1224,2289), (1277,2250), (1309,2204), (1328,2141), (1326,2075),
			(1294,2003), (1247,1949), (1171,1902), (1085,1875), (1058,1831),
			(1011,1790), (960,1766), (909,1758), (852,1766), (793,1792),
			(744,1829), (703,1872), (668,1919), (745,1913), (773,1882),
			(816,1853), (873,1828), (912,1826), (949,1838), (983,1860),
			(1010,1889), (1031,1928), (1048,1971), (1058,2021), (1019,2046),
			(971,1997), (909,1960), (864,1942), (805,1923), (745,1914),
			(668,1920), (610,1935), (563,1958), (518,1995), (483,2051),
			(464,2105), (462,2171), (481,2235), (527,2290), (574,2321),
			(642,2343), (714,2348), (784,2335), (862,2307), (923,2276))
			)
		])

	black_lines = Aspect(
		fillcolor=Aspect.colors["black"],
		polygons=[

		Polygon("black_lines1",
			((567,751), (578,755), (607,739), (655,716), (727,697), (794,689),
			(858,689), (925,700), (978,715), (1011,729), (1031,729),
			(1025,714), (998,700), (966,687), (914,675), (856,669), (792,669),
			(739,676), (680,690), (617,712), (593,724), (568,742))
			),
		Polygon("black_lines2",
			((499,1289), (522,1285), (543,1275), (561,1259), (575,1238),
			(584,1213), (587,1186), (584,1159), (575,1135), (561,1113),
			(543,1097), (522,1087), (499,1083), (477,1087), (456,1097),
			(438,1113), (424,1135), (415,1159), (412,1186), (415,1213),
			(424,1238), (438,1259), (456,1275), (477,1285))
			),
		Polygon("black_lines3",
			((1172,1262), (1191,1242), (1205,1218), (1213,1191), (1213,1163),
			(1206,1136), (1192,1111), (1173,1091), (1149,1077), (1122,1070),
			(1094,1070), (1068,1077), (1043,1091), (1024,1111), (1009,1135),
			(1002,1162), (1002,1190), (1009,1217), (1023,1242), (1042,1262),
			(1066,1276), (1093,1283), (1121,1283), (1147,1276))
			),
		Polygon("black_lines4",
			((1251,2284), (1270,2310), (1287,2324), (1310,2333), (1331,2335),
			(1343,2333), (1352,2322), (1352,2306), (1343,2289), (1329,2278),
			(1309,2272), (1301,2272), (1301,2278), (1309,2280), (1316,2287),
			(1326,2303), (1326,2311), (1317,2313), (1301,2307), (1283,2295),
			(1263,2276))
			),
		Polygon("black_lines5",
			((1009,2077), (1027,2056), (1043,2042), (1070,2031), (1097,2025),
			(1096,2016), (1076,2010), (1052,2009), (1031,2017), (1015,2030),
			(1006,2050), (1002,2073))
			),
		Polygon("black_lines6",
			((663,2181), (672,2193), (686,2206), (698,2209), (708,2205),
			(718,2195), (723,2201), (724,2214), (715,2227), (702,2232),
			(686,2230), (672,2219), (662,2204), (660,2190))
			),
		Polygon("black_lines7",
			((586,2180), (575,2194), (566,2202), (556,2206), (547,2205),
			(541,2201), (539,2208), (539,2218), (545,2228), (556,2231),
			(566,2230), (575,2222), (584,2209), (589,2186))
			),
		Polygon("black_lines8",
			((913,2289), (903,2294), (896,2306), (892,2325), (892,2346),
			(899,2380), (938,2396), (943,2363), (943,2342), (939,2321),
			(932,2303), (923,2292))
			),
		Polygon("black_lines9",
			((733,2404), (732,2379), (723,2353), (694,2356), (695,2385),
			(702,2405), (711,2418))
			),
		Polygon("black_lines10",
			((338,1881), (328,1855), (315,1842), (303,1839), (294,1841),
			(286,1838), (293,1823), (294,1804), (291,1787), (283,1773),
			(298,1772), (321,1775), (292,1762), (268,1760), (244,1763),
			(257,1774), (278,1799), (281,1819), (276,1833), (264,1841),
			(246,1821), (218,1798), (208,1796), (201,1797), (182,1787),
			(158,1783), (136,1798), (115,1815), (109,1834), (119,1822),
			(136,1812), (156,1809), (176,1811), (187,1816), (177,1841),
			(171,1865), (170,1900), (175,1926), (186,1948), (204,1965),
			(193,1934), (192,1906), (197,1881), (216,1877), (236,1866),
			(249,1855), (259,1866), (264,1878), (280,1867), (298,1864),
			(316,1866))
			)
		])

	nails = Aspect(
		fillcolor=Aspect.colors["clown"],
		pensize=3,
		polygons=[

		Polygon("nails1",
			((100,1896), (29,1921), (18,1937), (30,1957), (95,1988),
			(104,1942))
			),
		Polygon("nails2",
			((209,1806), (226,1812), (258,1844), (214,1871), (182,1875),
			(191,1834))
			),
		Polygon("nails3",
			((1143,1510), (1100,1509), (1082,1515), (1087,1537), (1109,1575),
			(1123,1563), (1140,1534))
			),
		Polygon("nails4",
			((1234,1444), (1195,1414), (1171,1406), (1159,1427), (1160,1478),
			(1184,1475), (1213,1461))
			),
		Polygon("nails5",
			((1328,1438), (1318,1407), (1307,1385), (1290,1375), (1273,1390),
			(1249,1440), (1274,1448), (1307,1446))
			),
		Polygon("nails6",
			((1398,1493), (1395,1433), (1388,1419), (1342,1458), (1382,1488))
			)
		])

	eyebrows = Aspect(
		fillcolor=Aspect.colors["hair"],
		pensize=3,
		polygons=[

		Polygon("eyebrows1",
			((745,2408), (736,2431), (705,2483), (677,2548), (663,2529),
			(654,2510), (630,2505), (611,2495), (626,2476), (686,2433),
			(724,2411))
			),
		Polygon("eyebrows2",
			((876,2380), (882,2395), (904,2416), (1025,2567), (1036,2539),
			(1043,2503), (1090,2487), (1031,2446), (947,2398), (895,2377))
			)
		])

	return (
		spikes, shell, arm, bib, teeth, mouth, tongue, hair, headband, head,
		horn, tooth, clown, clown_makeup, clown_mouth, clown_opening, hands,
		cuffs, cuffs_highlights, lips, black_lines, nails, eyebrows), size


def draw_icons(icon_list):
	"""Draws icons to the grid as per the provided data set's values."""

	# Construct all the icon designs and add the designs to a dict.
	Icon.designs["A"] = setup_design_a()
	Icon.designs["B"] = setup_design_b()
	Icon.designs["C"] = setup_design_c()
	Icon.designs["D"] = setup_design_d()

	# Cycle through the data set's icons; construct and draw.
	for parameters in icon_list:
		icon = Icon(*parameters)
		icon.draw()

#--------------------------------------------------------------------#

#  /$$$$$$$$                 /$$
# | $$_____/                | $$
# | $$       /$$$$$$$   /$$$$$$$
# | $$$$$   | $$__  $$ /$$__  $$
# | $$__/   | $$  \ $$| $$  | $$
# | $$      | $$  | $$| $$  | $$
# | $$$$$$$$| $$  | $$|  $$$$$$$
# |________/|__/  |__/ \_______/

#-----Main Program---------------------------------------------------#
#
# This main program sets up the grid, ready for you to start drawing
# your icons. Do not change any of this code except where indicated
# by comments marked "*****".

# Set up the drawing window with a neutral background color and
# enough space for the grid
setup(window_width, window_height)
bgcolor("grey")

# Give the window a title
# ***** Replace this title with one that describes your chosen
# ***** theme and icons
title("Nintendo Characters (Meta Knight, Charmander, Samus, Bowser Jr.)")

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed("fastest")

# Draw the grid
# ***** If you want to turn off animation while drawing the grid,
# ***** change the following argument to False
tracer(False)
# ***** If you don't want to display the grid's frame, individual
# ***** squares or the numeric labels change the corresponding
# ***** argument(s) below to False
draw_frame(True)
draw_squares(True)
draw_labels(True)

# Call the student's function to display the icons
# ***** If you want to turn off animation while drawing your icons,
# ***** change the following argument to False
tracer(False)
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_icons(data_set_00)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()
