__author__ = 'shainnif'

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'RBS Big Data Engineer Build',
	'author': 'Shaine Ismail',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'shaine.ismail@rbs.com',
	'version': '0.1',
	'install_requires': ['nose', 'wget'],
	'packages': ['build_tool'],
	'scripts': [],
	'name': 'rbs Build Tools'
}

setup(**config)
