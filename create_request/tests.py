import unittest
from unittest.mock import patch
from .views import CreateRequest
from .models import Client_Detail,Product_Area,Create_Request

class TestDatabase(unittest.TestCase):
	"""
	Unit test class to test database queries
	A small dummy database will be created in a memory which will be deleted 
	immediately after the tests are run.
	"""
	mock_data = [{
				"client_id": 1,
				"req_priority": 1,
				"req_description": "descA",
				"req_title": "titleA",
				"id": 1,
				"pro_area_id": 1,
				"target_date": "2018-10-10"
    }]
	
	def setUp(self):
		client = Client_Detail.objects.create(name='Velocity')
		product = Product_Area.objects.create(product_name='Reports')
		Create_Request.objects.create(req_title='title', 
								req_description='description',
								target_date='2018-10-10',
								pro_area_id=product,
								client_id=client, 
								req_priority=1)
								
	def test_get_feature_list(self):
		with patch.object(CreateRequest, "list", return_value=TestDatabase.mock_data) as mocked_get:
			request_data = Create_Request.objects.all()
			self.assertTrue(request_data)

if __name__ == '__main__':
    unittest.main()			