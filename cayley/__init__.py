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
			raise Exception(response.json["error"])

	def shape(self, data):
		if not isinstance(data, str):
			raise TypeError()
		response = requests.post("%s/shape/%s" % (self._url, self._lang), data)
		if response.status_code == requests.codes.ok:
			return response.json()
		else:
			raise Exception(response.json["error"])

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
			raise Exception(response.json["error"])

	def write_file(self, filename):
		if not isinstance(filename, str):
			raise TypeError()
		nquad_file = {'NQuadFile': open(filename, 'rb')}
		response = requests.post("%s/write/file/nquad" % (self._url), files=nquad_file)
		if response.status_code == requests.codes.ok:
			return response.json()
		else:
			raise Exception(response.json()["error"])

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
			raise Exception(response.json["error"])

class _null(object):
	def __repr__(self):
		return "null"

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
		self.queries.append("Morphism()")

	def __repr__(self):
		return ".".join(self.queries)

	# Traversals
	def Out(self, predicate_path=None, tags=None):
		if predicate_path is None:
			predicate_path = _null()
		if isinstance(predicate_path, list):
			for pred_path in predicate_path:
				if not isinstance(pred_path, str):
					raise TypeError("Predicate paths must be strings.")
		if isinstance(tags, list):
			for tag in tags:
				if not isinstance(tag, str):
					raise TypeError("Tags must be strings.")
		if tags is None:
			self.queries.append("Out(%s)" % (repr(predicate_path)))
		else:
			self.queries.append("Out(%s,%s)" % (repr(predicate_path), repr(tags)))
		return self

	def In(self, predicate_path=None, tags=None):
		if predicate_path is None:
			predicate_path = _null()
		if isinstance(predicate_path, list):
			for pred_path in predicate_path:
				if not isinstance(pred_path, str):
					raise TypeError("Predicate paths must be strings.")
		if isinstance(tags, list):
			for tag in tags:
				if not isinstance(tag, str):
					raise TypeError("Tags must be strings.")
		if tags is None:
			self.queries.append("In(%s)" % (repr(predicate_path)))
		else:
			self.queries.append("In(%s,%s)" % (repr(predicate_path), repr(tags)))
		return self

	def Both(self, predicate_path=None, tags=None):
		if predicate_path is None:
			predicate_path = _null()
		if isinstance(predicate_path, list):
			for pred_path in predicate_path:
				if not isinstance(pred_path, str):
					raise TypeError("Predicate paths must be strings.")
		if isinstance(tags, list):
			for tag in tags:
				if not isinstance(tag, str):
					raise TypeError("Tags must be strings.")
		if tags is None:
			self.queries.append("Both(%s)" % (repr(predicate_path)))
		else:
			self.queries.append("Both(%s,%s)" % (repr(predicate_path), repr(tags)))
		return self

	def Is(self, node, *nodes):
		if not isinstance(node, str):
			raise TypeError()
		for n in nodes:
			if not isinstance(n, str):
				raise TypeError()
		if nodes:
			self.queries.append("Is(%s)" % repr([node] + list(nodes)))
		else:
			self.queries.append("Is(%s)" % repr(node))
		return self

	def Has(self, predicate, object):
		if not isinstance(predicate, str):
			raise TypeError()
		if not isinstance(object, str):
			raise TypeError()
		self.queries.append("Has(%s,%s)" % (repr(predicate), repr(object)))
		return self

	def LabelContext(self, label_path=None, tags=None):
		if label_path is None:
			label_path = _null()
		if tags is None:
			self.queries.append("LabelContext(%s)" % repr(label_path))
		else:
			self.queries.append("LabelContext(%s,%s)" % (repr(label_path), repr(tags)))
		return self

	# Tagging
	def Tag(self, tag):
		if not isinstance(tag, str):
			raise TypeError()
		self.queries.append("Tag(%s)" % repr(tag))
		return self

	def Back(self, tag):
		if not isinstance(tag, str):
			raise TypeError()
		self.queries.append("Back(%s)" % repr(tag))
		return self

	def Save(self, predicate, tag):
		if not isinstance(predicate, str):
			raise TypeError()
		if not isinstance(tag, str):
			raise TypeError()
		self.queries.append("Save(%s,%s)" % (repr(predicate), repr(tag)))
		return self

	# Joining
	def Intersect(self, query):
		if not isinstance(query, _Query):
			return TypeError()
		self.queries.append("Intersect(%s)" % repr(query))
		return self
	def And(self, query):
		return self.Intersect(query)

	def Union(self, query):
		if not isinstance(query, _Query):
			return TypeError()
		self.queries.append("Union(%s)" % repr(query))
		return self
	def Or(self, query):
		return self.Union(query)

	def Except(self, query):
		if not isinstance(query, _Query):
			return TypeError()
		self.queries.append("Except(%s)" % repr(query))
		return self
	def Difference(self, query):
		return self.Except(query)

	# Morphisms
	def Follow(self, morphism):
		if not isinstance(morphism, _Path):
			raise TypeError()
		self.queries.append("Follow(%s)" % repr(morphism))
		return self

	def FollowR(self, morphism):
		if not isinstance(morphism, _Path):
			raise TypeError()
		self.queries.append("FollowR(%s)" % repr(morphism))
		return self

class _Query(_Path):
	def __init__(self, *node_ids):
		self.queries = []
		self.queries.append("g")
		if len(node_ids) > 0:
			self.queries.append("V(%s)" % repr(list(node_ids)))
		else:
			self.queries.append("V()")

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

	def ForEach(self, arg1, arg2=None):
		if isinstance(arg1, int) or isinstance(arg1, long):
			limit = arg1
			callback = arg2
		else:
			limit = None
			callback = arg1
		if not isinstance(callback, str):
			raise TypeError()
		if limit is None:
			self.queries.append("ForEach(%s)" % repr(callback))
		else:
			if not isinstance(limit, long) and not isinstance(limit, int):
				raise TypeError()
			self.queries.append("ForEach(%s,%s)" % (limit, repr(callback)))
		return ".".join(self.queries)
	def Map(self, arg1, arg2=None):
		return self.ForEach(arg1, arg2)
