namespace py hello.thrift
 
include "exceptions.thrift"
 
service HelloService {
    
    void ping(),

    string hello(
        1: required string name
    ) throws (
        1: exceptions.EUnknown ie
    )
    string fetch_documents()
    string fetch_descriptions()
    string fetch_document(
        
        1: required string id
    )
}