use quickkeys::QuickKeys;
use std::thread::JoinHandle;
use std::thread;

/*use serialport;
use std::io::{self, Write};
use enigo::{Enigo, KeyboardControllable};
use profile::Profile;

pub fn serial_test() {
    let mut port_name = "".to_string();
    if let Ok(mut ports) = serialport::available_ports() {
        println!("{:?}", ports[0]);
        port_name = ports[0].clone().port_name;
    } else {
        println!("Failed to detect any ports");
    }
    
    //let port_name = "/dev/ttyUSB0";
    if let Ok(mut port) = serialport::open(&port_name) {
        let mut serial_buf: Vec<u8> = vec![0; 4];
        println!("Receiving data on {} at 9600 baud:", &port_name);
        loop {
            if let Ok(t) = port.read(serial_buf.as_mut_slice()) {
                //io::stdout().write_all(&serial_buf[..t]).unwrap();
                println!("{:?}", serial_buf);
            }
        }
    } else {
        println!("Error: Port '{}' not available", &port_name);
    }
}

pub fn enigo_test() {
    let mut enigo = Enigo::new();
    enigo.key_sequence("πΣ");
}

pub fn emit_string(enigo: &mut Enigo, string: &str) {
    enigo.key_sequence(string);
}*/

pub fn start_qk_thread(qkdev: &QuickKeys) {
    let local_dev = qkdev.clone();
    let handle = thread::spawn(|| {
        qkdev.start();
    });
    handle.join();
    //return &local_dev;
}
