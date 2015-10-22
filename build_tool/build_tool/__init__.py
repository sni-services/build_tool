import urllib
import logging
import ConfigParser
# import os
from Version import *

config = ConfigParser.RawConfigParser()
config.read('resources/version.conf')
cm_section = "CM_LATEST"
major = config.getint(cm_section, 'major')
minor = config.getint(cm_section, 'minor')
bugfix = config.getint(cm_section, 'bugfix')

lv = Version(major, minor, bugfix, config)

# check the config
print "starting"


def main():
    if check_next_bugfix_version():
        # does the version have an entry in the config?
        version_string = "cm-" + lv.next_bug_fix_version

        if config.has_section(version_string):
            pass
        else:
            print "adding new version " + version_string
            config.add_section(version_string)
            version_string = "123"
            config.set(version_string, "downloaded", False)
            config.set(version_string, "repackage", False)
            config.set(version_string, "install_test", False)
            config.set(version_string, "deployment", False)
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
    cm_url = "http://archive.cloudera.com/cm5/redhat/6/x86_64/cm"
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
