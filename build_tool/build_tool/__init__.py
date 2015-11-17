import logging
import os
<<<<<<< HEAD
import Version
import os
=======
import urllib

from Version import *
>>>>>>> feature/download_latest_version

print 'Current Working Directory: ' + os.getcwd()

config_file = os.getcwd() + '/resources/version.json'

if os.path.isfile(config_file):
<<<<<<< HEAD
=======
	print "loading config file {0}".format(config_file)
>>>>>>> feature/download_latest_version
	lv = Version.from_config_file(config_file, "CM_LATEST")
else:
	print "can't find file " + config_file + ' exiting'
	exit(1)
<<<<<<< HEAD

download_root_directory = "/tmp/"
=======
>>>>>>> feature/download_latest_version


def main(self):
	# Check if the current version has
	if self.lv is None:
		lv = Version.from_config_file('resources/version.conf', "CM_LATEST")
		print "got here shaine"
	version_string = "cm-" + lv.next_bug_fix_version

<<<<<<< HEAD
	if lv.config.has_section(version_string):
		pass
	else:
		print "adding new version " + version_string
		# download the files
		download(get_cloudera_manager_url())


def set_config(self, config_file):
	self.config_file = config_file
	self.version_config = Version.from_config_file(config_file, "CM_LATEST")
=======
def main():
	if check_next_bugfix_version():
		# does the version have an entry in the config?
		version_string = "cm-" + lv.next_bug_fix_version

		if lv.config.has_section(version_string):
			pass
		else:
			print "adding new version " + version_string
			# download the files
			download(get_cloudera_manager_url())
>>>>>>> feature/download_latest_version


def check_next_bugfix_version():
	f = urllib.urlopen(get_cloudera_manager_url())
	if f.code == 200:
		logging.info("url exists")
		return True
	else:
		print f.code
		return False


def get_cloudera_manager_url():
<<<<<<< HEAD
	# create the directory
	if not os.path.exists(download_root_directory):
		os.makedirs(download_root_directory)
	if not os.path.exists(download_root_directory + "/" + lv.next_bug_fix_version):
		os.makedirs(download_root_directory + "/" + lv.next_bug_fix_version)

	cm_url = "http://archive.cloudera.com/cm5/redhat/6/x86_64/cm"
=======
	# TODO move this to config json file
	cm_url = lv.config['cloudera_manager']['url']
>>>>>>> feature/download_latest_version
	latest_url = "{}/{}".format(cm_url, lv.next_bug_fix_version)
	print latest_url
	return latest_url


def download(url):
	print url


def install_test():
	pass


def deployment():
	pass


if __name__ == '__main__':
	main()
