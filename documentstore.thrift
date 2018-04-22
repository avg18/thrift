namespace py documentstore.thrift
 
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
    ) throws (
        1: exceptions.EUnknown ie
    )
    string change_description(        
        1: required string id
        2: required string description
    ) throws (
        1: exceptions.EUnknown ie
    )
}