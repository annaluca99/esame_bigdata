from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "tourism123")

driver = GraphDatabase.driver(URI, auth=AUTH)

session = driver.session(database="neo4j")

# Scrittura: crea o aggiorna un nodo Movie
result = session.run(
    """
    QUA VA LA PRIMA QUERY
)

print("Written movie:")
for record in result:
    print(record["Luogo"], record["Citta"], record["Tipo"], record["Itinerario"])


session.close()
driver.close()