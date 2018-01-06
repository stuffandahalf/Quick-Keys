use serialport;
use enigo::{Enigo, KeyboardControllable};
use std::path::Path;
//use std::string::String;
use std::thread;

use profile::Profile;

#[derive(Debug, Clone, Copy)]
pub struct QuickKeys<'a> {
    profile: Profile<'a>,
    port: &'a str,
}

impl<'a> QuickKeys<'a> {
    /*#[cfg(target_os = "linux")]
    pub fn new() -> QuickKeys<'a> {
        return QuickKeys {
            profile: Profile::new(),
            port: "/dev/ttyUSB0",
        };
    }
    
    #[cfg(target_os = "windows")]
    pub fn new() -> QuickKeys<'a> {
        return QuickKeys {
            profile: Profile::new(),
            port: "COM4",
        };
    }*/
    
    pub fn new_on(port_name: &'a str) -> QuickKeys<'a> {
        return QuickKeys {
            profile: Profile::new(),
            port: port_name,
        }
    }
    
    pub fn main_script(&self) -> i32 {
        let mut enigo = Enigo::new();
        let mut serial_buf: Vec<u8> = vec![0; 4];
        if let Ok(mut port) = serialport::open(self.get_port()) {
            while self.port_exists() {
                if let Ok(_bytes) = port.read(serial_buf.as_mut_slice()) {
                    let i: usize = serial_buf[0] as usize - 49;
                    let sym = self.get_profile().get_symbol(i);
                    enigo.key_sequence(sym);
                }
                /*match port.read(serial_buf.as_mut_slice()) {
                    Ok(bytes) => println!("{}", bytes),
                    Err(err) => println!("{:?}", err),
                }*/
            }
            println!("Device disconnected");
            
        }
        else {
            println!("Error: Port '{}' not available", self.get_port());
            return 1;
        }
        
        return 0;
    }
    
    /*fn port_exists(&self) -> bool {
        if let Ok(ports) = serialport::available_ports() {
            let port_names: Vec<&str> = ports.iter().map(|s| &*s.port_name).collect();
            return port_names.contains(&self.get_port());
        }
        println!("QuickKeys on port {} disconnected", self.get_port());
        return false;
    }*/
    
    #[cfg(target_os = "linux")]
    fn port_exists(&self) -> bool {
        return Path::new(self.get_port()).exists();
    }
    
    #[cfg(target_os = "macos")]
    fn port_exists(&self) -> bool {
        return true;
    }
    
    #[cfg(target_os = "windows")]
    fn port_exists(&self) -> bool {
        return true;
    }
    
    pub fn get_port(&self) -> &str {
        return &self.port;
    }
    
    pub fn get_profile(&self) -> &Profile {
        return &self.profile;
    }
}

