from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req_query = request.args.get('query')
    g = Graph()
    g.parse("vu_studyguide.ttl", format="turtle")
    qres = g.query(req_query)
    serialized = qres.serialize(format='json-ld', indent=4)
    print(serialized)
    return Response(qres.serialize(format='json-ld', indent=4))
