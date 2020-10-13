# STEPS TAKEN:
# 1. Downloaded VUnets overview of all courses "vu_net_all_courses.html"
# 2. Find all divs with target class
# 3. Extract the innerHTML (course id)
# %%
from rdflib import Graph, RDF, Namespace, Literal, URIRef
import requests
from bs4 import BeautifulSoup

with open("vu_net_all_courses.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

course_ids_divs = soup.findAll("div", "code ng-binding")

course_ids = [x.contents[0].split()[0] for x in course_ids_divs]

# %%
# BUILDING THE ONTOLOGY


course_url_schema = "https://studiegids.vu.nl/en/2020-2021/courses/"

g = Graph()

# VUC = VUCourses
VUC = Namespace(course_url_schema)
g.bind('vuc', VUC)

# VUP = VUProperties
VUP = Namespace('https://www.vu.nl/en/properties/')
g.bind('vup', VUP)

# defining all namespaces
TEACH = Namespace('http://linkedscience.org/teach/ns#')
g.bind('teach', TEACH)

AIISO = Namespace('http://purl.org/vocab/aiiso/schema#')
g.bind('aiiso', AIISO)

DBO = Namespace("http://dbpedia.org/ontology/")
g.bind('dbo', DBO)

DBR = Namespace("http://dbpedia.org/resource/")
g.bind('dbr', DBR)

# URIRef is used for course_id because the course_id is dynamic and VUC.course_id would add the
# triple (course_id, property, object) and not (AM_470604, property, object)

for i, course_id in enumerate(course_ids):
    print(f"Scraped page {i} of {len(course_ids)}", end="\r", flush=True)
    course_page = requests.get(course_url_schema + course_id)
    if course_page.status_code != 200:
        continue
    soup = BeautifulSoup(course_page.text, "html.parser")
    try:
        # course is a course
        g.add((URIRef(VUC + course_id), RDF.type, TEACH.Course))
        # name of the course
        g.add((URIRef(VUC + course_id), TEACH.courseTitle,
               Literal(soup.find(id="title").find("h2").contents[0])))
        # general information (left box in studyguide) stores all DATA -> course_code, credits, period...
        general_information = soup.find("div", "course-data").findAll("td")
        # getting inner HTML for all data
        general_information = [x.text for x in general_information]
        g.add((URIRef(VUC + course_id), TEACH.ects,
               Literal(int(general_information[1].split()[0]))))
        # academicTerm is string because can be "whole academic year" or "P(eriod)3"
        g.add((URIRef(VUC + course_id), TEACH.academicTerm,
               Literal(general_information[2])))
        # just using VU.course level because I could not find something on the vocabularies
        g.add((URIRef(VUC + course_id), VUP.course_level,
               Literal(int(general_information[3]))))
        # language is using the dbr recourse
        language_dbr_format = general_information[4].split()[0] + '_language'
        g.add((URIRef(VUC + course_id), DBO.language,
               URIRef(DBR + language_dbr_format)))
        # course is taught by faculty
        # TODO instead of literal use vu websites for the faculties?
        g.add((URIRef(VUC + course_id), VUP.faculty,
               Literal(general_information[5])))
    except:
        pass
    # instead of professor responsible for course (doesnt exist in vocabularies)
    # i just add who is teaching the course (can be multiple persons)
    # i scrape all information about course coordinator and teacher both are sometimes
    # empty on given courses but at least one of them is always filled in
    # TODO here too teachers as page? but we have page so just leave it as literal?
    teachers = general_information[6]
    # some courses dont have that information
    try:
        teachers += general_information[8].split('\n')[:-1]
    except:
        pass
    for teacher in teachers:
        g.add(((URIRef(VUC + course_id)), TEACH.teacher, Literal(teacher)))
    course_description = soup.find(
        id="course-description").findAll("div", "paragraph")
    # deleting <br> and <h3> tags
    for section in course_description:
        for br in section.findAll("br"):
            br.extract()
        for h3 in section.findAll("h3"):
            h3.extract()
    try:
        g.add((URIRef(VUC + course_id), VUP.course_objective,
               Literal(" ".join(course_description[0].text.split()))))
        g.add((URIRef(VUC + course_id), VUP.course_content,
               Literal(" ".join(course_description[1].text.split()))))
        g.add((URIRef(VUC + course_id), VUP.teaching_methods,
               Literal(" ".join(course_description[2].text.split()))))
        g.add((URIRef(VUC + course_id), TEACH.grading,
               Literal(" ".join(course_description[3].text.split()))))
    except:
        pass
    # sometimes not provided
    try:
        g.add((URIRef(VUC + course_id), VUP.literature,
               Literal(" ".join(course_description[4].text.split()))))
        g.add((URIRef(VUC + course_id), VUP.target_audience,
               Literal(" ".join(course_description[5].text.split()))))
        g.add((URIRef(VUC + course_id), VUP.recommended_background,
               Literal(" ".join(course_description[6].text.split()))))
    except:
        pass
# %%

with open('vu_studyguide', 'w') as f:
    g.serialize('vu_studyguide', format='turtle')
