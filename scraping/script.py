# STEPS TAKEN:
# 1. Downloaded VUnets overview of all courses "vu_net_all_courses.html"
# 2. Find all divs with target class
# 3. Extract the innerHTML (course id)
# %%
from rdflib import Graph, RDF, Namespace, Literal, URIRef
import requests
from bs4 import BeautifulSoup
import pickle

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

# VU = everything from the vu that is not a course
VU = Namespace('https://www.vu.nl/en/properties/')
g.bind('vu', VU)

# defining all namespaces
TEACH = Namespace('http://linkedscience.org/teach/ns#')
g.bind('teach', TEACH)

AIISO = Namespace('http://purl.org/vocab/aiiso/schema#')
g.bind('aiiso', AIISO)

DBO = Namespace("http://dbpedia.org/ontology/")
g.bind('dbo', DBO)

DBR = Namespace("http://dbpedia.org/resource/")
g.bind('dbr', DBR)

RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
g.bind('rdfs', RDFS)

# URIRef is used for course_id because the course_id is dynamic and VUC.course_id would add the
# triple (course_id, property, object) and not (AM_470604, property, object)

for i, course_id in enumerate(course_ids):
    print(f"Scraped page {i} of {len(course_ids)}", end="\r", flush=True)
    course_page = requests.get(course_url_schema + course_id)
    if course_page.status_code != 200:
        continue
    soup = BeautifulSoup(course_page.text, "html.parser")
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
    g.add((URIRef(VUC + course_id), VU.courseLevel,
           Literal(int(general_information[3]))))
    # language is using the dbr recourse
    try:
        lang_label = general_information[4].split()[0]
        language_dbr_format = lang_label + '_language'
        g.add((URIRef(VUC + course_id), DBO.language,
               URIRef(DBR + language_dbr_format)))
        g.add((URIRef(DBR + language_dbr_format), RDFS.label,
               Literal(lang_label)))
    except:
        pass
    try:
        label = general_information[5]
        faculty_uri = "_".join(label.split())
        g.add((URIRef(VUC + course_id), VU.offeredByFaculty,
               URIRef(VU + faculty_uri)))
        g.add((URIRef(VU + faculty_uri), RDFS.label,
               Literal(label)))
    except:
        pass
    try:
        teachers = general_information[6]
    except:
        pass
    try:
        teachers = (teachers + general_information[8]).split('\n')[:-1]
    except:
        pass
    try:
        for teacher in teachers:
            teacher_uri = "_".join(teacher.split())
            g.add(((URIRef(VUC + course_id)), VU.taughtBy, URIRef(VU + teacher_uri)))
            g.add((URIRef(VU + teacher_uri)),
                  RDFS.label, Literal(teacher))
    except:
        pass
    try:
        course_description = soup.find(
            id="course-description").findAll("div", "paragraph")
        # deleting <br> and <h3> tags
        for section in course_description:
            for br in section.findAll("br"):
                br.extract()
            for h3 in section.findAll("h3"):
                h3.extract()
        g.add((URIRef(VUC + course_id), VU.courseObjective,
               Literal(" ".join(course_description[0].text.split()))))
        g.add((URIRef(VUC + course_id), VU.courseContent,
               Literal(" ".join(course_description[1].text.split()))))
        g.add((URIRef(VUC + course_id), VU.teachingMethods,
               Literal(" ".join(course_description[2].text.split()))))
        g.add((URIRef(VUC + course_id), TEACH.grading,
               Literal(" ".join(course_description[3].text.split()))))
    except:
        pass
    try:
        g.add((URIRef(VUC + course_id), VU.literature,
               Literal(" ".join(course_description[4].text.split()))))
        g.add((URIRef(VUC + course_id), VU.targetAudience,
               Literal(" ".join(course_description[5].text.split()))))
        g.add((URIRef(VUC + course_id), VU.recommendedBackground,
               Literal(" ".join(course_description[6].text.split()))))
    except:
        pass
# %%

# save the graph as ttl
with open('vu_studyguide.ttl', 'w') as f:
    g.serialize('vu_studyguide.ttl', format='turtle')


# saving the parsed graph in the root directory of the website
# this is done so that the serverless function does not need
# to parse the graph each time which is compute intensive
with open("../website/vu_studyguide_pickled.pk", 'wb') as f:
    pickle.dump(g, f)
