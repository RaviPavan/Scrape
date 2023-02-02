f = open("/Users/ravi/Downloads/Thesaurus-of-Job-Titles-master/synonym_job_titles_for_search_alternative.txt", "r")
f1 = open("/Users/ravi/GITBase/Scrape/SynonmFile-Formatted.txt", "w+")
linecounter =0
maxlines = 100000
for x in f:
  if (x.find('software')>0 or x.find('database')>0 or x.find('programmer')>0 or x.find('developer')>0 \
  or x.find('engineering')>0 or x.find('project')>0  or x.find('architect')>0  or x.find('intern')>0 or x.find('data')>0 \
   or x.find('ceo')>0 or x.find('web')>0 or x.find('founder')>0) and \
  (x.find('health')<0 and x.find('transport')<0 and x.find('care')<0 and x.find('worker')<0 and x.find('technician')<0 \
    and x.find('clinical')<0 and x.find('civil')<0  and x.find('electrical')<0) :
    if x.find('=>')>0 and x.find(',')>0:
        print(x[0:x.index('=>')])
        f1.writelines(x[0:x.index('=>')]+"\n")
    else:
        print("here")
        print(x)
    linecounter+=1
  if linecounter>=maxlines:
    break
print(linecounter)


# Should we club senior /principal /lead/intern altogether in single role (No weightage for synonyms to rank in OS)
# Developer/Architect/Managers/Founders . What are different roles we think to be grouped?
