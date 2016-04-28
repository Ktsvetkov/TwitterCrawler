import threading
import time
import urllib2, httplib2, requests


#requestNumber = 0

def getQuery():
    #content = urllib2.urlopen("https://django-whatsthemove.rhcloud.com/WhatsTheMove/?lat=33.7490&long=-84.3880&radius=0.25&count=100").read()
    #resp, content = httplib2.Http().request("https://django-whatsthemove.rhcloud.com/WhatsTheMove/?lat=33.7490&long=-84.3880&radius=0.25&count=100")
    r = requests.get("https://django-whatsthemove.rhcloud.com/WhatsTheMove/?lat=33.7490&long=-84.3880&radius=0.25&count=100")


    #print content
    #requestNumber += 1
    #print 'Finished - Query ' + str(requestNumber)


#Starting 1 query

incrementorNumber = 0
threads = []

start = time.time()

while incrementorNumber < 1:
    t = threading.Thread(name='thread_' + str(incrementorNumber), target=getQuery)
    t.start()
    threads.append(t)
    incrementorNumber += 1

incrementorNumber = 0

while incrementorNumber < 1:
    threads[incrementorNumber].join()
    incrementorNumber += 1

end = time.time()
print "\nTime taken for query with 1 request: " + str(end - start) + "\n"

#Ending 1 query


#Starting 10 query

incrementorNumber = 0
threads = []

start = time.time()

while incrementorNumber < 10:
    t = threading.Thread(name='thread_' + str(incrementorNumber), target=getQuery)
    t.start()
    threads.append(t)
    incrementorNumber += 1

incrementorNumber = 0

while incrementorNumber < 10:
    threads[incrementorNumber].join()
    incrementorNumber += 1

end = time.time()
print "\nTime taken for query with 10 request: " + str(end - start) + "\n"

#Ending 10 query


#Starting 100 query

incrementorNumber = 0
threads = []

start = time.time()

while incrementorNumber < 100:
    t = threading.Thread(name='thread_' + str(incrementorNumber), target=getQuery)
    t.start()
    threads.append(t)
    incrementorNumber += 1

incrementorNumber = 0

while incrementorNumber < 100:
    threads[incrementorNumber].join()
    incrementorNumber += 1

end = time.time()
print "\nTime taken for query with 100 request: " + str(end - start) + "\n"

#Ending 100 query

#Starting 500 query

incrementorNumber = 0
threads = []

start = time.time()

while incrementorNumber < 500:
    t = threading.Thread(name='thread_' + str(incrementorNumber), target=getQuery)
    t.start()
    threads.append(t)
    incrementorNumber += 1

incrementorNumber = 0

while incrementorNumber < 500:
    threads[incrementorNumber].join()
    incrementorNumber += 1

end = time.time()
print "\nTime taken for query with 500 request: " + str(end - start) + "\n"

#Ending 500 query

#Starting 1000 query

incrementorNumber = 0
threads = []

start = time.time()

while incrementorNumber < 1000:
    t = threading.Thread(name='thread_' + str(incrementorNumber), target=getQuery)
    t.start()
    threads.append(t)
    incrementorNumber += 1

incrementorNumber = 0

while incrementorNumber < 1000:
    threads[incrementorNumber].join()
    incrementorNumber += 1

end = time.time()
print "\nTime taken for query with 1000 request: " + str(end - start) + "\n"

#Ending 1000 query








