extern crate enigo;
extern crate serialport;

#[macro_use]
extern crate serde_derive;
extern crate serde;
extern crate serde_json;

mod profile;
mod qkdev;
mod quickkeys;

use std::string::String;
use profile::Profile;
use quickkeys::QuickKeys;
//use qkdev::QKDev;

const KEYS: usize = 6;

#[derive(Debug, Serialize, Deserialize)]
pub struct QKCore {
    pref_file: String,
    profiles: Vec<Profile>,
    devices: Vec<QuickKeys>,
}

impl QKCore {
    pub fn new(pref_file: &str, ) -> QKCore {
        QKCore {
            pref_file: String::from(pref_file),
            profiles: Vec::new(),
            devices: Vec::new(),
        }
    }
    
    pub fn new_device(&mut self, port: &str) -> Result<QuickKeys, String> {
        //self.devices.push(QuickKeys::new_on(port));
        match QuickKeys::new(port) {
            Ok(dev) => self.devices.push(dev),
            Err(err) => preintln!("{}", err),
        }
    }
}

/*#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}*/
