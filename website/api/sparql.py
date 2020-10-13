from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request
import pickle


app = Flask(__name__)

# opening the graph without parsing it (otherwise function runs too long)
filename = 'vu_studyguide_pickled'
with open(filename, 'rb') as fi:
    g = pickle.load(fi)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req_query = request.args.get('query')
    print(req_query)
    qres = g.query("""
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
               """)
    result = None
    for row in qres:
        result = row
        break
    return Response(result)
    # qres = g.query(req_query)
    # serialized = qres.serialize(format='json-ld', indent=4)
    # print(serialized)
    # return Response(qres.serialize(format='json-ld', indent=4))
