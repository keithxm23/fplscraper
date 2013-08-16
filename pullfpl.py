import simplejson as json
import requests, time
#import cPickle as pickle

url = 'http://fantasy.premierleague.com/web/api/elements/%d/'
i=1
r = requests.get(url %(i,))
elements = []
#for i in xrange(100):
while r.status_code == 200:
  try:
    r = requests.get(url % (i,))
    elements.append(r.json())
    print i
    i+=1
    trycount = 1
  except json.scanner.JSONDecodeError:
    print 'no data at ' + str(i) + ' waiting 2 seconds and trying again for the ' + str(trycount) +' time'
    time.sleep(2)
    trycount+=1
    if trycount > 5:
      print "Tried 5 times.. ending this"
      break
      
if trycount <= 5:
  print 'Broke out of loop since status code not 200 but ' + str(r.status_code)

with open('data.json','w') as outfile:
  json.dump(elements, outfile)
#pickle.dump(elements, open("pickle.p", "wb"))  