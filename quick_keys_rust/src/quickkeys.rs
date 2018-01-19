use serialport;
use enigo::{Enigo, KeyboardControllable};
use std::path::Path;
use std::string::String;
use std::thread;
use std::sync::mpsc::Receiver;

use profile::Profile;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct QuickKeys {
    //profile: Profile,
    port: String,
}

impl QuickKeys {
    pub fn new() -> QuickKeys {
        return QuickKeys {
            //profile: Profile::new(),
            port: String::new(),
        }
    }
    
    pub fn new_on(port_name: &str) -> QuickKeys {
        return QuickKeys {
            //profile: Profile::new(),
            port: String::from(port_name),
        };
    }
    
    pub fn start(&self, rx: Receiver<bool>, profile: Profile) {
        let mut exit = false;
        let mut enigo = Enigo::new();
        let mut serial_buf: Vec<u8> = vec![0; 4];
        if let Ok(mut port) = serialport::open(self.port()) {
            println!("Connected to QuickKeys on port {}", self.port());
            while self.port_exists() && !exit {
                if let Ok(_bytes) = port.read(serial_buf.as_mut_slice()) {
                    let i: usize = serial_buf[0] as usize - 49;
                    //let sym = self.profile().get_symbol(i);
                    let sym = profile.get_symbol(i);
                    enigo.key_sequence(sym);
                }
                if let Ok(val) = rx.try_recv() {
                    exit = val;
                }
            }
            //println!("Device disconnected");
            println!("Thread terminated");
        }
        else {
            println!("Error: Port '{}' not available", self.port());
        }
    }
    
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
    
    /*pub fn profile(&self) -> &Profile {
        return &self.profile;
    }
    
    pub fn set_profile(&mut self, new_prof: Profile) {
        self.profile = new_prof;
    }
    
    pub fn set_symbol(&mut self, index: usize, symbol: &str) {
        self.profile.set_symbol(index, symbol);
    }*/
}

