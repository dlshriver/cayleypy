import unittest

from cayley import *

class CayleyTests(unittest.TestCase):
	def test_emit_string(self):
		self.assertEqual(g.Emit("test"), 'g.Emit("test")')

	def test_emit_list(self):
		self.assertEqual(g.Emit(["test_item_1", "test_item_2"]),
			'g.Emit(["test_item_1", "test_item_2"])')

	def test_emit_dict(self):
		emit = g.Emit({"test_key_1": 1, "test_key_2": 2})
		self.assertTrue(emit == "g.Emit({\"test_key_1\": 1, \"test_key_2\": 2})"
			or emit == "g.Emit({\"test_key_2\": 2, \"test_key_1\": 1})")

	def test_vertex_all(self):
		self.assertEqual(g.V().All(), "g.V().All()")

	def test_vertex_get_limit(self):
		self.assertEqual(g.V().GetLimit(10), "g.V().GetLimit(10)")

	def test_vertex_to_array(self):
		self.assertEqual(g.V().ToArray(), "g.V().ToArray()")

	def test_vertex_to_value(self):
		self.assertEqual(g.V().ToValue(), "g.V().ToValue()")

	def test_vertex_tag_array(self):
		self.assertEqual(g.V().TagArray(), "g.V().TagArray()")

	def test_vertex_tag_value(self):
		self.assertEqual(g.V().TagValue(), "g.V().TagValue()")

	def test_vertex_foreach(self):
		with self.assertRaises(NotImplementedError):
			self.assertEqual(g.V().ForEach(), "g.V().ForEach()")

	def test_path_out_all(self):
		self.assertEqual(g.V().Out().All(), "g.V().Out().All()")

	def test_path_out_pred_path_all(self):
		self.assertEqual(g.V("alice").Out("follows").All(),
		 	"g.V(['alice']).Out('follows').All()")

	def test_path_out_pred_paths_all(self):
		self.assertEqual(g.V("bob").Out(["follows", "status"]).All(),
			"g.V(['bob']).Out(['follows', 'status']).All()")

	def test_path_out_pred_path_tag_all(self):
		self.assertEqual(g.V("bob").Out("status", "pred").All(),
			"g.V(['bob']).Out('status','pred').All()")

	def test_path_in_all(self):
		self.assertEqual(g.V().In().All(), "g.V().In().All()")

	def test_path_in_pred_path_all(self):
		self.assertEqual(g.V("bob").In("follows").All(),
		 	"g.V(['bob']).In('follows').All()")

	def test_path_in_pred_paths_all(self):
		self.assertEqual(g.V("bob").In(["follows", "status"]).All(),
			"g.V(['bob']).In(['follows', 'status']).All()")

	def test_path_in_pred_path_tag_all(self):
		self.assertEqual(g.V("bob").In("follows", "pred").All(),
			"g.V(['bob']).In('follows','pred').All()")

	def test_path_both_all(self):
		self.assertEqual(g.V().Both().All(), "g.V().Both().All()")

	def test_path_both_pred_path_all(self):
		self.assertEqual(g.V("bob").Both("follows").All(),
		 	"g.V(['bob']).Both('follows').All()")

	def test_path_both_pred_paths_all(self):
		self.assertEqual(g.V("bob").Both(["follows", "status"]).All(),
			"g.V(['bob']).Both(['follows', 'status']).All()")

	def test_path_both_pred_path_tag_all(self):
		self.assertEqual(g.V("bob").Both("follows", "pred").All(),
			"g.V(['bob']).Both('follows','pred').All()")

	def test_path_is(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex().Is("bob")

	def test_path_has(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex().Has("follows", "bob")

	def test_path_label_context(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex().LabelContext()

	def test_path_tag(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex().Tag("start")

	def test_path_back(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex().Back("start")

	def test_path_save(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex().Save("follows", "target")

	def test_path_intersect(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").Out("follows").Intersect(g.V("alice").Out("follows"))

	def test_path_and(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").Out("follows").And(g.V("alice").Out("follows"))

	def test_path_union(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").Out("follows").Union(g.V("alice").Out("follows"))

	def test_path_or(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").Out("follows").Or(g.V("alice").Out("follows"))

	def test_path_except(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").Out("follows").Except(g.V("alice").Out("follows"))

	def test_path_difference(self):
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").Out("follows").Difference(g.V("alice").Out("follows"))

	def test_path_follow(self):
		morphism = g.Morphism().Out("follows")
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").Follow(morphism)

	def test_path_followr(self):
		morphism = g.Morphism().Out("follows")
		with self.assertRaises(NotImplementedError):
			graph.Vertex("bob").FollowR(morphism)

if __name__ == "__main__":
	unittest.main(verbosity=10)
