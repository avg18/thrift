#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

import json
import uuid
from hello.thrift import HelloService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

import logging

log = logging.getLogger()
log.setLevel(logging.DEBUG)

DOMAIN = "localhost"

def main():
    # Make socket
    transport = TSocket.TSocket(DOMAIN, 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = HelloService.Client(protocol)

    # Connect!
    transport.open()

    logging.info( f'connected ... {client.hello(DOMAIN)}')

    _documents = eval(client.fetch_documents())
    logging.info(_documents)
   
    _descriptions = eval(client.fetch_descriptions())
    logging.info(_descriptions)
    logging.info(type(_descriptions))

    _document = eval(client.fetch_document(_descriptions[1]['id']))
    logging.info(_document)
    logging.info(f'Dokument {type(_document)}')

    # Close!
    transport.close()


if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
