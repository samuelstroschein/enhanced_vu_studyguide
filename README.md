# Ontology

**LEGEND**:  
-> implied (needs to be programmed?)


### Prefixes

PREFIX vuc <https://studiegids.vu.nl/en/2020-2021/courses/>  
PREFIX vu <https://www.vu.nl/>  
PREFIX aiiso <https://vocab.org/aiiso/schema#>  
PREFIX teach <http://linkedscience.org/teach/ns/#>  

### Classes
1. teach:Course  
  1.1 vu:ScienceCourse -> ?course vu:offeredBy vu:Faculty_Of_Science  
  1.2 vu:BusinessCourse -> ?course vu:offeredBy vu:Faculty_Of_Business   
  1.3 vu:TheologyCourse -> ?course vu:offeredBy vu:Faculty_Of_Theology  
  1.4 vu:HumanitiesCourse -> ?course vu:offeredBy vu:Faculty_Of_Humanities  
    
2. teach:Teacher  
  -> every ?person who is aiiso:teaching a Course, ?person is a teach:Teacher
  -> every course that is vu:taughtBy ?person, ?person is a teach:Teacher
  
3. aiiso:Faculty


# Example Query 
```SPARQL
PREFIX vu: <https://www.vu.nl/en/properties/>
PREFIX vuc: <https://studiegids.vu.nl/en/2020-2021/courses/>
PREFIX teach: <http://linkedscience.org/teach/ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
select DISTINCT * where { 
	?course teach:ects ?credits ;
         	vu:courseLevel ?level;
          	teach:academicTerm ?period;
           	teach:courseTitle ?title;
            vu:taughtBy ?teacher;
            dbo:language ?language;
            teach:grading ?grading;
            vu:courseContent ?content;
            rdf:type teach:Course;
            vu:courseObjective ?objective;
            vu:offeredByFaculty ?faculty;
            vu:literature ?literature;
            vu:teachingMethods ?teachingMethod.
} LIMIT 100
```

link to endpoint [click](https://enhanced-vu-studyguide.vercel.app/api/sparql)
make sure that you add ?query={your_query} to the endpoint. Important do not define the prefixes, instead just start the query with SELECT * WHERE{} and use whitespace!
