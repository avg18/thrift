namespace py hello.thrift
 
include "exceptions.thrift"
 
service HelloService {
    
    void ping(),

    string hello(
        1: required string name
    ) throws (
        1: exceptions.EUnknown ie
    )
}