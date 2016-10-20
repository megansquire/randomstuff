# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:59:04 2016

@author: megan

Assumes pre-made db table with the following structure:
CREATE TABLE `simpsons_script` (
  `id` int(11) NOT NULL PRIMARY KEY,
  `episode_id` int(11) DEFAULT NULL,
  `number` int(11) DEFAULT NULL,
  `raw_text` text CHARACTER SET utf8,
  `timestamp_in_ms` int(11) DEFAULT NULL,
  `speaking_line` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `character_id` int(11) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `raw_character_text` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `raw_location_text` varchar(200) CHARACTER SET utf8 DEFAULT NULL,
  `spoken_words` text CHARACTER SET utf8,
  `normalized_text` text CHARACTER SET utf8,
  `word_count` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

"""

import csv
import pymysql
f = open("simpsons_script_lines.csv", 'rt', encoding='utf-8')
reader = csv.DictReader(f, quotechar='"')

# give your db credentials here
db = pymysql.connect(host='',
                     db='simpsons',
                     user='',
                     passwd='',
                     port=3306,
                     charset='utf8mb4',
                     autocommit=True)
cursor = db.cursor()

insertQuery = "INSERT INTO simpsons_script \
                            (id, \
                            episode_id, \
                            number, \
                            raw_text, \
                            timestamp_in_ms, \
                            speaking_line, \
                            character_id,\
                            location_id, \
                            raw_character_text, \
                            raw_location_text, \
                            spoken_words, \
                            normalized_text, \
                            word_count) \
                            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

print("Inserting row number...")
for row in reader:
    row_id = int(row['id'])
    episode_id = int(row['episode_id'])
    number = int(row['number'])
    raw_text = row['raw_text']
    time_in_ms = int(row['timestamp_in_ms'])
    speaking_line = row['speaking_line']
    if row['character_id']:
        character_id = int(row['character_id'])
    else:
        character_id = None
    if row['location_id']:
        location_id = int(row['location_id'])
    else:
        location_id=None
    rct = row['raw_character_text']
    rlt = row['raw_location_text']
    spoken_words = row['spoken_words']
    normalized = row['normalized_text']
    if row['word_count']:
        if row['word_count'].isdigit():
            word_count = int(row['word_count'])
        else:
            word_count = None
    else: 
        word_count = None
    print(row_id)

    data = (row_id, episode_id, number, raw_text,
            time_in_ms, speaking_line,
            character_id, location_id, rct, rlt,
            spoken_words, normalized, word_count)

    try:
        cursor.execute(insertQuery,data)
    except:
        print(">>>>>problem with row #",row_id)
        break
f.close()
