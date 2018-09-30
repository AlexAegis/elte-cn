""" this file is meant to run first then it
should run file b unless it's called from file b

Note that an import will run the script, so anything
whats directly in there will run
Also note that this import syntax altough deals with circular
imports, it still lets the first file run twice, as running
the script is not considered as an import
"""

print "file a loaded"

import example1_multifile


class ExampleA(object):
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
