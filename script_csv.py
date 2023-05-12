import csv, os

test = ['Lidar 1', 'Lidar 2', 'Lidar 3', 'Lidar 4', 'Lidar 5', 'Lidar 6', 'Lidar 7', 'Lidar 8']
data_list = ["Null", "Null"]


class script_csv:
	'''
    takes in information from range_lidar.py and stores the data from each lidar into the 
    data_list to have it in the right order when writing in the .csv file.
    Keeping in mind hardware latency, make the data_list be filled with dummy items "Null"
    '''
	# checks if the file is already created, if it is it will append data
	# if not, it creates a new one.
	def is_csv(self, file):
		if (not(os.path.isfile(file))):
			print("File doesn't not exist! Creating one now...")
			self.create_csv(file)
	# creating the csv file
	def create_csv(self, file):
		with open(file, 'w') as f:
			filewriter = csv.writer(f, delimiter=',', lineterminator='\n',
						quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerow(test)

	# stores the data from ever loop in range_lidar into global variable to be called after every loop
	def data_append(self, data, x):
		global data_list
		# if the list is empty, it fills the list with dummy items "Null"
		if (len(data_list) == 0):
			data_list = ["Null"]*2

		# checks if index matches for loop index, if so, swithc dummy item for given data.
		for i in range(len(test)):
			if (x == i) and (data != None):
				data_list[i] = data
			else:
				pass
	

	# appends the data_list into the row in order to fill in the column spaces.
    # clears the list to store new data for the following row.
	def append_csv(self, file):
		global data_list
		with open(file, 'a') as f:
			filewriter = csv.writer(f, delimiter=',', lineterminator='\n',
                                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
			filewriter.writerows([data_list])
			data_list = []

	# post processing for the csv file; remove empty rows to make it readable for users.
	def remove_blanks(self, file, file1):
		with open(file, 'r') as in_file:
			with open(file1, 'w') as out_file:
				writer = csv.writer(out_file)
				for row in csv.reader(in_file):
					if any(row):
						writer.writerow(row)
	
	

