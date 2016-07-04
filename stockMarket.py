import urllib as r, json

data = []

for i in range(0, 31):
	date = "2016-03-%s" % (i)
	data.append(json.loads(r.urlopen("http://api.fixer.io/%s" % (date)).read())

print(data)