class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value


class TwHashTable:
	def __init__(self, size):
		self.size = size
		from itertools import repeat
		self.array = [[] for i in repeat(None, size)]

	def __get_hash_value__(self, key):

		return key % self.size

	def __find_node_by_key__(self, key, chain_list):

		for node in chain_list:
			if node.key == key:
				return node
		return None

	def __check_key_value__(self, key):

		if isinstance( key, int ) == False:
			raise ValueError('Integer please')

	def add(self, key, value):

		self.__check_key_value__(key)

		node = Node(key, value)
		index = self.__get_hash_value__(key)

		if len(self.array) > index:
			self.array[index].append(node)
		else:
			self.array[index] = [node]

	def remove(self, key):

		self.__check_key_value__(key)

		index = self.__get_hash_value__(key)
		chain_list = self.array[index]
		
		if self.array[index] is not None:

			for node in self.array[index]:
				if node.key == key :
					self.array[index].remove(node)
					break

	def get(self, key):

		self.__check_key_value__(key)

		index = __get_hash_value__(key)
		chain_list = array[index]
		return __find_node_by_key__(key)


	def print_hash_structure(self):
		for index in range(0, self.size):
			print("Index : " + str(index) + " => ", end='')
			if self.array[index] is not None:
				for node in self.array[index]:
					print(str(node.value) + " ", end='')
				print()

		print("Work!")


tw_hash_table = TwHashTable(100)

tw_hash_table.add(12, "First")
tw_hash_table.add(43, "Removed")
tw_hash_table.add(90, "Second")
tw_hash_table.add(67, "Third")
tw_hash_table.add(5, "Fourth")
tw_hash_table.add(105, "Fifth")
tw_hash_table.add(205, "Sixth")
tw_hash_table.add(305, "Seventh")

tw_hash_table.remove(43)

tw_hash_table.print_hash_structure()