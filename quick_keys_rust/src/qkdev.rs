use PREFS;

use quickkeys::QuickKeys;
use profile::Profile;
use preferences::Preferences;
use std::thread;
use std::sync::mpsc::{channel, Sender, Receiver};
use std::mem;

#[derive(Debug)]
pub struct QKDev {
    device: QuickKeys,
    profile: Profile,
    handle: Option<thread::JoinHandle<()>>,
    tx: Option<Sender<bool>>,
}

impl QKDev {
    pub fn new(port: &str) -> QKDev {
        let (tx, rx) = channel::<bool>();
        let mut qk = QKDev {
            device: QuickKeys::new_on(port),
            profile: Profile::new(),
            handle: None,
            tx: Some(tx),
        };
        qk.init(rx);
        return qk;
    }
    
    pub fn new_from(device: &QuickKeys) -> QKDev {
        return QKDev {
            device: device.clone(),
            profile: Profile::new(),
            handle: None,
            tx: None,
        };
    }
    
    fn init(&mut self, rx: Receiver<bool>) {
        let local_dev = self.device().clone();
        let local_prof = self.profile().clone();
        self.handle = Some(thread::spawn(move || {
            local_dev.start(rx, local_prof);
        }));
    }
    
    pub fn start(&mut self) {
        let (tx, rx) = channel::<bool>();
        self.tx = Some(tx);
        self.init(rx);
    }
    
    pub fn stop(&mut self) {
        if let Some(tx) = self.tx.clone() {
            let _tx_res = tx.send(true);
            self.tx = None;
            let handle_opt = mem::replace(&mut self.handle, None);
            if let Some(handle) = handle_opt {
                let _hande_res = handle.join();
            }
        }
        else {
            println!("tx is not initialized");
        }
    }
    
    pub fn device(&self) -> &QuickKeys {
        return &self.device;
    }
    
    pub fn set_symbol(&mut self, index: usize, symbol: &str) {
        /*self.stop();
        if let Some(mut edit_prof) = pref.find_profile(self.profile().name()) {
            edit_prof.set_symbol(index, sym);
        }
        self.start();*/
        match PREFS.try_lock() {
            Ok(mut prefs) => {
                self.stop();
                //change this to move out value
                match prefs.find_profile(self.profile().name()) {
                    Some(mut local_profile) => {
                        local_profile.set_symbol(index, symbol);
                        self.set_profile(local_profile.clone());
                        prefs.add_profile(&local_profile);
                    },
                    None => {
                        //edit local and add to PREFS
                        self.profile.set_symbol(index, symbol);
                        prefs.add_profile(self.profile());
                    },
                }
                self.start();
            }
            Err(err) => println!("{}", err),
        }
    }
    
    pub fn profile(&self) -> &Profile {
        return &self.profile;
    }
    
    pub fn set_profile(&mut self, new_profile: Profile) {
        self.profile = new_profile;
    }
    
    /*fn move_device(self) -> QuickKeys {
        return self.device;
    }*/
    
    /*pub fn handle(&self) -> &Option<thread::JoinHandle<()>> {
        return &self.handle;
    }*/
}
