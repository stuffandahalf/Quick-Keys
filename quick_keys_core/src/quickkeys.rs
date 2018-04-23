use std::path::Path;
use std::string::String;
use std::thread;
use std::sync::mpsc::Receiver;
use serialport;
use enigo::{Enigo, KeyboardControllable};

pub struct QuickKeys {
    port: String,
}

impl QuickKeys {
    pub fn new(port: &str) -> Result<QuickKeys, String> {
        //if 
        QuickKeys {
            port: String::from(port),
        }
    }
}
