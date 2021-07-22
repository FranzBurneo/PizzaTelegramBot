  
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper('https://dbpedia.org/sparql')

def obtener_ingredientes(ingredient):
    sparql.setQuery(f'''
        SELECT ?res ?image
        WHERE {{ 
            dbr:{ingredient} dbo:abstract ?res .
            dbr:{ingredient} foaf:depiction ?image.
            FILTER (lang(?res) = "es") 
        }}
    ''')
    sparql.setReturnFormat(JSON)
    qres = sparql.query().convert()
    if len(qres['results']['bindings']) == 0:
        return "Información no encontrada"
    else:
        result = qres['results']['bindings'][0]
        ingredient = result['res']['value']
        image = result['res']['value']
        return result