import sys
from http.server import BaseHTTPRequestHandler
from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request
from rdflib.plugins.sparql.results.jsonresults import JSONResultSerializer


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req_query = request.args.get('query')
    g = Graph()
    g.parse("vu_studyguide.ttl", format="turtle")
    qres = g.query(req_query)
    json = JSONResultSerializer(qres).serialize(sys.stdout)
    print(json)
    return Response(json)
