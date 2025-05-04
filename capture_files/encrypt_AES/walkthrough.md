As you know the data is being sent within the network, check the endpoints listed by wireshark and apply ip filters from this window, there should be very few endpoints within the network listed. Double click on a packet to view properties. To find the data being sent right click on a packet, and click Analyze->Follow->TCP Stream. Change the view format to HEX.

This information is true for any packet received from the AES_CFB encrypted sender

1. Identify the Ip+Port sending the data 
    192.168.12.18:52269

2. Identify Ip+Port receiving the data
    192.168.12.51:12345

3. Identify the data being sent if possible
    not possible
4. If identifying the data is not possible, explain why
    Data is encrypted
5. You are given that the data was encrypted using some AES method and that the first two packets data before encoding sent by the sender are the same
a. can you indentify which method was used? 
Looking at the packet data it is very short, which rules out the usage of tags, and so it is most likely AES-CFB or AES-ECB (AES-CFB was used)
b. Is the encryption random between packets? If not, can you identify the constants and what they are?
the first two packets sent by the sender have the same encoding and so it is not random, since we know the encoder uses AES-CFB or AES-ECB we can derive the IV to be b'\x9c\x3a\x12\x7f\x44\xa0\xef\x01\x88\x5d\xc3\x7a\x6b\x9e\x4f\x25'
c. If you aren given the plain text data, would you be able to decipher more information about the encryption, such as the keys?
No, since AES uses a feeback loop with a key to encrypt the data, knowing the plain text data and the encrypted data is not enough to generate the key.
6. How were you able to identify the packets associated with data exfiltration

Possible answers not limited to:
    Suspicious endpoints
    Suspicious destination port

7. Given your method of identifying these packets, how could the attacker have hidden their communication better
    Use well known ports
    Use cloud hosting for the C2/receiver