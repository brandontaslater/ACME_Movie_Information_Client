import sqlite3
import json
from os.path import normpath
import os


def FetchAllData(path, table):
    print("Main: Fetching All Data From Table")
    db = sqlite3.connect(str(path))
    cursor = db.cursor()
    cursor.execute('SELECT * FROM '+table)
    all_rows = cursor.fetchall()
    db.close()
    if len(all_rows) == 0:
        all_rows = 0
        print("Main: Finished Fetching All Data From Table")
    return all_rows


def FetchColumnNames(path, table):
    print("Main: Fetching Column Names From Table")
    db = sqlite3.connect(str(path))
    db.row_factory = sqlite3.Row
    cursor = db.execute('select * from '+table)
    # instead of cursor.description:
    row = cursor.fetchone()
    db.close()
    names = row.keys()
    print("Main: Finished Fetching Column Names From Table")
    return names


def CreateTable(path, TableName):
    print("Main: Creating Table")
    if TableName == 'DownloadHistoryTMDb':
        CreateTableString = 'create table if not exists ' + TableName + ' (id INTEGER PRIMARY KEY, vote_count TEXT , IMDbId TEXT , video TEXT , vote_average TEXT , title TEXT , popularity TEXT , poster_path TEXT , original_language TEXT , original_title TEXT , genre_ids TEXT , backdrop_path TEXT , adult TEXT , overview TEXT , release_date TEXT)'
    elif TableName == 'DownloadHistoryOMDb':
        CreateTableString = 'create table if not exists '+TableName+' (id INTEGER PRIMARY KEY, Title TEXT , Year TEXT , Rated TEXT , Released TEXT , Runtime TEXT , Genre TEXT , Director TEXT , Writer TEXT , Actors TEXT , Plot TEXT , Language TEXT , Country TEXT , Awards TEXT , Poster TEXT , Ratings TEXT , Metascore TEXT , imdbRating TEXT , imdbVotes TEXT , imdbID TEXT , Type TEXT , DVD TEXT , BoxOffice TEXT , Production TEXT , Website TEXT , Response TEXT)'
    else:
        CreateTableString = 'create table if not exists ' + TableName + ' (id INTEGER PRIMARY KEY, Title TEXT, IMDbID TEXT, ReleaseDate TEXT, Plot TEXT)'
    db = sqlite3.connect(str(path))
    cursor = db.cursor()
    cursor.execute(CreateTableString)
    db.commit()
    db.close()
    print("Main: Finished Creating Table")


def InsertIntoTable(path, table, data_dict):
    print("Main: Inserting Into Table")
    if table == 'DownloadHistoryTMDb':
        data_dict = EditDictionaryKey(data_dict, 1, "IMDbId")
    list1 = list(data_dict.values())
    if table == 'DownloadHistoryOMDb':
        list1[14] = json.dumps(list1[14])
    elif table == 'DownloadHistoryTMDb':
        list1[0] = json.dumps(list1[0])
        list1[1] = json.dumps(list1[1])
        list1[2] = json.dumps(list1[2])
        list1[3] = json.dumps(list1[3])
        list1[5] = json.dumps(list1[5])
        list1[9] = json.dumps(list1[9])
        list1[11] = json.dumps(list1[11])
    db = sqlite3.connect(str(path))
    columns = ', '.join(data_dict.keys())
    placeholders = ', '.join('?' * len(data_dict))
    cursor = db.cursor()
    sql = 'INSERT INTO '+table+' (%s) VALUES(%s)' % (columns, placeholders)
    cursor.execute(sql, list1)
    db.commit()
    db.close()
    print("Main: Finished Inserting Into Table")


def DeleteData(path, table, position):
    print("Main: Deleting Data")
    db = sqlite3.connect(str(path))
    cursor = db.cursor()
    cursor.execute('DELETE FROM '+table+' WHERE id = ? ', (position,))
    db.commit()
    db.close()
    print("Main: Finished Deleting Data")


def EditDictionaryKey(data_dict, PositionKey, NewValue):
    print("Main: Editing Dictionary Key")
    Keys = list(data_dict.keys())
    Values = list(data_dict.values())
    Keys[PositionKey] = NewValue
    print("Main: Finished Editing Dictionary Key")
    return dict(zip(Keys, Values))


def AddToDictionary(data_dict, PositionKey, list1, list2):
    print("Adding To Dictionary")
    keys = list(data_dict.keys())
    items = list(data_dict.values())
    bottomKey = []
    bottomItem = []
    bottomKey.append(keys[PositionKey])
    keys.pop(PositionKey)
    bottomItem.append(items[PositionKey])
    items.pop(PositionKey)
    mergedKeys = keys + list1 + bottomKey
    mergedItems = items + list2 + bottomItem
    print("Finished Adding to dictionary")
    return dict(zip(mergedKeys, mergedItems))


def main():
    print("Main: Initialisation")
    location = str(os.getcwd()) + "\ACME_Storage.db"
    path = normpath(location)

    db = sqlite3.connect(str(path))
    db.close()
    CreateTable(path, 'DownloadHistoryOMDb')
    CreateTable(path, 'DownloadHistoryTMDb')
    CreateTable(path, 'WishList')
    print("Main: Initialisation Finished")

