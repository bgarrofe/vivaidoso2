import urllib2
import re

IP_PATTERN = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
DEFAULT_PAC = 'http://proxy-bluecoat.cvrd.br/rio002.pac'

class ProxySettings(object):
	
	def __init__(self, pac=DEFAULT_PAC):
		self.pac = pac
		self.proxy = ''
	
	def get_ip(self):
		response = urllib2.urlopen(self.pac)
		html = response.read()
		searchObj = re.search(IP_PATTERN, html)
		self.proxy = searchObj.group()
		return self.proxy

if __name__ == '__main__':
	myproxy = ProxySettings(DEFAULT_PAC)
	print myproxy.get_ip()