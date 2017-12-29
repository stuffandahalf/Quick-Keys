extern crate serialport;

mod quickkeys;
mod profile;

use std::io::{self, Write};

fn unbox<T>(value: Box<T>) -> T {
    *value
}

fn main() {
    //println!("Hello, world!");
    let mut port_name = "".to_string();
    if let Ok(mut ports) = serialport::available_ports() {
        println!("{:?}", ports[0]);
        let ref port = &ports[0];
        port_name = port.port_name;
    } else {
        println!("Failed to detect any ports");
    }
    
    //let port_name = "/dev/ttyUSB0";
    if let Ok(mut port) = serialport::open(&port_name) {
        let mut serial_buf: Vec<u8> = vec![0; 1000];
        println!("Receiving data on {} at 9600 baud:", &port_name);
        loop {
            if let Ok(t) = port.read(serial_buf.as_mut_slice()) {
                io::stdout().write_all(&serial_buf[..t]).unwrap();
            }
        }
    } else {
        println!("Error: Port '{}' not available", &port_name);
    }
}
