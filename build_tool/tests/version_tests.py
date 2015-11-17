from build_tool.Version import *
from nose.tools import assert_equals
import os

__author__ = 'Shaine Ismail'


def test_version_constructor():
	assert_equals(Version(1, 2, 3).get_current_version_string(), "1.2.3")


def test_next_bugfix_version():
	assert_equals(Version(1, 2, 3).next_bug_fix_version(), "1.2.4")


def test_next_minor_version():
	assert_equals(Version(1, 2, 3).next_minor_version(), "1.3.3")


def test_next_major_version():
	assert_equals(Version(1, 2, 3).next_major_version(), "2.2.3")


def test_config_init():
	v = Version.from_config_file(os.getcwd() + "/tests/test_version.json", "CM_LATEST")
	assert_equals(v.get_current_version_string(), "5.4.5")


def test_config_cm_url():
	v = Version.from_config_file(os.getcwd() + "/tests/test_version.json", "CM_LATEST")
	assert_equals(v.get_cm_url(), "http://goes.no.where.com")


def test_config_latest_cm_downloaded():
	v = Version.from_config_file(os.getcwd() + "/tests/test_version.json", "CM_LATEST")
	assert_equals(v.is_cm_version_downloaded(), False)


def test_config_latest_cm_repackage_successful():
	v = Version.from_config_file(os.getcwd() + "/tests/test_version.json", "CM_LATEST")
	assert_equals(v.is_cm_version_repackaged(), False)


def test_config_latest_cm_install_test_passed():
	v = Version.from_config_file(os.getcwd() + "/tests/test_version.json", "CM_LATEST")
	assert_equals(v.is_cm_version_install_test_passed(), False)


def test_config_latest_cm_deployed_to_tec_dev():
	v = Version.from_config_file(os.getcwd() + "/tests/test_version.json", "CM_LATEST")
	assert_equals(v.is_cm_version_deployed_to_tec_dev(), False)
