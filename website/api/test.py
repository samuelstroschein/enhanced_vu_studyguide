from rdflib import Graph, RDF, Namespace, Literal, URIRef
import pickle

# g = Graph()
# g.parse("vu_studyguide.ttl", format="turtle")
# # open a pickle file
filename = 'mypickle.pk'

with open(filename, 'rb') as fi:
    word_list = pickle.load(fi)
# qres = g.query("""
#                PREFIX vu: <https://www.vu.nl/en/properties/>
# PREFIX vuc: <https://studiegids.vu.nl/en/2020-2021/courses/>
# PREFIX teach: <http://linkedscience.org/teach/ns#>
# PREFIX dbo: <http://dbpedia.org/ontology/>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# select DISTINCT * where { 
# 	?course teach:ects ?credits ;
#          	vu:courseLevel ?level;
#           	teach:academicTerm ?period;
#            	teach:courseTitle ?title;
#             vu:taughtBy ?teacher;
#             dbo:language ?language;
#             teach:grading ?grading;
#             vu:courseContent ?content;
#             rdf:type teach:Course;
#             vu:courseObjective ?objective;
#             vu:offeredByFaculty ?faculty;
#             vu:literature ?literature;
#             vu:teachingMethods ?teachingMethod.
# } LIMIT 100
#                """)
# for row in qres:
#     print(row)
#     break
