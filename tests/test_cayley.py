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
		self.assertEqual(g.V().ForEach("function(d) { g.Emit(d) }"),
			"g.V().ForEach('function(d) { g.Emit(d) }')")

	def test_vertex_foreach_with_limit(self):
		self.assertEqual(g.V().Map(1, "function(d) { g.Emit(d) }"),
			"g.V().ForEach(1,'function(d) { g.Emit(d) }')")

	def test_path_out_all(self):
		self.assertEqual(g.V().Out().All(), "g.V().Out(null).All()")

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
		self.assertEqual(g.V().In().All(), "g.V().In(null).All()")

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
		self.assertEqual(g.V().Both().All(), "g.V().Both(null).All()")

	def test_path_both_pred_path_all(self):
		self.assertEqual(g.V("bob").Both("follows").All(),
		 	"g.V(['bob']).Both('follows').All()")

	def test_path_both_pred_paths_all(self):
		self.assertEqual(g.V("bob").Both(["follows", "status"]).All(),
			"g.V(['bob']).Both(['follows', 'status']).All()")

	def test_path_both_pred_path_tag_all(self):
		self.assertEqual(g.V("bob").Both("follows", "pred").All(),
			"g.V(['bob']).Both('follows','pred').All()")

	def test_path_is_node(self):
		self.assertEqual(g.V().Is("bob").All(), "g.V().Is('bob').All()")

	def test_path_is_nodes(self):
		self.assertEqual(g.V().Is("bob", "alice").All(),
			"g.V().Is(['bob', 'alice']).All()")

	def test_path_has(self):
		self.assertEqual(g.V().Has("follows", "alice").All(),
			"g.V().Has('follows','alice').All()")

	def test_path_label_context_empty(self):
		self.assertEqual(g.V().LabelContext().All(), "g.V().LabelContext(null).All()")

	def test_path_label_context_string_path(self):
		self.assertEqual(g.V().LabelContext("alice").All(),
			"g.V().LabelContext('alice').All()")

	def test_path_label_context_list_path(self):
		self.assertEqual(g.V().LabelContext(["alice", "bob"]).All(),
			"g.V().LabelContext(['alice', 'bob']).All()")

	def test_path_label_context_query_path(self):
		self.assertEqual(g.V().LabelContext(g.V('bob')).All(),
			"g.V().LabelContext(g.V(['bob'])).All()")

	def test_path_label_context_string_path_string_tags(self):
		self.assertEqual(g.V().LabelContext("alice", "status").All(),
			"g.V().LabelContext('alice','status').All()")

	def test_path_label_context_string_path_list_tags(self):
		self.assertEqual(g.V().LabelContext("alice", ["status", "follows"]).All(),
			"g.V().LabelContext('alice',['status', 'follows']).All()")

	def test_path_tag(self):
		self.assertEqual(g.V().Tag("start").All(), "g.V().Tag('start').All()")

	def test_path_back(self):
		self.assertEqual(g.V().Back("start").All(), "g.V().Back('start').All()")

	def test_path_save(self):
		self.assertEqual(g.V().Save("follows", "target").All(),
			"g.V().Save('follows','target').All()")

	def test_path_intersect(self):
		self.assertEqual(g.V().Intersect(g.V("alice")).All(),
			"g.V().Intersect(g.V(['alice'])).All()")

	def test_path_and(self):
		self.assertEqual(g.V().And(g.V("alice")).All(),
			"g.V().Intersect(g.V(['alice'])).All()")

	def test_path_union(self):
		self.assertEqual(g.V().Union(g.V("alice")).All(),
			"g.V().Union(g.V(['alice'])).All()")

	def test_path_or(self):
		self.assertEqual(g.V().Union(g.V("alice")).All(),
			"g.V().Union(g.V(['alice'])).All()")

	def test_path_except(self):
		self.assertEqual(g.V().Except(g.V("alice")).All(),
			"g.V().Except(g.V(['alice'])).All()")

	def test_path_difference(self):
		self.assertEqual(g.V().Except(g.V("alice")).All(),
			"g.V().Except(g.V(['alice'])).All()")

	def test_path_follow(self):
		morphism = g.Morphism().Out("follows")
		self.assertEqual(g.V("bob").Follow(morphism).All(),
			"g.V(['bob']).Follow(g.Morphism().Out('follows')).All()")

	def test_path_followr(self):
		morphism = g.Morphism().Out("follows")
		self.assertEqual(g.V("bob").FollowR(morphism).All(),
			"g.V(['bob']).FollowR(g.Morphism().Out('follows')).All()")

if __name__ == "__main__":
	unittest.main(verbosity=10)
