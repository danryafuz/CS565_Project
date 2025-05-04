As you know the data is being sent within the network, check the endpoints listed by wireshark and apply ip filters from this window, there should be very few endpoints within the network listed. To find the data being sent look at the largest packet sent to this endpoint. To find the source and destination see the source and destination of this packet. 




The packet containing the message is #2622 in the trace

1. Identify the Ip+Port sending the data 
    192.168.204.129:44230

2. Identify Ip+Port receiving the data
    192.168.204.130:12345

3. Identify the data being sent if possible
    546869732069732061207665727920736563726574206d6573736167652073656e742076696120616e20756e656e6372797074656420736f636b6574
This is a hex encoded string that equals:
    "This is a very secret message sent via an unencrypted socket"
4. If identifying the data is not possible, explain why
    Only applicable for the encyrpted pair
5. How were you able to identify the packets associated with data exfiltration

Possible answers not limited to:
    Suspicious endpoints
    Suspicious destination port

6. Given your method of identifying these packets, how could the attacker have hidden their communication better
    Use well known ports
    Use cloud hosting for the C2/receiver

