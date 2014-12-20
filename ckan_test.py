import ckan_module

class CkanTest:
	def __init__(self, server_address, api_key, resource_id):
		self.ckan = ckan_module.ckan(server_address, api_key, resource_id)

	#test create datastore on ckan
	def create_datastore_test(self):
		fields = [{'id': 'temperature', 'type':'float'},{'id': 'humidity', 'type': 'float'},{'id': 'pm25', 'type': 'float'}]
		self.ckan.create_datastore(fields)

	#test delete datastore on ckan
	def delete_datastore_test(self):
		self.ckan.delete_datastore()

	#test update resource on ckan
	def update_resource_test(self):
		self.ckan.update_resource()

	#test get data from ckan
	def get_data_test(self):
		self.ckan.get_data(1,1)

	#test push data to ckan
	def push_data_test(self):
		data = {'temperature': 32, 'humidity': 90, 'pm25': 15}
		self.ckan.push_data(data)

	#test delete data on ckan
	def delete_data_test(self):
		filters = {'temperature': 32}
		self.ckan.delete_data(filters)

server_address = ''
api_key = ''
resource_id = ''

ckan_test = CkanTest(server_address, api_key, resource_id)
#ckan_test.create_datastore_test()
#ckan_test.delete_datastore_test()
#ckan_test.update_resource_test()
#ckan_test.get_data_test()
#ckan_test.push_data_test()
ckan_test.delete_data_test()
