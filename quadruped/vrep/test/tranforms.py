#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
import numpy as np
import math

"""
This file is needed by gait Trot class
"""

# FIXME: 20160625 add euler -> quaternion transform and reverse


def distance(a, b):
	"""
	Calculate the distance between pt a and pt b.
	in: vector a, vector b
	out: magnitude(b-a)
	"""
	return math.sqrt((b[0] - a[0])**2.0 + (b[1] - a[1])**2.0 + (b[2] - a[2])**2.0)
	# c = b-a
	# return math.sqrt(np.dot(c, c))


def rotateAroundCenter(matrix, axis, theta):
	"""
	not sure what this does

	in:
		matrix - ????
		axis of rotation - 'x', 'y', or 'z'
		theta - angle of rotation (rads)
	out: ???
	"""
	# axis = get_axis(axis)
	aa = [0, 0, 1]
	if axis == "x": aa = [1, 0, 0]
	elif axis == "y": aa = [0, 1, 0]
	# elif axis == "z": ret = [0, 0, 1]

	axis = np.asarray(aa)
	# theta = np.asarray(theta)
	axis = axis / math.sqrt(np.dot(axis, axis))  # normalizing axis
	a = math.cos(theta / 2.0)
	b, c, d = -axis * math.sin(theta / 2.0)
	aa, bb, cc, dd = a * a, b * b, c * c, d * d
	bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
	rot = np.array([[aa+bb-cc-dd, 2.0*(bc+ad), 2.0*(bd-ac)],
					[2.0*(bc-ad), aa+cc-bb-dd, 2.0*(cd+ab)],
					[2.0*(bd+ac), 2.0*(cd-ab), aa+dd-bb-cc]])
	return np.dot(rot, matrix)


def rotate(matrix, axis, theta, center=None):
	"""
	how is this different???
	in:
		matix - ??
		axis - axis of rotation??
		theta - angle of rotation (rads)
	out: ???
	"""
	if not center:
		center = np.matrix([[0], [0], [0]])
	else:
		center = np.matrix(center)
	matrix = np.matrix(matrix)
	if matrix.shape[0] == 1:
		matrix = np.transpose(matrix)

	if center.shape[0] == 1:
		center = np.transpose(center)
	# print center
	# print matrix

	dislocated = np.subtract(matrix, center)
	# print dislocated
	rotated = rotateAroundCenter(dislocated, axis, theta)
	# print rotated
	relocated = np.add(rotated, center)
	return relocated

# test = [[1], [0], [0]]

# print (rotate(test, 'y', math.pi, [0, 1, 0]))