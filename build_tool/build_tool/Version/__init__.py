import json

BUGFIX = "bugfix"
MAJOR = "major"
MINOR = "minor"
cm = 'cloudera_manager'


def get_software_version_string(major, minor, bugfix):
	return "{}.{}.{}".format(major, minor, bugfix)


class Version(object):
	"""docstring for Version"""

	def __init__(self, major, minor, bugfix, config_path=None, section=None, ):
		self.major = major
		self.minor = minor
		self.bugfix = bugfix
		self.section = section

	@classmethod
	def from_config_file(cls, config_path, section):
		cls.config = ConfigParser.RawConfigParser()
		cls.config.read(config_path)
		return cls(cls.config.getint(section, MAJOR), cls.config.getint(section, MINOR),
		           cls.config.getint(section, BUGFIX), config_path, section )
	def __init__(self, major, minor, bugfix):
		self.major = major
		self.minor = minor
		self.bugfix = bugfix
		self.current_version = get_software_version_string(major, minor, bugfix)

	@classmethod
	def from_config_file(cls, config_path, section):
		with open(config_path) as json_data_file:
			cls.config = json.load(json_data_file)
		major = cls.config[cm]['LATEST'][MAJOR]
		minor = cls.config[cm]['LATEST'][MINOR]
		bugfix = cls.config[cm]['LATEST'][BUGFIX]

		return cls(major, minor, bugfix)

	def get_next_version_string(self, revision):
		if revision == MAJOR:
			return self.next_major_version()
		if revision == MINOR:
			return self.next_minor_version()
		if revision == BUGFIX:
			return self.next_bug_fix_version

	def next_bug_fix_version(self):
		return get_software_version_string(self.major, self.minor, self.bugfix + 1)

	def next_minor_version(self):
		return get_software_version_string(self.major, self.minor + 1, self.bugfix)

	def next_major_version(self):
		return get_software_version_string(self.major + 1, self.minor, self.bugfix)

	def get_current_version_string(self):
		return get_software_version_string(self.major, self.minor, self.bugfix)

	def add_new_version(self, bugfix):
		self.config.add_section(get_software_version_string(self.major, self.minor, bugfix))

	def is_downloaded(self):
		return False
	def get_cm_url(self):
		return self.config[cm]['url']

	def is_cm_version_downloaded(self):
		return self.config[cm]['VERSIONS'][self.current_version]['downloaded']['status']

	def is_cm_version_repackaged(self):
		return self.config[cm]['VERSIONS'][self.current_version]['repackaged']['status']

	def is_cm_version_install_test_passed(self):
		return self.config[cm]['VERSIONS'][self.current_version]['install_test']['status']

	def is_cm_version_deployed_to_tec_dev(self):
		return self.config[cm]['VERSIONS'][self.current_version]['deployed']['tech/dev']

	def get_cm_download_url(self, ):
		print self.get_cm_url() + self.current_version;
