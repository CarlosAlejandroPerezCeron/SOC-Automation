from elasticsearch import Elasticsearch
import structlog
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "http://localhost:9200")

# Conectar con Elasticsearch
es = Elasticsearch(ELASTICSEARCH_HOST)

def log_security_event(event_type, details):
    log_entry = {
        "event_type": event_type,
        "details": details
    }
    es.index(index="soc-automation-logs", body=log_entry)
