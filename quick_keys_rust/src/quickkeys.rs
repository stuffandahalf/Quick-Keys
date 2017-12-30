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
        
        return 0;
    }
    
    pub fn get_profile(&self) -> &Profile {
        return &self.profile;
    }
}

