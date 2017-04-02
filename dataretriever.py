# Data Retriever
# The module can be used to retrieve data from different forecasters.

# Presently the ASAP Forecasts are being downloaded,
# other data could be downloaded using the retriever method

import urllib2
from sys import argv
from time import sleep
from bs4 import BeautifulSoup

class DataRetriever:

	def __init__(self):
        # Download data to a user specified local directory
        # Provide destination in such formats:
        #   ubuntu : /home/ASAP_data
        #   windows: C:/ASAP_data/

		self.dest = argv[1]

	def retriever(self, asap, dest):
		response = urllib2.urlopen(asap)
		h = response.info()
		totalsize = int(h["Content-Length"])
		print "Downloading {0} bytes...".format(totalsize),
		file_open = open(dest, 'wb')
		blocksize = 8192    # Reading chunks of 8192 bytes
		count = 0
		while True:
			chunk = response.read(blocksize)
			if not chunk:
				break
			file_open.write(chunk)
			count += 1
			if totalsize > 0:
				percent = int(count * blocksize * 100 / totalsize)
				percent = min(percent, 100)
				print "{0}%".format(percent),
			if percent < 100:
				print "\b",
			else:
				print "Done."
		file_open.flush()
		file_open.close()

	def dsd_retriever(self):
		for year in range (2015,2017):
			for month in range (1, 13):
				if (month < 10):
					month = '0' + str(month)
				temp_url = "https://iswa.gsfc.nasa.gov/iswa_data_tree/model/solar/asap/flare-monitor-data/{0}/{1}"
				temp_url = temp_url.format(year,month)
				page = urllib2.urlopen(temp_url)
				forecast = BeautifulSoup(page, "lxml")
				all_days = forecast.find_all("a")
				days = []  
				for link in all_days:
				days.append(link.get("href"))
				for day in days:
					if day[0] == '2':
						asap = temp_url + '/' + day
						print asap
						dest = "{0}/ASAP_FORECAST_{1}.txt".format(self.dest,day)
						print "\nDownloading ASAP FORECAST {0} data :".format(year)
						self.retriever(asap, dest)
						#Providing sleep time to prevent forced session termination
						sleep(3)

						 			


if __name__ == '__main__':
	retrieve = DataRetriever()
	retrieve.dsd_retriever()
