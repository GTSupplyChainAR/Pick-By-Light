#!/usr/bin/python
import sys
import json

def jsonInputHandler(filename):
    """Take json file containing tasks which contain orders and return dictionaries
    {
        "tasks": [
            {
                "orders": [
                    {
                        "A32": 1,
                        "B31": 2,
                        "target": "C11"
                    },
                    {
                        "A41": 3,
                        "target": "C12"
                    }
                ]
            }
        ]
    }

    Keyword arguments:
    filename - name of json file

    Returns:
    returnList - nested list of separate orders
    """
    returnList = []
    with open(filename) as fh:
        jsonDict = json.load(fh)
    
    taskList = jsonDict['tasks']
    for orderDict in taskList:
        orderList = list(orderDict.values())[0]
        
        for order in orderList:
            rackList = list(order.keys())
            rackList.remove('target')

            returnList.append(rackList)

    return returnList

def compareBarcode(checkList):
    """Take a list of order lists and iterate through to check if barcodes match orders. If not, beep on laptop

    Keyword arguments:
    checkList - nested list of separate orders

    Returns:
    None
    """

    for order in checkList:
        while order != []:
            print(order)
            barcode = input("Barcode: ")[4:]
            if barcode not in order:
                print("\a")
            else:
                order.remove(barcode)

def main(argv):
    checkList = jsonInputHandler('pick_tasks.json')
    compareBarcode(checkList)

if __name__ == "__main__":
    main(sys.argv)