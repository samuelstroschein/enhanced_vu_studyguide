# How to run

This project is hosted using vercel at the following [url](https://enhanced-vu-studyguide.vercel.app). One can view and interact with the application there. 

It is not required to run the code locally but is is possible. 
In order to run this code locally one is required to clone the git and run the following commands in terminal while in the website folder:
```
> npm install
```

```
> npm run dev
``` 

After running the last command the website will open on localhost port 3000. One can view the website on there, it is essentially the same as the hosted version. One tiny difference is, is that the arrows do turn when expanding the treeview. This is because vercel does not parse the dynamic treeview correctly. 

The endpoint is also hosted at vercel using the following [url](https://enhanced-vu-studyguide.vercel.app/api/sparql). If you open the endpoint without any query parsed into t he link it shows a quick explanation of the endpoint itsself. 

The scraping folder can be ignored but is used to fetch all webpages at [Vu Studyguide](https://studiegids.vu.nl/en) using all the codes of courses at the vrije universiteit, these codes have been obtained by manually downloading all html code at the sign up for extracurricular courses in the sign up for courses page at [VuNet](vunet.vu.nl). The scraper will create a ttl file with only direct triples, any inferred triples have to be added manually using Protegé (or any other program that can do the same). If one would want to run the scraper again you need to navigate to the scraper folder using terminal and run:

```
>python script.py
```

# Default Query used by application 
```SPARQL
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX teach: <http://linkedscience.org/teach/ns#>
PREFIX vu: <https://www.vu.nl/en/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select DISTINCT ?StudieGids_URL ?Credits ?Level ?Period ?Title ?Grading ?Content ?Objective ?Teaching_Method ?Literature ?Language ?Faculty where { 
	?StudieGids_URL rdf:type vu:CourseCredits;
    				teach:ects ?Credits.
    ?StudieGids_URL rdf:type vu:CourseLevel;
    				vu:courseLevel ?Level.
    ?StudieGids_URL rdf:type vu:CoursePeriod;
             		teach:academicTerm ?Period.
    ?StudieGids_URL rdf:type teach:Course;
          			dbo:language ?LanguageName;
          			teach:courseTitle ?Title.
           OPTIONAL {
        	?StudieGids_URL teach:grading ?Grading;
            vu:courseContent ?Content;
            vu:courseObjective ?Objective;
            vu:offeredByFaculty ?FacultyName;
            vu:literature ?Literature;
            vu:teachingMethods ?Teaching_Method.
			?FacultyName rdfs:label ?Faculty.
			?LanguageName rdfs:label ?Language.
    		}   
    FILTER (?Credits = '6'^^xsd:integer || ?Credits = '3'^^xsd:integer)
    FILTER (?Level = '600'^^xsd:integer || ?Level = '500'^^xsd:integer || ?Level = '400'^^xsd:integer || ?Level = '300'^^xsd:integer || ?Level = '200'^^xsd:integer || ?Level = '100'^^xsd:integer)
    FILTER (?Period = 'P1'@en || ?Period = 'P2'@en || ?Period = 'P3'@en || ?Period = 'P4'@en || ?Period = 'P5'@en || ?Period = 'P6'@en)
    FILTER (?Language = 'Dutch'@en || ?Language = 'English'@en)
} limit 100
```


