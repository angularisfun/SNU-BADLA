import urllib
import urllib2
import random

a = ["Your Daddy","Your Mommy","Ram Sharma","Your Dick","Justin Beiber"]
b = ["The one your daddy did to make you","the one you watch regularly online","The ones your served in restraunts","Engineering Motherfucker ! "]
c = ["Your Ex","Prince William","Baba Ramdev","Your Future Girlfriend","Mark Zuckerberg"]
d = ["3A","3C","GH2","GH1","Your Mothers Cunt"]
e = ["69","420","100","infinity","Fuck you, i cant count"]
f = ["The Jocker","The Batman","F***69","The Number of balls you have = 0 ","The number of times you got your girfriend pregnant"]
g = ["1234- 69","Password","khul jaa sim sim","what your dad tells your mom every night","the combination to your chastity belt"]
h = ["Mr 5000 $ a Night ","your Moms Number","You deserve a trip to north korea","Your mammas so fat that atomic clocks have to be reset everytime she gets near them "]

n = 0
while(n<=5000):
    redirectionHandler = urllib2.HTTPRedirectHandler() 
    opener = urllib2.build_opener(redirectionHandler)
    urllib2.install_opener(opener)
    query_args = { 'name' : random.choice(a), 'sname':random.choice(b), 'pname':random.choice(c),'hno':random.choice(d),'room':random.choice(e),'netid':random.choice(f),'pass':random.choice(g),'snupass':random.choice(h)}
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    url = "http://snu.site11.com/"
    request = urllib2.Request(url,data=urllib.urlencode(query_args))
    request.add_header('User-agent', user_agent)
    results = urllib2.urlopen(request)
    print "FUCKED HIS ASS"
    n = n+1
print "done"





 

