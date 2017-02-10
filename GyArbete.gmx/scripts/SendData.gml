///SendData()
myBuffer = buffer_create(16, buffer_wrap, 8); //16 bytes, 8 bit alignment for smother use of int64

steeringWheel = 300*device_get_tilt_y();
steeringWheel = round(steeringWheel);
thrust = 300*device_get_tilt_z();
thrust = round(thrust);
int64(steeringWheel);
int64(thrust);
    
buffer_write(myBuffer, buffer_u64, int64(steeringWheel));
buffer_write(myBuffer, buffer_u64, int64(thrust));
    
network_send_raw(global.client, myBuffer, buffer_get_size(myBuffer));
