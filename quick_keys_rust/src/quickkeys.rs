use serialport;
use enigo::{Enigo, KeyboardControllable};
use std::string::String;

use profile::Profile;

#[derive(Debug, Clone, Copy)]
pub struct QuickKeys<'a> {
    profile: Profile<'a>,
    port: &'a str,
    exit: bool,
}

impl<'a> QuickKeys<'a> {
    pub fn new() -> QuickKeys<'a> {
        return QuickKeys {
            profile: Profile::new(),
            port: "/dev/ttyUSB0",
            exit: false,
        };
    }
    
    pub fn main_script(&self) -> i32 {
        let mut exit = false;
        let mut enigo = Enigo::new();
        let mut serial_buf: Vec<u8> = vec![0; 4];
        //let Ok(mut ports) = serialport::available_ports()/*.iter().map(|d| d.port).collect()*/;
        //let port_names: Vec<String> = ports.iter().map(|d| d.port_name).collect();
        //println!("{:?}", ports);
        if let Ok(mut port) = serialport::open(self.get_port()) {
            //while !self.exit {
            while !exit {
            //while ports.contains(self.port) {
                if let Ok(bytes) = port.read(serial_buf.as_mut_slice()) {
                    let i: usize = serial_buf[0] as usize - 49;
                    let sym = self.get_profile().get_symbol(i);
                    enigo.key_sequence(sym);
                }
                
                if let Ok(mut ports) = serialport::available_ports() {
                    let port_names: Vec<&str> = ports.iter().map(|p| &*p.port_name).collect();
                    println!("{:?}", port_names);
                    /*if port_names.contains(self.port) {
                        exit = true;
                        //return 1;
                    }*/
                } else {
                    exit = true;
                    //return 1;
                }
            }
            println!("Device disconnected");
        }
        else {
            println!("Error: Port '{}' not available", self.get_port());
            return 1;
        }
        
        return 0;
    }
    
    pub fn get_port(&self) -> &str {
        return &self.port;
    }
    
    pub fn get_profile(&self) -> &Profile {
        return &self.profile;
    }
}

