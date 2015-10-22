# import ConfigParser

BUGFIX = "bugfix"
MAJOR = "major"
MINOR = "minor"


def get_software_version_string(major, minor, bugfix):
	return "{}.{}.{}".format(major, minor, bugfix)


class Version(object):
	"""docstring for Version"""

	def __init__(self, major, minor, bugfix, config):
		self.major = major
		self.minor = minor
		self.bugfix = bugfix
		self.config = config

	def get_next_version_string(self, revision):
		if revision == MAJOR:
			return self.next_major_version()
		if revision == MINOR:
			return self.next_minor_version()
		if revision == BUGFIX:
			return self.next_bug_fix_version

	@property
	def next_bug_fix_version(self):
		return get_software_version_string(self.major, self.minor, self.bugfix + 1)

	def next_minor_version(self):
		return get_software_version_string(self.major, self.minor + 1, self.bugfix)

	def next_major_version(self):
		return get_software_version_string(self.major + 1, self.minor , self.bugfix)

	def add_new_version(self, bugfix):
		self.config.add_section(get_software_version_string(self.major, self.minor, bugfix))
