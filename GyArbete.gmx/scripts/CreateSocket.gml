#define CreateSocket
///CreateSocket()
global.client = network_create_socket(network_socket_tcp);
//if !timeline0_running;
 //   {
        ConnectClientSocket();
//    }

#define ConnectSocket
///ConnectSocket()
connected = network_connect_raw(global.client, "127.0.0.1", 6510);
return connected;