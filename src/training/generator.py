""" Generate training data from templates and information. """

import os, csv, sys

def get_box_locations(file_path):
	
	file = open(file_path)
	file_data = csv.DictReader(file)
	box_locations = []
	for row in file_data:
		data = {
			'box': {
				'x' : row['box-x'],
				'y' : row['box-y'],
			},
			'name': {
				'x' : row['name-x'],
				'y' : row['name-y'],
			}
		}
		box_locations.append(data)
	file.close()
	
	return box_locations

def get_candidates(file_path):
	file = open(file_path)
	file_data = csv.DictReader(file)
	candidates = []
	for row in file_data:
		data = {
			'last' : row['Last'],
			'first' : row['First'],
		}
		candidates.append(data)
	file.close()

	return candidates


if __name__ == "__main__":
	print("\nAll box/name box_locations:")
	box_locations = get_box_locations("full-preferential/box-locations.csv")
	for box in box_locations:
		print(box)
	print("\nAll candidates:")
	candidates = get_candidates("full-preferential/candidates.csv")
	for candidate in candidates:
		print(candidate["last"], candidate["first"])
