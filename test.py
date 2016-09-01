ACCESS_TOKEN = "EAACEdEose0cBAAI4ZB7krFTZCVGosW70LZBjX0DlhuWqOgaDcxieGerPPyiGLrY127ZBVBAEa2lB8IlNTEOnFxQwiBZAYD2XsFrXjsSUEnt1pd1GMJhatkZBGXxij9LZCiMHs4J3TJQz7Tiu1FhhZC2aKHGw1O28nnlL4nBDZCGZB87AZDZD"

from pyFB import User

x = User(access_token = ACCESS_TOKEN)
print x.info
print x.name
x.religion = 'Hello! Testing!'
print x.save()
