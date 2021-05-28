try:
    import pandas as pd
    import numpy as np
    from elasticsearch import Elasticsearch
    from elasticsearch import helpers
    es = Elasticsearch(http_compress=True)
except Exception as e:
    print(e)

