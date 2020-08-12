import requests
import pprint


def req():
    r = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:0156012197&jscmd=data&format=json")
    meta = r.json()['ISBN:0156012197']
    #pprint.pprint(meta)

    for key in meta.keys():
        if key == "title":
            print("Title : {}".format(meta[key]))

        if key == 'publish_date':
            print("Year : {}".format(meta[key]))

        if key == "authors":
            dump = meta[key][0]
            print("Author : {}".format(dump['name']))
            
req()

# output 
#ISBN:
#Title : The Little Prince
#Year : 2000
#Author :Antoine de Saint-Exupéry

