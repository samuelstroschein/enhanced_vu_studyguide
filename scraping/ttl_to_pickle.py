from rdflib import Graph, RDF, Namespace, Literal, URIRef
import pickle

g = Graph()
g.parse("vu_studyguide.ttl", format="turtle")


# saving the parsed graph in the root directory of the website
# this is done so that the serverless function does not need
# to parse the graph each time which is compute intensive
with open("./vu_studyguide_pickled.pk", 'wb') as f:
    pickle.dump(g, f)