/*os_lock_orientation(true);
while (os_is_network_connected()){
    
}*/
//draw_text(50, 50, 'test');
connected = (-1);
global.client = network_create_socket(network_socket_tcp);
while (connected == -1){
connected = network_connect_raw(global.client, "127.0.0.1", 6510);
//draw_text(0, 0, connected);
}

/*while (true) {
    points[0,0] = 1;
    points[0,1] = 1;
    for (i = 0; i < 5; i++) {
        
    
    }
}*/

myBuffer = buffer_create(16, buffer_wrap, 8);
while (true) {
    steeringWheel = 2*device_get_tilt_y();
    steeringWheel = -15;//round(steeringWheel);
    thrust = 2*device_get_tilt_z();
    thrust = 255;//round(thrust);
    int64(steeringWheel);
    int64(thrust);
    
    buffer_write(myBuffer, buffer_u64, int64(steeringWheel));
    buffer_write(myBuffer, buffer_u64, int64(thrust));
    
    network_send_raw(global.client, myBuffer, buffer_get_size(myBuffer));
}
