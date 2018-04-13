import logging

from .exceptions.ttypes import EUnknown

from .documents.document import Document,get_documents, get_descriptions, get_document
from .documents.doc_mock import dummy

class HelloHandler:
    '''
    Implements thrift server logic.
    '''

    def __init__(self):
        logging.info('Initializing handler')
        dummy()
        

    def __del__(self):
        logging.info('Disposing handler')


    # -------------------------------------------------------------------------
    # -------------- Thrift - HelloService Implementation -------------
    # -------------------------------------------------------------------------

    def ping(self):
        logging.info('Run hello request')

    def hello(self, name):
        logging.info('Run hello request')
        return f'{name}-Handler'
    
    def fetch_documents(self):
        return get_documents()

    def fetch_document(self, id):
        return get_document(id)
    
    def fetch_descriptions(self):
        return get_descriptions()
 
if __name__ == '__main__':
    
    import sys
    sys.path.append('C:/01-Workspace/04-AVG/03_2-Thrift/src')

    _handler = HelloHandler()
    dummy()