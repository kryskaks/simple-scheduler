class Struct(object):
	def __init__(self, **kwds):
		self._store = kwds

	def __getattr__(self, attr):
		return self._store[attr]