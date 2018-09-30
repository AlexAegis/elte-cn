"""Runner file
"""
import example1_multifile_a
import example1_multifile_b

print "file master loaded"


def run():
	"""
	Run the files
	"""

	example1_multifile_a.ExampleA().test()
	example1_multifile_b.ExampleB().test()


if __name__ == '__main__':
	run()
