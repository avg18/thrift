# AVG Thrift

RPC API for DocumentStore.

## Prerequisites

Install Conda: https://conda.io/miniconda.html

## Installing

**rest-environment**

````
 $ conda env create -f environment-rest.yml
````

## Run
- run src/pyhton/server.py in environment. 
- run src/pyhton/hello-client.py in environment. 

# API


````yml
POST /change_description
HTTP/1.1
HOST: http://localhost:9090/v1.0
Content-Type: application/json

{
  "description": string,
  "id": string
}

POST /fetch_documents
HTTP/1.1
HOST: http://localhost:9090/v1.0
Content-Type: application/json

[{

  "description": string,
  "id": string
  "name": string

}]


POST /fetch_descritptions
HTTP/1.1
HOST: http://localhost:9090/v1.0
Content-Type: application/json

[
    {
        "description": string,
        "id": string
    }
    ...
]
````