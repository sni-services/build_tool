import logging
import os
import urllib

from Version import *

print 'Current Working Directory: ' + os.getcwd()

config_file = os.getcwd() + '/resources/version.json'

if os.path.isfile(config_file):
	print "loading config file {0}".format(config_file)
	lv = Version.from_config_file(config_file, "CM_LATEST")
else:
	print "can't find file " + config_file + ' exiting'
	exit(1)

# check the config
print "starting"


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


def check_next_bugfix_version():
	f = urllib.urlopen(get_cloudera_manager_url())
	if f.code == 200:
		logging.info("url exists")
		return True
	else:
		print f.code
		return False


def get_cloudera_manager_url():
	# TODO move this to config json file
	cm_url = lv.config['cloudera_manager']['url']
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
