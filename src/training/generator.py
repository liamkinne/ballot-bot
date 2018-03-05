""" Generate training data from templates and information. """

import os, csv, sys
import numpy
import cv2
import random

def get_box_locations(file_path):
	with open(file_path, 'r') as file:
		csv_data = csv.DictReader(file)
		box_locations = []
		for number, row in enumerate(csv_data):
			box_locations.append({
				'number' : number,
				'x' : int(row['box-x']),
				'y' : int(row['box-y']),
				'width' : int(row['width']),
				'height' : int(row['height']),
			})
	return box_locations

def get_candidates(file_path):
	with open(file_path, 'r') as file:
		data = csv.DictReader(file)
		candidates = []
		numer = 0
		for row in data:
			candidates.append({
				'last' : row['Last'],
				'first' : row['First'],
			})
	return candidates

def overlay_image(image, overlay, pos):
	x, y = pos
	image[y:y+overlay.shape[0], x:x+overlay.shape[1]] = overlay

def create_data(number, template_image_path, locations_path):
	images = []
	template_image = cv2.imread(template_image_path)
	for i in range(number):
		this_image = template_image
		box_locations = get_box_locations(locations_path)
		for box in box_locations:
			n = random.randint(1, len(box_locations))
			dir_list = os.listdir('mnist-dataset/' + str(n) + '/')
			path = 'mnist-dataset/' + str(n) + '/' + random.choice(dir_list)
			number_image = cv2.imread(path)
			number_image = cv2.bitwise_not(number_image) #invert
			overlay_image(this_image, number_image, (box['x'], box['y']))

		images.append(this_image)
	return images;

# Unit Test
if __name__ == "__main__":
	# print layout data
	print("\nAll box/name box_locations:")
	box_locations = get_box_locations("full-preferential/box-locations.csv")
	for box in box_locations:
		print(box)
	print("\nAll candidates:")
	candidates = get_candidates("full-preferential/candidates.csv")
	for candidate in candidates:
		print(candidate["last"], candidate["first"])

	template_path = 'full-preferential/templates/template.jpg'
	locations_path = 'full-preferential/box-locations.csv'
	images = create_data(3, template_path, locations_path)
	for image in images:
		cv2.imshow("Test Image. Press zero for next image.",image)
		cv2.waitKey()
