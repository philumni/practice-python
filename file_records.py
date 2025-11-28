class Record:
	name=""
	height="0'0\""
	id=0

	def __init__(self, name, height, id):
		self.name = name
		self.height = height
		self.id = id
		
	def __str__(self):
		return f"Name={self.name}height={self.height}id={self.id}"


class ReadIdAndHeight:
	FILENAME="id_and_height.txt"	
	id_and_height={}

	def read_file_into_dict(self, filename):
		try:
			with open(filename, 'r') as f:
				while True:
					id = f.readline()
					if not id: 
						break

					height = f.readline()	
					if not height: 
						break

					try:
						int(id) # a bit of validation
						self.id_and_height[id]=height
					except ValueError:
						print("Error: Could not convert line to a number. Invalid data found.")

		except FileNotFoundError:
			print(f"Error: File '{filename}' not found.")


class ReadNameAndId:
	FILENAME="name_and_id.txt"

	# We have to make id come first since its unique.	
	id_and_name={}	
	
	def read_file_into_dict(self, filename):
	
		try:
			with open(filename, 'r') as f:
				while True:
					name = f.readline()
					if not name: 
						break

					id = f.readline()	
					if not id: 
						break
					try:
						int(id) # a bit of validation
						self.id_and_name[id]=name
					except ValueError:
						print("Error: Could not convert line to a number. Invalid data found.")

		except FileNotFoundError:
			print(f"Error: File '{filename}' not found.")
		
	
class MakeRecords:
	records = []
	FILENAME = "records.txt"

	def __init__(self, id_and_name,id_and_height):
		for id in id_and_name.keys():
			print(f"Making record for id={id}")
			a_record = Record(id_and_name.get(id), id_and_height.get(id), id)
			self.records.append(a_record);

	def get_records(self):
		return self.records

	def write_records(self):
		try:
			with open(self.FILENAME, "w") as f:
				for a_record in self.records:
					f.write(a_record.name)
					f.write(a_record.height)
					f.write(a_record.id)
					f.write("\n");
		except OSError as e	:
				print(f"Unable to create file '{self.FILENAME}' because {e}.")

	def output_records(self):
		result=""
		for a_record in self.records:
			result+=a_record
		return result

	def read_records(self):
		records=[]
		print()
  
		try:
			with open(self.FILENAME, "r") as f:
				while True:
					name=f.readline()
					if not name:
						break
					height=f.readline()
					if not height:
						break	
					id=f.readline()
					if not id:
						break	
					blank=f.readline()
					if not blank:
						break
					a_record = Record(name, height, id)
					print(a_record)
		except FileNotFoundError:
			print(f"Error: File '{self.FILENAME}' not found.")


def main():
	print("\nReading name and id flat file...")
	readA = ReadNameAndId();
	readA.read_file_into_dict(readA.FILENAME)

	print("\nReading id and height flat file...\n")		
	readB = ReadIdAndHeight();

	readB.read_file_into_dict(readB.FILENAME)

	makeRecords = MakeRecords(readA.id_and_name, readB.id_and_height)
	
	print("Writing records to flat file...")
	makeRecords.write_records()
	
	print("\nReading records from flat file...")
	makeRecords.read_records()
 
	input("Press enter to continue.")
	print("\nProcess complete.")

main()
