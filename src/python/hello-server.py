import sys
import logging
 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
 
from documentstore.thrift import HelloService
from documentstore.handler import HelloHandler
 
PORT = 9090

 
# log to stdout
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(threadName)s - %(message)s')
 
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(1)
 
ch.setFormatter(formatter)
log.addHandler(ch)
 
logging.info('Hello server starting on port %d', PORT)


if __name__ == '__main__':
    
    handler = HelloHandler()
    processor = HelloService.Processor(handler)
    transport = TSocket.TServerSocket(port=PORT)
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    tfactory = TTransport.TBufferedTransportFactory()
    server =  TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    try:
        print(f'Starting sever on port: {PORT}')
        server.serve()
        print('done.')
    except (KeyboardInterrupt, SystemExit):
        logging.info('Caught signal, stopping threads')
        logging.info('Threads stopped, terminating')
