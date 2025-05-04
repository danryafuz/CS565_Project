To run encrypt_AES or encrypt_AES_GCM:
1. Have VM Linux running with the source code, have local machine with the source code
2. change the HOST variable in the sender.py and receiver.py to the IP address of the VM
3. Make sure you have python has access to the socket and pycryptodome libraries
4. Run 'python receiver.py' in terminal in your VM
5. Run 'python sender.py' in terminal on your local machine
6. Data should be sending and receiving! Have wireshark listen over loopback to see traces
