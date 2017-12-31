use serialport;
use enigo::{Enigo, KeyboardControllable};

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
        let mut enigo = Enigo::new();
        let mut serial_buf: Vec<u8> = vec![0; 4];
        if let Ok(mut port) = serialport::open(self.get_port()) {
            while !self.exit {
                if let Ok(bytes) = port.read(serial_buf.as_mut_slice()) {
                    let i: usize = serial_buf[0] as usize - 49;
                    let sym = self.get_profile().get_symbol(i);
                    enigo.key_sequence(sym);
                }
            }
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

