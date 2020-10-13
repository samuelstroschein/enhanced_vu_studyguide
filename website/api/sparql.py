from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request
import pickle


app = Flask(__name__)

# opening the graph without parsing it (otherwise function runs too long)
with open('vu_studyguide_pickled.pk', 'rb') as fi:
    g = pickle.load(fi)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req_query = request.args.get('query')
    print(req_query)
    qres = g.query(qres)
    result = None
    for row in qres:
        result = row
        break
    return Response(result)
    # qres = g.query(req_query)
    # serialized = qres.serialize(format='json-ld', indent=4)
    # print(serialized)
    # return Response(qres.serialize(format='json-ld', indent=4))
