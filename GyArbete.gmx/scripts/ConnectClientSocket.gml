///ConnectClientSocket()
connected = network_connect_raw(global.client, "127.0.0.1", 6510);
//return connected;
if (connected != -1) {
    timeline_index = timeline0;
    timeline_loop = true;
    timeline_running = true;
}
