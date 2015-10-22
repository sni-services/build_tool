__author__ = 'Shaine Ismail'

import unittest
from build_tool.Version import *


class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.version = Version(1, 2, 3)
		self.config_version = Version.from_config_file("tests/test_version.conf", "CM_LATEST")

	def test_version_constructor(self):
		self.assertEqual(self.version.get_current_version_string(), "1.2.3")

	def test_next_bugfix_version(self):
		self.assertEqual(self.version.next_bug_fix_version(), "1.2.4")

	def test_next_minor_version(self):
		self.assertEqual(self.version.next_minor_version(), "1.3.3")

	def test_next_major_version(self):
		self.assertEqual(self.version.next_major_version(), "2.2.3")

	def test_config_init(self):
		self.assertEquals(self.config_version.get_current_version_string(), "5.4.5")
		self.assertEqual(self.config_version.isDownloaded(), False )

	# lv.config.set(version_string, "downloaded", False)
	# lv.config.set(version_string, "repackage", False)
	# lv.config.set(version_string, "install_test", False)
	# lv.config.set(version_string, "deployment", False)


if __name__ == '__main__':
	unittest.main()
