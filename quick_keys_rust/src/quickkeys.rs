use serialport;
use serialport::SerialPort;
use std::string::String;
use std::ptr;

use profile::Profile;

//#[derive(Debug, Clone, Copy]
pub struct QuickKeys<'a> {
    profile: Profile,
    port: &'a /*(*/SerialPort/* + 'a)*/,
}

impl<'a> QuickKeys<'a> {
    pub fn new() -> QuickKeys<'a> {
        return QuickKeys {
            profile: Profile::new(),
            port: QuickKeys::open_port().unwrap(),
        };
    }
    
    fn open_port() -> Option<&'a SerialPort> {
        //let mut p: &SerialPort;
        match serialport::open("/dev/ttyUSB0")
        {
            Ok(t) => return Some(t),
            Err(err) => /*println!("Error opening default serial port: {}", err); */return None,
        }
        //return p
        //if let Ok(p) = 
    }
    
    pub fn get_profile(&self) -> &Profile {
        return &self.profile;
    }
}
