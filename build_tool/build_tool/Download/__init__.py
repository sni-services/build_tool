class Download(object):
	def __init__(self, output_directory):
		self.urls = []
		self.output_directory = output_directory
		super(Download, self).__init__()

	def add_file_to_download_list(self, url):
		self.urls.append(url)

	def download_all_files(self):
		for url in self.urls:
			print url





