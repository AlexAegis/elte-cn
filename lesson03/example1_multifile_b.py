""" this file is meant to run second so before doing
anything it should run file a, unless it's called from file a
"""

print "file b loaded"

import example1_multifile


class ExampleB(object):
	"""[summary]

	Arguments:
		object {[type]} -- [description]
	"""

	@classmethod
	def test(cls):
		"""test print
		"""
		print cls.class_name()

	@classmethod
	def class_name(cls):
		"""test print
		"""

		return cls.__name__


if __name__ == '__main__':
	example1_multifile.run()
