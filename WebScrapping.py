import requests
from requests.exceptions import HTTPError
import bs4

def getquote(l=[]):
    for i in range(len(l)):
        yield l[i].getText()

def web_scrap(url):
    result= requests.get(url)
    soup = bs4.BeautifulSoup(result.text,"lxml")
    try:
        list_quotes = soup.select('.text')
        list_author = (soup.select('.author'))
        list_tags = (soup.select('.tag-item'))
    except HTTPError as httperror:
        print(f"Http error has occured :{httperror}")
    except Exception as err:
        print(f"Other exception has occured : {err}")
    else:
        return [list_quotes,list_author,list_tags]


if __name__=="__main__":
    #print(web_scrap())
    pagenumber=1
    while True:
        url = "http://quotes.toscrape.com/page/"+str(pagenumber)
        list_items=[]
        list_items=web_scrap(url)
        try:
            for i in range(len(list_items)):
                if(len(list_items[i]))==0:
                    raise Exception
                iter=getquote(list_items[i])
                if i==0:
                    item="Quote"
                elif i==1:
                    item="Author"
                else:
                    item="Tags"
                n=1
                for i in iter:
                    print (f"{item} {n} :{i}")
                    n+=1
        except TypeError as type:
            print(f"The Page does not have the required class item, the list iteration gives error {type}")
            break
        except Exception as e:
            print(f"The Page does not have the required class item, the list iteration gives error {e}")
            break
        else:
            pagenumber+=1
            print(f"Fetching items from page {pagenumber}")
        

