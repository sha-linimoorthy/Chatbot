from random import randint

a0="to decrease in amount"

a1=["Abate","Moderate","decrease","diminish","discount","downsize","dwindle","knock down",
"lessen","lower", "lessened","reduced","subdued",
"alleviated","eased","lightened","toned down",
"moderated", "qualified",
"shallow", "superficial",
"feeble", "weak in quantity"]

a2=["advance","develop","enlarge","expand","exten",
"forward",
"grow",
"increase"]

a3="to increase in amount"

c0="Better qualified"

c2=[ "ace", "adept", "experienced", "expert", "master", "masterful", "masterly", "practiced", "proficient", "seasoned", "skilled", "skillful", "veteran","overqualified",
"prepared", "schooled", "trained",
"apt", "ready", "willing","capable",
"all-around", "protean", "versatile"]

c1=["inexpert", "unseasoned", "unskilled", "unskillful",
"unprepared", "unschooled", "untrained",
"beginning", "green", "new", "raw", "untested", "untried"]

c3="Not better qualified"

text=input()
n=randint(0,8)
if text in a1:
    print("Meaning : ",a0)
    print("synonyms : ",a1[n])
    print("antonyms : ",a2[n])
elif text in a2:
    print("Meaning : ",a3)
    print("synomyms : ",a2[n])
    print("antonyms : ",a1[n])
elif text in c2:
    print("Meaning : ",c0)
    print("synomyms : ",c2[n])
    print("antonyms : ",c1[n])
elif text in c2:
    print("Meaning : ",c3)
    print("synomyms : ",c1[n])
    print("antonyms : ",c2[n])   
    
    
    
