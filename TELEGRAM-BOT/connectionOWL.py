from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper(
    'http://localhost:3030/ds/sparql')


def get_response_pizzas():
    sparql.setQuery('''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX P:<http://www.semanticweb.org/msigf65thin/ontologies/2021/5/PizzaTutorial#>
        SELECT DISTINCT ?name 
        WHERE { 
            ?s rdfs:subClassOf P:NamedPizza .
            ?s rdfs:label ?name
            FILTER (lang(?name) = 'es')
        }
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres

def get_response_ingredients(pizza):
    sparql.setQuery(f'''
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX P:<http://www.semanticweb.org/msigf65thin/ontologies/2021/5/PizzaTutorial#>
	    SELECT ?ingredients
	    WHERE {{ P:{pizza} rdfs:subClassOf ?o .
	    ?o owl:someValuesFrom ?h .
  	    ?h rdfs:label ?ingredients 
        FILTER (lang(?ingredients) = 'es')
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    return qres


if __name__ == '__main__':
    get_response_pizzas()
