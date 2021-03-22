from task3_files.classes import game
import json



# Data read from json   
def dataRead(jsonFileName):
    gamestmp = []
    with open(jsonFileName) as json_data:
        data = json.load(json_data)

    for x in data['Games']:
        gamestmp.append(game.Game(x['name'], x['platform'], x['genre'], x['price'], x['release_date'], x['availability'], x['pegi']))
    
    return gamestmp
    


# Data write into json
def dataWrite(games, jsonFileName):
    datatoWrite = {}
    datalist= []

    for item in games:
        tempdata={}
        tempdata['name'] = item.name
        tempdata['platform'] = item.platform
        tempdata['genre'] = item.genre
        tempdata['price'] = item.price
        tempdata['release_date'] = item.release_date
        tempdata['availability'] = item.availability
        tempdata['pegi'] = item.pegi
        datalist.append(tempdata)

    datatoWrite ['Games'] = datalist

    with open(jsonFileName, 'w') as data_output:
        json.dump(datatoWrite, data_output, indent=2)