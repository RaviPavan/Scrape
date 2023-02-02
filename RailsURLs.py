f = open("/Users/ravi/GITBase/Scrape/RailsURLs.txt", "r")
linecounter =0
maxlines = 100000
for x in f:
  
  if (x.find('http')>0 ) :
    if x.find('http')>0:
        substr= x[x.index('http'):len(x)]
        print(substr[0:substr.index('"')])
    else:
        continue
    linecounter+=1
  if linecounter>=maxlines:
    break
print(linecounter)