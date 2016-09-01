
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




class User(object):
	"""docstring for User"""
	ALL_USER_FIELDS = []
	def __init__(self, u_id="me",access_token=None,fields = []):
		self.infoAPI = GraphAPI(2.7,access_token)
		self.info = self.infoAPI.request(method = 'get',path = [u_id],params={'fields':",".join(fields)})
		for k,v in self.info.items():
			setattr(self,k,v)

	def save(self):
		saved_params = copy.deepcopy(vars(self))
		saved_params.pop('infoAPI',None)
		saved_params.pop('info',None)
		return self.infoAPI.request(method = 'POST' ,  post_params = saved_params)


		






