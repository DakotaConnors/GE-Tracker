import os
import datetime
clear = lambda: os.system('cls')

class userInterface():
    def __init__(self):
        self.pageNumber = 0.0

    def printItemPriceHistory(self, itemName, watchingItemsPrice):
        #print all prices from the beginning
        '''
        for item in watchingItemsPrice:
            if item.name == itemName:
                print(itemName + '\n')
                lastTime = item.priceTracker[0][1]
                now = datetime.datetime.now()
                print(str(item.priceTracker[0][0]), str(item.priceTracker[0][1].month), '-', item.priceTracker[0][1].day, (str(item.priceTracker[0][1].hour) + ':' + str(item.priceTracker[0][1].minute)))
                for change in item.priceTracker:
                    if change[1].minute % 1 == 0:
                        print(change[0], str(change[1].month), '-', str(change[1].day), (str(change[1].hour) + ':' + str(change[1].minute)))
        '''
        #print last X changes
        listOfPrintedItems = []
        for item in watchingItemsPrice:
            if item.name == itemName:
                print(itemName + '\n')
                lastPrice = 0
                for change in reversed(item.priceTracker):
                    if len(listOfPrintedItems) >= 10:
                        break
                    if lastPrice != change[0]:
                        lastPrice = change[0]
                        listOfPrintedItems.append((change[0],change[1]))
                    #print(change[0], (str(change[1].month) + '-' + str(change[1].day)), (str(change[1].hour) + ':' + str(change[1].minute)), str(changeInPrice))
        for i in range(len(listOfPrintedItems)):
            changeInPrice = 0
            if i < len(listOfPrintedItems)-1:
                changeInPrice = listOfPrintedItems[i][0] - listOfPrintedItems[i+1][0]
            print(listOfPrintedItems[i][0], str(listOfPrintedItems[i][1].month), '-', str(listOfPrintedItems[i][1].day), (str(listOfPrintedItems[i][1].hour) + ':' + str(listOfPrintedItems[i][1].minute)), changeInPrice)

    def sortBestChangesByPercent(self, watchingItemsPrice):
        '''
        The goal of this function is to sort the top X items based off their most
        recent change by percentage
        Print item name and percentage of change
        '''
        bestItemList = []
        itemNamePercentageList = []
        for item in watchingItemsPrice:
            name = item.name
            if len(item.priceTracker) != 0:
                if len(item.priceTracker) == 1: price1 = item.priceTracker[0]
                else: price1 = item.priceTracker[len(item.priceTracker)-1][0]
                price2 = price1
                for price in reversed(item.priceTracker):
                    if price[0] != price1:
                        price2 = price[0]
                        break
                if price1 != 0:
                    change = price1 - price2
                    percent = change / price1
                    itemNamePercentageList.append((name, percent))

        for i in range(len(itemNamePercentageList)-1):
            for j in range(len(itemNamePercentageList)-1):
                if itemNamePercentageList[j][1] > itemNamePercentageList[j-1][1]:
                    temp = itemNamePercentageList[j]
                    itemNamePercentageList[j] = itemNamePercentageList[j-1]
                    itemNamePercentageList[j-1] = temp

        for i in range(10

        ):
            bestItemList.append(itemNamePercentageList[i])
        return bestItemList

    def checkItemsOnTheRise(self, watchingItemsPrice):
        bestItemsOnTheRise = []
        itemsOnTheRise = []

        for item in watchingItemsPrice:
            name = item.name
            rise = False
            riseNumber = 0
            if len(item.priceTracker) != 0:
                lastPrice = item.priceTracker[len(item.priceTracker)-1][0] #newer price
                for price in reversed(item.priceTracker):
                    if price[0] != lastPrice:
                        if price[0] < lastPrice: #older price is less than newer price
                            rise = True
                            riseNumber += 1
                            lastPrice = price[0]
                        else:
                            #print(name, 'is not on the rise')
                            break
                itemsOnTheRise.append((name, riseNumber))

        for i in range(len(itemsOnTheRise)-1):
            for j in range(len(itemsOnTheRise)-1):
                if itemsOnTheRise[j][1] < itemsOnTheRise[j+1][1]:
                    temp = itemsOnTheRise[j]
                    itemsOnTheRise[j] = itemsOnTheRise[j+1]
                    itemsOnTheRise[j+1] = temp

        return itemsOnTheRise

    def checkItemsOnTheFall(self, watchingItemsPrice):
        bestItemsOnThefall = []
        itemsOnThefall = []

        for item in watchingItemsPrice:
            name = item.name
            fall = False
            fallNumber = 0
            if len(item.priceTracker) != 0:
                lastPrice = item.priceTracker[len(item.priceTracker)-1][0] #newer price
                for price in reversed(item.priceTracker):
                    if price[0] != lastPrice:
                        if price[0] > lastPrice: #older price is less than newer price
                            fall = True
                            fallNumber += 1
                            lastPrice = price[0]
                        else:
                            #print(name, 'is not on the fall')
                            break
                itemsOnThefall.append((name, fallNumber))

        for i in range(len(itemsOnThefall)-1):
            for j in range(len(itemsOnThefall)-1):
                if itemsOnThefall[j][1] < itemsOnThefall[j+1][1]:
                    temp = itemsOnThefall[j]
                    itemsOnThefall[j] = itemsOnThefall[j+1]
                    itemsOnThefall[j+1] = temp

        return itemsOnThefall

    def checkTrend(self, itemName, watchingItemsPrice):
        for item in watchingItemsPrice:
            if item.name == itemName:
                trend = 0
                i = 0
                lastPrice = item.priceTracker[len(item.priceTracker)-1][0]
                for price in reversed(item.priceTracker):
                    if i >= 10: break
                    if price[0] < lastPrice:
                        lastPrice = price[0]
                        trend += 1
                        i+=1
                    elif price[0] > lastPrice:
                        lastPrice = price[0]
                        trend -= 1
                        i+=1

                return trend

    def changePage(self, watchingItemsPrice, itemName):
        clear()
        pageString = ''
        if self.pageNumber == 0.0:
            pageString += 'Welcome to the GE Tracker! What would you like to do?\n\n'
            pageString += '(1) Search Item\n'
            pageString += '(2) Check top 10 List\n'
            pageString += '(3) Check items on the rise\n'
            pageString += '(4) Check items on the fall'

        elif self.pageNumber == 1.0: #searching for an item
            pageString += 'What item would you like to seach for?\n\n'

        elif self.pageNumber == 1.1: #viewing a searched item
            self.printItemPriceHistory(itemName, watchingItemsPrice)
            trend = self.checkTrend(itemName, watchingItemsPrice)
            print('Current Trend: ', trend,'\n')
            print('(1) Back to Main Menu')

        elif self.pageNumber == 2.0: #viewing top 10 list
            print('Top 10 Items in the last change\n')
            bestItemList = self.sortBestChangesByPercent(watchingItemsPrice)
            for item in bestItemList:
                print(item)
            pageString += '\n(1) Back to main menu'
        elif self.pageNumber == 3.0: #viewing items on the rise
            print('Current items on the rise\n')
            itemsOnTheRise = self.checkItemsOnTheRise(watchingItemsPrice)
            for item in itemsOnTheRise:
                if item[1] != 0: print(item)
            pageString += '\n(1) Back to main menu'

        elif self.pageNumber == 4.0: #viewing items on the fall
            print('Current items on the fall\n')
            itemsOnTheFall = self.checkItemsOnTheFall(watchingItemsPrice)
            for item in itemsOnTheFall:
                if item[1] != 0: print(item)
            pageString += '\n(1) Back to main menu'

        print(pageString)

    def handleUserInput(self, userInput, watchingItemsPrice):
        if userInput == 'close' or userInput == 'quit':
            return 'close'
        if self.pageNumber == 0.0:
            if userInput == '1':
                self.pageNumber = 1.0
                self.changePage(watchingItemsPrice, '')
            elif userInput == '2':
                self.pageNumber = 2.0
                self.changePage(watchingItemsPrice, '')
            elif userInput == '3':
                self.pageNumber = 3.0
                self.changePage(watchingItemsPrice, '')
            elif userInput == '4':
                self.pageNumber = 4.0
                self.changePage(watchingItemsPrice, '')

        elif self.pageNumber == 1.0: #searching for item
            self.pageNumber = 1.1 #view searched item static
            self.changePage(watchingItemsPrice, userInput)

        elif self.pageNumber == 1.1:
            if userInput == '1':
                self.pageNumber = 0.0
                self.changePage(watchingItemsPrice, '')

        elif self.pageNumber == 2.0:
            if userInput == '1':
                self.pageNumber = 0.0
                self.changePage(watchingItemsPrice, '')

        elif self.pageNumber == 3.0:
            if userInput == '1':
                self.pageNumber = 0.0
                self.changePage(watchingItemsPrice, '')

        elif self.pageNumber == 4.0:
            if userInput == '1':
                self.pageNumber = 0.0
                self.changePage(watchingItemsPrice, '')

        return ''
