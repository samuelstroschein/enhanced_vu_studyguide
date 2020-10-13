from http.server import BaseHTTPRequestHandler
from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req_query = request.args.get('query')
    g = Graph()

    g.parse("vu_studyguide.ttl", format="turtle")
    # print(g.serialize(format="turtle").decode("utf-8"))
    qres = g.query(req_query)
    return Response(qres)

