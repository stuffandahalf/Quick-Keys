use profile::Profile;
use quickkeys::QuickKeys;
use PREF_FILE;

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
    
    /*pub fn load_prefs(&mut self) -> Preferences {
        
    }
    
    pub fn write_prefs(&self) {
        
    }*/
}
