import json
import requests

class CayleyClient(object):
	def __init__(self, url="http://localhost:64210", lang="gremlin", version="v1"):
		self._url = "%s/api/%s" % (url, version)
		self._version = version
		self._lang = lang

	def query(self, data):
		if not isinstance(data, str):
			raise TypeError()
		response = requests.post("%s/query/%s" % (self._url, self._lang), data)
		if response.status_code == requests.codes.ok:
			return response.json()
		else:
			return None

	def shape(self):
		raise NotImplementedError()

	def write(self, subject, predicate, object, provenance=None):
		if not (isinstance(subject, str) and
			isinstance(predicate, str) and
			isinstance(object, str)):
			raise TypeError()
		quad = {
			"subject": subject,
			"predicate": predicate,
			"object": object,
		}
		if provenance and isinstance(provenance, str):
			quad["label"] = provenance
		response = requests.post("%s/write" % (self._url), json.dumps([quad]))
		if response.status_code == requests.codes.ok:
			return response.json()
		else:
			return None

	def write_file(self, filename):
		raise NotImplementedError()

	def delete(self, subject, predicate, object, provenance=None):
		if not (isinstance(subject, str) and
			isinstance(predicate, str) and
			isinstance(object, str)):
			raise TypeError()
		quad = {
			"subject": subject,
			"predicate": predicate,
			"object": object,
		}
		if provenance and isinstance(provenance, str):
			quad["label"] = provenance
		response = requests.post("%s/delete" % (self._url), json.dumps([quad]))
		if response.status_code == requests.codes.ok:
			return response.json()
		else:
			return None

class _Graph(object):
	def Vertex(self, *node_ids):
		return _Query(*node_ids)
	def V(self, *node_ids):
		return self.Vertex(*node_ids)

	def Morphism(self):
		return _Path()
	def M(self):
		return self.Morphism()

	def Emit(self, data):
		return "g.Emit(%s)" % json.dumps(data)
g = graph = _Graph()

class _Path(object):
	def __init__(self):
		self.queries = []
		self.queries.append("g")

	# Traversals
	def Out(self, predicate_path=None, tags=None):
		if predicate_path is None:
			if tags is not None:
				raise ValueError("Cannot have tags without predicates.")
			self.queries.append("Out()")
			return self
		if isinstance(predicate_path, list):
			for pred_path in predicate_path:
				if not isinstance(pred_path, str):
					raise ValueError("Predicate paths must be strings.")
		if isinstance(tags, list):
			for tag in tags:
				if not isinstance(tag, str):
					raise ValueError("Tags must be strings.")
		if tags is None:
			self.queries.append("Out(%s)" % (repr(predicate_path)))
		else:
			self.queries.append("Out(%s,%s)" % (repr(predicate_path), repr(tags)))
		return self

	def In(self, predicate_path=None, tags=None):
		if predicate_path is None:
			if tags is not None:
				raise ValueError("Cannot have tags without predicates.")
			self.queries.append("In()")
			return self
		if isinstance(predicate_path, list):
			for pred_path in predicate_path:
				if not isinstance(pred_path, str):
					raise ValueError("Predicate paths must be strings.")
		if isinstance(tags, list):
			for tag in tags:
				if not isinstance(tag, str):
					raise ValueError("Tags must be strings.")
		if tags is None:
			self.queries.append("In(%s)" % (repr(predicate_path)))
		else:
			self.queries.append("In(%s,%s)" % (repr(predicate_path), repr(tags)))
		return self

	def Both(self, predicate_path=None, tags=None):
		if predicate_path is None:
			if tags is not None:
				raise ValueError("Cannot have tags without predicates.")
			self.queries.append("Both()")
			return self
		if isinstance(predicate_path, list):
			for pred_path in predicate_path:
				if not isinstance(pred_path, str):
					raise ValueError("Predicate paths must be strings.")
		if isinstance(tags, list):
			for tag in tags:
				if not isinstance(tag, str):
					raise ValueError("Tags must be strings.")
		if tags is None:
			self.queries.append("Both(%s)" % (repr(predicate_path)))
		else:
			self.queries.append("Both(%s,%s)" % (repr(predicate_path), repr(tags)))
		return self

	def Is(self, node, *nodes):
		raise NotImplementedError()

	def Has(self, predicate, object):
		raise NotImplementedError()

	def LabelContext(self, label_path=None, tags=None):
		raise NotImplementedError()

	# Tagging
	def Tag(self, tag):
		raise NotImplementedError()

	def Back(self, tag):
		raise NotImplementedError()

	def Save(self, predicate, tag):
		raise NotImplementedError()

	# Joining
	def Intersect(self, query):
		raise NotImplementedError()
	def And(self, query):
		return self.Intersect(query)

	def Union(self, query):
		raise NotImplementedError()
	def Or(self, query):
		return self.Union(query)

	def Except(self, query):
		raise NotImplementedError()
	def Difference(self, query):
		return self.Except(query)

	# Morphisms
	def Follow(self, morphism):
		raise NotImplementedError()

	def FollowR(self, morphism):
		raise NotImplementedError()

class _Query(_Path):
	def __init__(self, *node_ids):
		self.queries = []
		self.queries.append("g")
		if len(node_ids) > 0:
			self.queries.append("V(%s)" % repr(list(node_ids)))
		else:
			self.queries.append("V()")

	def __repr__(self):
		return ".".join(self.queries)

	def All(self):
		self.queries.append("All()")
		return ".".join(self.queries)

	def GetLimit(self, size):
		self.queries.append("GetLimit(%s)" % size)
		return ".".join(self.queries)

	def ToArray(self):
		self.queries.append("ToArray()")
		return ".".join(self.queries)

	def ToValue(self):
		self.queries.append("ToValue()")
		return ".".join(self.queries)

	def TagArray(self):
		self.queries.append("TagArray()")
		return ".".join(self.queries)

	def TagValue(self):
		self.queries.append("TagValue()")
		return ".".join(self.queries)

	def ForEach(self, limit=None, callback=None):
		raise NotImplementedError()
