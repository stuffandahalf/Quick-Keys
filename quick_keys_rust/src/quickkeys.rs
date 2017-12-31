use serialport;
use serialport::SerialPort;
use enigo::{Enigo, KeyboardControllable};
use std::string::String;
//use std::ptr;

use profile::Profile;

//#[derive(Debug, Clone, Copy]
pub struct QuickKeys<'a> {
    profile: Profile<'a>,
    //port: &'a /*(*/SerialPort/* + 'a)*/,
    port: &'a str,
}

impl<'a> QuickKeys<'a> {
    pub fn new() -> QuickKeys<'a> {
        return QuickKeys {
            profile: Profile::new(),
            //port: QuickKeys::open_port().unwrap(),
            port: "/dev/ttyUSB0",
        };
    }
    
    /*fn open_port() -> Option<&'a SerialPort> {
        //let mut p: &SerialPort;
        match serialport::open("/dev/ttyUSB0")
        {
            Ok(t) => return Some(t),
            Err(err) => /*println!("Error opening default serial port: {}", err); */return None,
        }
        //return p
        //if let Ok(p) = 
    }*/
    
    pub fn main_script(&self) -> i32 {
        let mut enigo = Enigo::new();
        let mut serial_buf: Vec<u8> = vec![0; 4];
        if let Ok(mut port) = serialport::open(self.get_port()) {
            loop {
                if let Ok(bytes) = port.read(serial_buf.as_mut_slice()) {
                    //println!("{}", bytes);
                    //println!("{:?}", serial_buf);
                    
                    let i: usize = serial_buf[0] as usize - 49;
                    let sym = self.get_profile().get_symbol(i);
                    //println!("{}", self.get_profile().get_symbol(i));
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

