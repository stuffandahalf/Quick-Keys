use profile::Profile;
use quickkeys::QuickKeys;
use PREF_FILE;

use std::string::String;
use std::path::Path;
use std::fs::File;
use std::io::prelude::*;

#[derive(Debug, Clone)]
pub struct Preferences {
    profiles: Vec<Profile>,
    devices: Vec<QuickKeys>,
}

impl Preferences {
    pub fn new() -> Preferences {
        let mut p = Preferences {
            profiles: Vec::new(),
            devices: Vec::new(),
        };
        p.profiles.push(Profile::new());
        return p;
    }
    
    pub fn load_prefs(&mut self) {
        if Path::new(PREF_FILE).exists() {
            self.profiles = Vec::new();
            self.devices = Vec::new();
            if let Ok(mut file) = File::open(PREF_FILE) {
                let mut pref = String::new();
                file.read_to_string(&mut pref);
                println!("{}", pref);
            }
            else {
                println!("Error: Failed to open preference file");
            }
        }
    }
    
    /*pub fn write_prefs(&self) {
        
    }*/
}
