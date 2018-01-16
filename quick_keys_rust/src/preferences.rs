use profile::Profile;
use quickkeys::QuickKeys;
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
        p.profiles.push(Profile::new());
        return p;
    }
    
    /*pub fn load_prefs(&mut self) {
        if Path::new(PREF_FILE).exists() {
            self.profiles = Vec::new();
            self.devices = Vec::new();
            let mut profiles: usize = 0;
            let mut devices: usize = 0;
            
            if let Ok(mut file) = File::open(PREF_FILE) {
                let mut pref = String::new();
                file.read_to_string(&mut pref);
                //println!("{}", pref);
                let mut iter = pref.split_whitespace();
                match iter.next() {
                    Some(val) => profiles = val.parse().unwrap(),
                    None => println!("{}", EOF_ERR),
                }
                match iter.next() {
                    Some(val) => devices = val.parse().unwrap(),
                    None => println!("{}", EOF_ERR),
                }
                iter.next();
                for _ in 0..profiles {
                    let mut new_prof = Profile::new();
                    match iter.next() {
                        Some(val) => new_prof.set_name(String::from(val)),
                        None => println!("{}", EOF_ERR),
                    }
                    for i in 0..KEYS {
                        match iter.next() {
                            Some(val) => new_prof.set_symbol(i, val),
                            None => println!("{}", EOF_ERR),
                        }
                    }
                    //println!("{:?}", new_prof);
                    self.profiles.push(new_prof);
                }
                iter.next();
                for _ in 0..devices {
                    QuickKeys::new();
                    /*match iter.next() {
                        Some(val) => 
                    }*/
                }
            }
            else {
                println!("{}", FILE_OPEN_ERR);
            }
        }
    }*/
    
    pub fn load_prefs(&mut self) {
        match File::open(PREF_FILE) {
            Ok(mut file) => {
                let mut json_str = String::new();
                file.read_to_string(&mut json_str);
                let data: Preferences = serde_json::from_str(&*json_str).unwrap();
                self.profiles = data.profiles().clone();
                self.devices = data.devices().clone();
            },
            Err(err) => println!("{}", err),
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
    
    //fn set_var(&mut self, var: &mut String
    
    pub fn write_prefs(&self) {
        match File::create(PREF_FILE) {
            Ok(mut file) => {
                let json_str = serde_json::to_string(self).unwrap();
                println!("{}", json_str);
                file.write_all(&*json_str.as_bytes());
            },
            Err(err) => println!("{:?}", err),
        }
    }
    
    pub fn profiles(&self) -> &Vec<Profile> {
        return &self.profiles;
    }
    
    pub fn devices(&self) -> &Vec<QuickKeys> {
        return &self.devices;
    }
}
