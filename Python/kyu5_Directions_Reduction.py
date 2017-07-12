# Modify: 04/12/2017
#
# Author: jguardado39 (John Guardado)

class Solution(object):
	"""
	https://www.codewars.com/kata/550f22f4d758534c1100025a
	
	Once upon a time, on a way through the old wild west,…

	… a man was given directions to go from one 
	point to another. The directions were 
	"NORTH", "SOUTH", "WEST", "EAST". Clearly 
	"NORTH" and "SOUTH" are opposite, "WEST" 
	and "EAST" too. Going to one direction and 
	coming back the opposite direction is a 
	needless effort. Since this is the wild west, with 
	dreadfull weather and not much water, it's 
	important to save yourself some energy, 
	otherwise you might die of thirst!

	How I crossed the desert the smart way.

	The directions given to the man are, for 
	example, the following:

	["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
	
	or

	{ "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };

	or (haskell)

	[North, South, South, East, West, North, West]
	
	You can immediatly see that going "NORTH" 
	and then "SOUTH" is not reasonable, better 
	stay to the same place! So the task is to 
	give to the man a simplified version of the plan. A 
	better plan in this case is simply:

	["WEST"]
	
	or

	{ "WEST" }
	
	or (haskell)

	[West]
	
	or (rust)

	[WEST];

	Other examples:

	In ["NORTH", "SOUTH", "EAST", 
	"WEST"], the direction "NORTH" + "SOUTH" 
	is going north and coming back right away. 
	What a waste of time! Better to do nothing.

	The path becomes ["EAST", "WEST"], now 
	"EAST" and "WEST" annihilate each other, 
	therefore, the final result is [] (nil in Clojure).

	In ["NORTH", "EAST", "WEST", "SOUTH", 
	"WEST", "WEST"], "NORTH" and "SOUTH" are 
	not directly opposite but they become directly 
	opposite after the reduction of "EAST" and 
	"WEST" so the whole path is reducible to 
	["WEST", "WEST"].

	Task

	Write a function dirReduc which will take an 
	array of strings and returns an array of strings 
	with the needless directions removed (W<->E 
	or S<->N side by side).

	The Haskell version takes a list of directions 
	with data Direction = North | East | 
	West | South. The Clojure version returns nil 
	when the path is reduced to nothing. The Rust 
	version takes a slice of enum Direction 
	{NORTH, SOUTH, EAST, WEST}.

	Examples

	dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]) => ["WEST"]
	dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"]) => []
	See more examples in "Example Tests"

	Note

	All paths can't be made simpler. The path 
	["NORTH", "WEST", "SOUTH", "EAST"] is not 
	reducible. "NORTH" and "WEST", "WEST" and 
	"SOUTH", "SOUTH" and "EAST" are not 
	directly opposite of each other and can't 
	become such. Hence the result path is itself : 
	["NORTH", "WEST", "SOUTH", "EAST"].

	"""
	def __init__(self, arg):
		super(Solution, self).__init__()
		self.arg = arg
	
	def dirReduc(arr):
		c = {'NORTH':'SOUTH','SOUTH':'NORTH','EAST':'WEST','WEST','EAST'}
		while True:
			b, i = [], 0
			while i < len(arr) - 1:
				if c[arr[i]] == arr[i + 1]:
					i += 2
				else:
					b.append(arr[i])
					i += 1
			if i < len(arr):
				b.append(arr[i])
				i += 1
			if len(arr) == len(b):
				arr = b
				break
			arr = b
		return arr	

	def dirReduc_alt(arr):
		dir = " ".join(arr)
		dir2 = dir.replace("NORTH SOUTH",'').replace("SOUTH NORTH",'').replace("EAST WEST",'').replace("WEST EAST",'')
		dir3 = dir2.split()
		return dirReduc(dir3) if len(dir3) < len(arr) else dir3

if __name__ == '__main__':
    sol = Solution()	