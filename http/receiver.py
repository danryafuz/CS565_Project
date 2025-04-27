import grpc
import message_pb2
import message_pb2_grpc
from concurrent import futures
import threading
import sys

HOST = '127.0.0.1'  
PORT = 12345  


class MessageReceiver(message_pb2_grpc.MessageServicer):
    def Send(self, request, context):
        message = request.msg
        print(message)
        return message_pb2.reply(msg = "received")



def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    message_pb2_grpc.add_MessageServicer_to_server(MessageReceiver(), server)
    server.add_insecure_port(f'[::]:{PORT}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()