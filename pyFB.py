import requests
import pprint
import copy

class GraphAPI(object):
	"""docstring for Facebook"""
	VALID_VERSIONS = ['2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7']
	VALID_METHODS = ['GET', 'POST', 'DELETE']
	GRAPH_API_URL = "https://graph.facebook.com/"
	def __init__(self, version, access_token):
		self._access_token = access_token
		for valid_version in self.VALID_VERSIONS:
			if str(version) == valid_version:
				self.version = valid_version
		try:
			self.version
		except AttributeError:
			self.version = self.VALID_VERSIONS[-1]			
	def request(self,params={},post_params={},files=None,path=[],method=None):
		url = self.GRAPH_API_URL+'v'+self.version+'/'+'/'.join(path)
		if not method or method not in self.VALID_METHODS:
			method = "GET"
		if method == 'GET':
			params.setdefault('access_token',self._access_token)
			return requests.get(url,params=params).json()
		elif method ==	'POST':
			post_params.setdefault('access_token',self._access_token)
			return requests.post(url,data=post_params).json()
		elif method == 'DELETE':
			params.setdefault('access_token',self._access_token)
			return requests.delete(url,params=params).json()	

class GraphAPIObject(object):

	def __init__(self,version,path,access_token=None,fields=[]):
		self.infoAPI = GraphAPI(version,access_token)
		self.path = path
		self.info = self.infoAPI.request(method = 'get',path = path,params={'fields':",".join(fields)})
		for k,v in self.info.items():
			setattr(self,k,v)

	def save(self,post_params=None):
		saved_params = copy.copy(vars(self))
		saved_params.pop('infoAPI',None)
		saved_params.pop('info',None)
		if post_params:
			for key in saved_params.keys():
				if key not in post_params:
					del saved_params[key]
		print saved_params				

				
		return self.infoAPI.request(method = 'POST' , path=self.path, post_params = saved_params)

	def delete(self):
		return self.infoAPI.request(method = 'DELETE',path = self.path)	
	
class GraphAPIError(Exception):
	
    def __init__(self, result):
        self.result = result
        self.code = None
        try:
        	self.message = self.result['error']['message']
        	self.type = self.result['error']['type']
        	self.code = self.result['error']['code']
        	self.subcode = self.result['error']['error_subcode']
        	self.traceid = self.result['error']['fbtrace_id']
        except:
        	self.message = self.result	
        Exception.__init__(self, self.message)






