import urllib as r, json as j
from Tkinter import *

CHART_WIDTH = 600

def getPrices (symbol):
	data, prices = [], []

	for i in range(0, 31):
		date = "2016-04-%s" % (i)
		data.append(j.loads(r.urlopen("http://api.fixer.io/%s" % (date)).read()))

	for i in data:
		try:
			prices.append(i['rates'][symbol])
		except Exception, e: continue

	return prices

def createWindow (symbol):
	main = Tk()

	main.title("Chart of EUR/%s" % (symbol))
	main.geometry("%ix320" % (CHART_WIDTH))
	main.resizable(width=False, height=False)

	chartCanvas = Canvas(main, width=600, height=CHART_WIDTH)
	chartCanvas.pack(side='bottom')

	priceData = getPrices(symbol)

	index, pricesCount = 0, len(priceData)

	lineTail = [0, (priceData[0] ** 3 * 1000) - 400]

	for i in range(0, pricesCount - 1):
		dx = CHART_WIDTH / pricesCount
		lineHead = [index + dx, (priceData[i + 1] ** 3 * 1000) - 400]
		chartCanvas.create_line(lineTail[0], lineTail[1], lineHead[0], lineHead[1], fill='red')
		index += dx
		print(lineTail)
		lineTail = lineHead
		print(lineTail)

	main.mainloop()

createWindow('GBP')