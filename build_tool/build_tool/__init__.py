import urllib
import logging
import os
from Version import *
import os

<<<<<<< HEAD
=======
print 'Current Working Directory: ' + os.getcwd()

config_file = os.getcwd() + '/build_tool/resources/version.conf'

if os.path.isfile(config_file):
    lv = Version.from_config_file(config_file, "CM_LATEST")
else:
    print "can't find file " + config_file + ' exiting'
    exit(1)
>>>>>>> 8055a0d14b1a7a867f70ed719a3c7502f2e11e66

# check the config
print "starting"

download_root_directory = "/Volumes/MacHD/cm/"


def main(self):
	# Check if the current version has
	if self.lv == None:

		lv = Version.from_config_file('resources/version.conf', "CM_LATEST")
		print "got here shaine"




<<<<<<< HEAD
	if check_next_bugfix_version():
		# does the version have an entry in the config?
		version_string = "cm-" + lv.next_bug_fix_version
=======
def main():
    if check_next_bugfix_version():
        # does the version have an entry in the config?
        version_string = "cm-" + lv.next_bug_fix_version
>>>>>>> 8055a0d14b1a7a867f70ed719a3c7502f2e11e66

        if lv.config.has_section(version_string):
            pass
        else:
            print "adding new version " + version_string
            # download the files
            download(get_cloudera_manager_url())


def set_config(self, config_file):
	self.config_file = config_file
	self.version_config = Version.from_config_file(config_file, "CM_LATEST")

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
	latest_url = "{}/{}".format(cm_url, lv.next_bug_fix_version)
	print latest_url
	return latest_url
=======
    cm_url = "http://archive.cloudera.com/cm5/redhat/6/x86_64/cm"
    latest_url = "{}/{}".format(cm_url, lv.next_bug_fix_version)
    print latest_url
    return latest_url
>>>>>>> 8055a0d14b1a7a867f70ed719a3c7502f2e11e66


def download(url):
    print url


def install_test():
    pass


def deployment():
    pass


if __name__ == '__main__':
    main()
