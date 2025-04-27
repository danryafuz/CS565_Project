import grpc
import message_pb2
import message_pb2_grpc

HOST = '127.0.0.1'  
PORT = 12345  

with grpc.insecure_channel(f'{HOST}:{PORT}') as channel:
                    stub = message_pb2_grpc.MessageStub(channel)
                    request = message_pb2.request(msg = "test") # Replace with message to send
                    response = stub.Send(request)
                    print(response.msg)