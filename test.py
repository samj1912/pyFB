ACCESS_TOKEN = "EAACEdEose0cBABBK7IDLoA6XYdACLljSjKuJ2UKxiRpeiqfLuxnW6luV6MjDaEjwvaUf9xkBHUGKQjNtY8HyR1v3lfaqWQuaMBEFRA2bpngBQXwn5xW4m9h4LHPFWo05ygN5fpPQJuG5WTXCjhMYeWWwZAY1AMreGa7ZAfUQZDZD"

from pyFB import GraphAPIObject

x = GraphAPIObject(2.7,'me',fields=['bio','name','birthday'], access_token = ACCESS_TOKEN)
y = GraphAPIObject(2.7,['10205121410262892_10210752821564655','comments'], access_token = ACCESS_TOKEN)
# print x.info


# print y.info
print y.data

for j in y.data:
	temp = GraphAPIObject(2.7,[j['id']],access_token=ACCESS_TOKEN)
	temp.delete()

# print z.info
# z.message = "You are love <3"
# print z.save()