As this is implemented via gRPC you can find the communication in the trace by looking for gRPC headers. To find the data being sent look at the largest packet in this gRPC communication period. To find the source and destination see the source and destination of this packet. 


message is contained in packet 2184

1. Identify the Ip+Port sending the data 
    192.168.204.129:37352
2. Identify Ip+Port receiving the data
    192.168.204.130:12345
3. Identify the data being sent if possible
    45787472656d656c7920636f6e666964656e7469616c206d6573736167652c20646f206e6f74206c657420616e796f6e65207365652074686973
This is a hex encoded string that equals:
    "Extremely confidential message, do not let anyone see this"
4. If identifying the data is not possible, explain why
    Only applicable in the encrypted pair
5. How were you able to identify the packets associated with data exfiltration
Possible answers not limited to:
    gRPCHTTP protocol appears in the trace before the message
    Suspicious endpoint
    Suspicious target port

6. Given your method of identifying these packets, how could the attacker have hidden their communication better
    Use a less loud method than gRPC
    Fragment the data over multiple messages to make identification more difficult
    Use well know ports
