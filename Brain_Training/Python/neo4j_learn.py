from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable, Neo4jError
import os
import sys
from datetime import timezone,timedelta
from neo4j.time import D

NEO4J_URI = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "C1sc0@123")


def test_db_connection():

    try:
        print("Verifying connectivity...")
        driver.verify_connectivity() # if any issue it will raise exception
        print("✓ Connected to Neo4j successfully.\n")

        # Execute a simple query to confirm DB is working

        with driver.session(database="mydb1") as session: # to change the user database name use this space
            result = session.run("MATCH (n) RETURN count(n) AS node_count")
            record = result.single()
            if record:
                print(f"✓ Total nodes in database: {record['node_count']}")
                return 0
            else:
                print("⚠ Query executed but no result returned.")

    # except AuthError as e:
    #     print(f"✗ Authentication failed: {e}")
    #     print(f"  Check NEO4J_USER and NEO4J_PASSWORD (currently: {NEO4J_USER})")
    #     sys.exit(1)
    #
    # except ServiceUnavailable as e:
    #     print(f"✗ Neo4j service unavailable: {e}")
    #     print(f"  Is Neo4j running on {NEO4J_URI}?")
    #     sys.exit(1)

    # except Neo4jError as e:
    #     print(f"✗ Database error: {e}")
    #     sys.exit(1)
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")
        sys.exit(1)


def cypher_query():
    query = """
    MATCH (m:Movie)<-[:ACTED_IN]-(p:Person) WHERE m.title=$title with m.title as MovieName, p.name as Actor 
    RETURN MovieName,Actor
    """
    query1 = """ MATCH path = (person:Person)-[actedIn:ACTED_IN]->(movie:Movie {title: $title})
    RETURN path, person, actedIn, movie"""
    movie = "Toy Story"
    with driver.session(database="mydb1") as session:
        result = session.run(query1,title=movie)
        records = list(result)

    # for record in records:
    #     print(f"{record['MovieName']} -> {record['Actor']}")

    for record in records:
        node = record["movie"]
        print(node.element_id)      # (1)
        print(node.labels)          # (2)
        print(node.items())         # (3)
        print(node["name"])
        print(node.get("name", "N/A"))

        acted_in = record["actedIn"]
        print(acted_in.id)         # (1)
        print(acted_in.type)       # (2)
        print(acted_in.items())    # (3)
        print(acted_in["roles"])
        print(acted_in.get("roles", "(Unknown)"))
        print(acted_in.start_node) # (5)
        print(acted_in.end_node)   # (6)
        path = record["path"]
        print(path.start_node)  # (1)
        print(path.end_node)    # (2)
        print(len(path))  # (1)
        print(path.relationships)  # (1)

def temporal_test():
    query = """
    CREATE (e:Event {
      startsAt: $datetime,              // (1)
      createdAt: datetime($dtstring),   // (2)
      updatedAt: datetime()             // (3)
    })
    """
    with driver.session(database="mydb1") as session:
        result = session.run(query)
        records = list(result)

if __name__ == "__main__":
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        # test_db_connection()
        cypher_query()
    except Exception as e:
        print(f"✗ An unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        driver.close()
        print("\nDriver closed.")
    # cypher_query = input("Write you cypher query: ")
    # print(f"Executing query: {cypher_query}")