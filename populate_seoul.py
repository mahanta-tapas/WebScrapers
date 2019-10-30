import psycopg2,psycopg2.extensions
import csv
import os
import codecs
import sys

def usage(argv0):
    print "Usage: " + argv0 + " <server> <database> <username> <password> <path> "

if __name__ == '__main__':
    if len(sys.argv) < 6:
        usage(sys.argv[0])
    server = sys.argv[1]
    datab = sys.argv[2]
    username = sys.argv[3]
    passw = sys.argv[4]
    write_file = sys.argv[5]
    try:
        conn = psycopg2.connect(database=datab, user=username ,host=server,password=passw)
    except:
        print "database connection failed"

    cur = conn.cursor()

    query = "select * from (select *  from detail left outer join (select * from category_type_map) as B on detail.detail_id = B.detail_id) as A inner join (select * from category_type where category_type.hierarchy_type = 1 and category_type.category_type != 'establishment') as B on A.category_type_id = B.category_type_id"
    #copy query to "home/tapas/seouldata.csv" with delimiter ','	
    outputquery = "COPY ({0}) TO STDOUT WITH CSV DELIMITER '|'".format(query)
    with open(write_file, 'wb') as f:
        cur.copy_expert(outputquery, f)

