import unittest

from cayley import *

class CayleyClientTests(unittest.TestCase):
	def test_query_default(self):
		client = CayleyClient()
		response = client.query("graph.Vertex().GetLimit(1)")
		self.assertTrue(isinstance(response, dict))

	def test_query_gremlin_v1(self):
		client = CayleyClient(url="http://localhost:64210", version="v1", lang="gremlin")
		response = client.query("graph.Vertex().GetLimit(1)")
		self.assertTrue(isinstance(response, dict))

	def test_shape_default(self):
		client = CayleyClient()
		response = client.shape("graph.Vertex().GetLimit(1)")
		self.assertTrue(isinstance(response, dict))

	def test_shape_gremlin_v1(self):
		client = CayleyClient(url="http://localhost:64210", version="v1", lang="gremlin")
		response = client.shape("graph.Vertex().GetLimit(1)")
		self.assertTrue(isinstance(response, dict))

	def test_write(self):
		client = CayleyClient()
		response = client.write("alice", "drinks", "milk")
		self.assertTrue(isinstance(response, dict))
		self.assertEqual(response["result"], "Successfully wrote 1 quads.")

	def test_write_file(self):
		client = CayleyClient()
		response = client.write_file("C:/Users/David/Downloads/cayley_0.4.1_windows_amd64/data/30kmoviedata.nq.gz")
		self.assertTrue(isinstance(response, dict))
		self.assertEqual(response["result"], "Successfully wrote 471705 quads.")

	def test_delete(self):
		client = CayleyClient()
		response = client.delete("alice", "drinks", "milk")
		self.assertTrue(isinstance(response, dict))
		self.assertEqual(response["result"], "Successfully deleted 1 quads.")

if __name__ == "__main__":
	unittest.main(verbosity=10)
