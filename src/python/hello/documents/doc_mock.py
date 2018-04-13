#/usr/bin/env --utf-8--

from .document import Document, add_document

from datetime import datetime 

BESCHREIBUNG = ("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed" 
     "diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam") 


def dummy():
    add_document('erstes valid', BESCHREIBUNG, 0)
    add_document('zweites valid', BESCHREIBUNG)

def doc_dummy():
    return Document('erstes valid', BESCHREIBUNG, 0)


    
if __name__ == '__main__':
    print(doc_dummy())



