from build_tool.Version import *
from nose.tools import assert_equals

__author__ = 'Shaine Ismail'


def setup():
	version = Version(1, 2, 3)


def test_version_constructor():
	assert_equals(Version(1, 2, 3).get_current_version_string(), "1.2.3")


def test_next_bugfix_version():
	assert_equals(Version(1, 2, 3).next_bug_fix_version(), "1.2.4")


def test_next_minor_version():
	assert_equals(Version(1, 2, 3).next_minor_version(), "1.3.3")


def test_next_major_version():
	assert_equals(Version(1, 2, 3).next_major_version(), "2.2.3")


def test_config_init():
	v = Version.from_config_file("tests/test_version.conf", "CM_LATEST")
	assert_equals(v.get_current_version_string(), "5.4.5")

# lv.config.set(version_string, "downloaded", False)
# lv.config.set(version_string, "repackage", False)
# lv.config.set(version_string, "install_test", False)
# lv.config.set(version_string, "deployment", False)
