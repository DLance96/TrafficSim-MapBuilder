import coordinates

#Road object. Stores information regarding the position of a road
class road(object):

	#road constructor. Takes in itself, the road's starting
	#coordinates, the road's length, the number
	#of outgoing lanes, and the number of outgoing lanes.
	def __init__(self, start_coord, length, out_lanes, in_lanes):
		self.coord = start_coord
		self.length = length
		self.out_lanes = out_lanes
		self.in_lanes = in_lanes
	
	#returns starting coordinates of the road.
	def get_coords(self):
		return self.coord
	
	#returns lengths of the road. 
	def get_length(self):
		return self.length
		
	#returns the end coordinates of this road.
	def get_end_coords(self):
		return self.end_coord
	
	#returns the number of outgoing lanes of the road.
	def get_out_lanes(self):
		return self.out_lanes
	
	#returns the number of incoming lanes of the road.
	def get_in_lanes(self):
		return self.in_lanes
	
	#updates the start coordinates of the road.
	def update_coords(self, new_start_coord):
		self.coord = new_start_coord
	
	#updates the length of the road.
	def update_length(self, new_length):
		self.length = new_length
			
	#updates the number of outgoing lanes of the road.
	def update_out_lanes(self, new_out_lanes):
		self.out_lanes = new_out_lanes
	
	#updates the number of incoming lanes of the road.
	def update_in_lanes(self, new_in_lanes):
		self.in_lanes = new_in_lanes
	
	#Returns a list	of next locations for all vehicles on this road.
	def request_next_locations(self):
		print 'Calls the compute_next_location function of eached contained vehicle'
		print 'Should return a list of coordinates, ie next locations of vehicles.' 

	#Determines if an object is on the current road. Returns true if so, false if otherwise.
	def is_on_road(self, coord):
		print 'determines of coord is within the boundary of the Road.'
		
	#Converts local coordinates to global coordinates. Returns global coordinates.
	def location_conversion(self, local_coord):
		print 'locationconversion'
	
	#Returns the index of of a neighboring object that contains the global coordinate.
	def which_neighbor(self, global_coord):
		print 'whichneighbor' 
		
	#Transfers a vehicle to the local coordinates of the road corresponding to the 
	#global coordinates.
	def transfer(self, vehicle, global_coord):
		print 'transfer'
		
	#Shifts each vehicle to its next location by calling the vehicle's update_location()
	def update_positions(self):
		print 'updatepositions'
	
	#Spawns a vehicle on the road using vehicle and driver templates. The enum describes the car direction.	
	def spawn(self, vehicle_template, driver_template, enum):
		print 'spawn'
		
	#Adds a neighboring road to this road.
	def add_neighboring_road(self, neighbor_road):
		self.neighboring_road = neighbor_road
		
	#Adds a neighboring intersection to this road.
	def add_neighboring_intersection(self, intersection):
		self.neighboring_intersection = intersection
		
	#Returns the neighboring road.
	def get_neighboring_road(self):
		return self.neighboring_road
	
	#Returns the neighboring intersection.
	def get_neighboring_intersection(self):
		return self.neighboring_intersection

#main method of road object.		
def main():
	start_coord = coordinates.coordinates(3,1)
	out_lanes = 4
	in_lanes = 3
	length = 2
	
	r = road(start_coord, length, out_lanes, in_lanes)
	r2 = road(start_coord, 12, 23, 54)
	
	r.add_neighboring_road(r2)
	
	road_coord = r.get_coords()
	
	start_x = road_coord.get_x()
	start_y = road_coord.get_y()
	
	
	print 'start coords: (' + str(start_x) + ', ' + str(start_y) + ')' 
	print 'out lanes: ' + str(r.get_out_lanes())
	print 'in lanes: ' + str(r.get_in_lanes())
	print 'length: ' + str(r.get_length())
	print ' '
	
	new_coord = coordinates.coordinates(7,4)
	
	r.update_coords(new_coord)
	r.update_length(10)
	r.update_out_lanes(96)
	r.update_in_lanes(12)
	
	new_road_coord = r.get_coords()
	new_x = new_road_coord.get_x()
	new_y = new_road_coord.get_y()
	
	print 'new coords: (' + str(new_x) + ', ' + str(new_y) + ')' 
	print 'out lanes: ' + str(r.get_out_lanes())
	print 'in lanes: ' + str(r.get_in_lanes())
	print 'length: ' + str(r.get_length())

if __name__ == '__main__':
	main()