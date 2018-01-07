use serialport;
use enigo::{Enigo, KeyboardControllable};
use std::path::Path;
use std::string::String;
use std::thread;

use profile::Profile;

#[derive(Debug, Clone)]
pub struct QuickKeys {
    profile: Profile,
    port: String,
    exit: bool,
}

impl QuickKeys {
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
    
    pub fn new_on(port_name: &str) -> QuickKeys {
        return QuickKeys {
            profile: Profile::new(),
            port: String::from(port_name),
            exit: false,
        };
    }
    
    pub fn start(&/*mut */self) {
        //self.exit = false;
        let mut enigo = Enigo::new();
        let mut serial_buf: Vec<u8> = vec![0; 4];
        if let Ok(mut port) = serialport::open(self.port()) {
            println!("Connected to QuickKeys on port {}", self.port());
            while self.port_exists() && !self.exit {
                if let Ok(_bytes) = port.read(serial_buf.as_mut_slice()) {
                    let i: usize = serial_buf[0] as usize - 49;
                    let sym = self.profile().get_symbol(i);
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
            println!("Error: Port '{}' not available", self.port());
        }
    }
    
    pub fn stop(&mut self) {
        self.exit = true;
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
        return Path::new(self.port()).exists();
    }
    
    #[cfg(target_os = "macos")]
    fn port_exists(&self) -> bool {
        return true;
    }
    
    #[cfg(target_os = "windows")]
    fn port_exists(&self) -> bool {
        return true;
    }
    
    pub fn port(&self) -> &str {
        return &*self.port;
    }
    
    pub fn profile(&self) -> &Profile {
        return &self.profile;
    }
    
    pub fn set_symbol(&mut self, index: usize, symbol: &str) {
        self.profile.set_symbol(index, symbol);
    }
}

