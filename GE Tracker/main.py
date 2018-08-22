import urllib.request, json
import datetime
from item import item
from save import save
from save import load
from userInterface import userInterface
import threading
from watchingItems import watchingItems


import os
clear = lambda: os.system('cls')

clear()
print('starting up')
#watchingItems = ['Dragon hunter crossbow', "Zulrah's scales", 'Twisted bow']
watchingItemsPrice = load()
if watchingItemsPrice == []:
    for thing in watchingItems:
        tempItem = item(thing)
        watchingItemsPrice.append(tempItem)
if len(watchingItemsPrice) < len(watchingItems):
    for item1 in watchingItems:
        foundItem = False
        for item2 in watchingItemsPrice:
            if item2.name == item1:
                foundItem = True
                break
        if not(foundItem):
            watchingItemsPrice.append(item(item1))

completeItemList = []
now = datetime.datetime.now()
lastMinute = now.minute - 1

def grabPriceData(): #Returns Dictionary of all Items
    with urllib.request.urlopen("https://rsbuddy.com/exchange/summary.json") as url:
        data = json.loads(url.read().decode())
        return data

def updateCurrentPriceSheet(data):
    dataString = str(data)
    tokens = dataString.split()

def updateWatchingItemsPrice():
    '''
    Returns a list of items:
    Item name: ____ - Item Price: ____ - Last Change: ____
    '''

    data = grabPriceData()
    for i in range(1000000):
        item = data.get(str(i))
        if item != None:
            name = item.get('name')
            overallAverage = item.get('sell_average')
            if name in watchingItems:
                for i in range(len(watchingItems)):
                    if name == watchingItems[i]:
                        watchingItemsPrice[i].overallAverage = overallAverage
                        watchingItemsPrice[i].priceTracker.append((overallAverage, datetime.datetime.now()))
                        watchingItemsPrice[i].setChange()

def initCompleteItemList():
    data = grabPriceData()
    for i in range(1000000):
        ITEM = data.get(str(i))
        if ITEM != None:
            name = ITEM.get('name')
            overallAverage = ITEM.get('sell_average')
            tempItem = item(name)
            tempItem.overallAverage = overallAverage
            tempItem.setChange()
            tempItem.priceTracker.append((overallAverage, datetime.datetime.now()))
            completeItemList.append(tempItem)

def updateCompleteItemList():
    data = grabPriceData()
    for i in range(1000000):
        item = data.get(str(i))
        if item != None:
            name = item.get('name')
            overallAverage = item.get('sell_average')
            for item in completeItemList:
                if item.name == name:
                    item.overallAverage = overallAverage
                    item.setChange
                    item.priceTracker.append((overallAverage, datetime.datetime.now()))
                    break


def printScreen(timer):
    clear()
    names = []
    sellPrices = []
    changes = []
    for item in watchingItemsPrice:
        names.append(item.name)
        sellPrices.append(item.overallAverage)
        changes.append(item.change)

    nameString = 'Name:      '
    for name in names: nameString += name + '     '
    print(nameString)

    sellPricesString = 'Price:     '
    for i in range(len(sellPrices)):
        sellPricesString += str(sellPrices[i]) + (' ' * (len(names[i]) - len(sellPrices)))
    print(sellPricesString)

    changesString = 'Change:     '
    for i in range(len(changes)):
        changesString += str(changes[i]) + (' ' * (len(names[i])))
    print(changesString)
    print(timer)

def printScreenOnlyChanges(i):
    for item in completeItemList:
        if item.change != 0:
            print(item.name, item.overallAverage, item.change)
    print(i)

running = True
UI = userInterface()
UI.changePage(watchingItemsPrice, '')
initCompleteItemList()

def priceUpdater():
    #updating prices every minute
    done = False
    while not(done):
        global lastMinute
        now = datetime.datetime.now()
        if lastMinute != now.minute:
            updateWatchingItemsPrice()
            updateCompleteItemList()
            save(watchingItemsPrice)
            lastMinute = now.minute

t1 = threading.Thread(target=priceUpdater) # args=(i,)
t1.daemon = True
t1.start()

while (running):
    #checking buttons pressed
    userInput = input()
    response = UI.handleUserInput(userInput, watchingItemsPrice)
    userInput = ''
    if response == 'close':
        running = False
