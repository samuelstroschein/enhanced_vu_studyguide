from rdflib import Graph, RDF, Namespace, Literal, URIRef
from flask import Flask, Response, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# opening the graph without parsing it (otherwise function runs too long)
with open('vu_studyguide_pickled.pk', 'rb') as fi:
    g = pickle.load(fi)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    req_query = request.args.get('query')
    qres = g.query(req_query)
    return Response(qres.serialize(format="json"))
