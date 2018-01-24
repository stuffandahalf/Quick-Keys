use profile::Profile;
use quickkeys::QuickKeys;
use qkdev::QKDev;
use KEYS;
use PREF_FILE;

use serde_json;
use std::string::String;
use std::path::Path;
use std::fs::File;
use std::io::prelude::*;

static EOF_ERR: &str = "Error: Unexpected EOF";
static FILE_OPEN_ERR: &str = "Error: Failed to open preference file";

#[derive(Debug, Clone, Serialize, Deserialize)]
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
        
        if Path::new(PREF_FILE).exists() {
            p.load_prefs();
        }
        else {
            p.profiles.push(Profile::new());
            p.write_prefs();
        }
        return p;
    }
    
    pub fn load_prefs(&mut self) {
        match File::open(PREF_FILE) {
            Ok(mut file) => {
                let mut json_str = String::new();
                let _ = file.read_to_string(&mut json_str);
                let data: Preferences = serde_json::from_str(&*json_str).unwrap();
                self.profiles = data.profiles().clone();
                self.devices = data.devices().clone();
                println!("Preferences loaded from disk");
            },
            Err(err) => println!("{}", err),
        }
    }
    
    pub fn write_prefs(&self) {
        match File::create(PREF_FILE) {
            Ok(mut file) => {
                let json_str = serde_json::to_string(self).unwrap();
                let _ = file.write_all(&*json_str.as_bytes());
                println!("Preferences saved");
            },
            Err(err) => println!("{:?}", err),
        }
    }
    
    pub fn find_profile(&self, name: String) -> Option<Profile> {
        for i in 0..self.profiles.len() {
            if self.profiles[i].name() == name {
                return Some(self.profiles[i].clone());
            }
        }
        return None;
    }
    
    pub fn profiles(&self) -> &Vec<Profile> {
        return &self.profiles;
    }
    
    pub fn devices(&self) -> &Vec<QuickKeys> {
        return &self.devices;
    }
    
    pub fn reset_devices(&mut self, devices: &mut Vec<QKDev>) {
        self.devices = devices.iter().map(|d| d.device().clone()).collect();
    }
}
