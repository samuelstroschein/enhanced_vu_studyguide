from http.server import BaseHTTPRequestHandler
from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    res = request.args.get('query')
    return Response(res)


# g = Graph()

# g.parse("vu_studyguide.ttl", format="turtle")
# # print(g.serialize(format="turtle").decode("utf-8"))
# qres = g.query(
#     """PREFIX vu: <https://www.vu.nl/en/properties/>
# PREFIX vuc: <https://studiegids.vu.nl/en/2020-2021/courses/>
# PREFIX teach: <http://linkedscience.org/teach/ns#>
# PREFIX dbo: <http://dbpedia.org/ontology/>
# PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# select DISTINCT * where {
#     ?course teach:ects ?credits ;
#             vu:courseLevel ?level;
#             teach:academicTerm ?period;
#             teach:courseTitle ?title;
#             vu:taughtBy ?teacher;
#             dbo:language ?language;
#             teach:grading ?grading;
#             vu:courseContent ?content;
#             rdf:type teach:Course;
#             vu:courseObjective ?objective;
#             vu:offeredByFaculty ?faculty;
#             vu:literature ?literature;
#             vu:teachingMethods ?teachingMethod.
# } LIMIT 1""")
