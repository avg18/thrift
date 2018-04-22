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
from documentstore.thrift import HelloService
from documentstore.exceptions.ttypes import EUnknown

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
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloService.Client(protocol)

    # Connect!
    transport.open()

    logging.info( f'connected ... {client.hello(DOMAIN)}')

    
    # Document and description Tests

    _documents = eval(client.fetch_documents())
    logging.info(f'DOKUMENT: {_documents}')
   
    _descriptions = eval(client.fetch_descriptions())
    logging.info(f'DOKUMENT: {_descriptions}')


    # Document and description Tests with exception
    try:
        _document = eval(client.fetch_document(_descriptions[1]['id']))
    except EUnknown as e:
        logging.info(f'Unknown Exception: {e}')

    try:
        _document = eval(client.fetch_document('d4lf2e5e-8923-4f11-861c-2d6d09ce6b0e'))
    except EUnknown as e:
        logging.info(f'Unknown Exception: {e}')

    try:
        _change = eval(client.change_description(_descriptions[1]['id'], 'anders'))
    except EUnknown as e:
        logging.info(f'Unknown Exception: {e}')

    
    # Close!
    transport.close()


if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
