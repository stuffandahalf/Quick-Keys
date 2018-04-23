#[macro_use]
extern crate lazy_static;
#[macro_use]
extern crate text_io;
extern crate serialport;
extern crate enigo;
extern crate gtk;

#[macro_use]
extern crate serde_derive;
extern crate serde;
extern crate serde_json;

mod profile;
mod quickkeys;
//mod quickkeystest;
mod preferences;
mod qkdev;
//mod qklib;
//mod editor;
mod cli;

use std::sync::Mutex;

const KEYS: usize = 6;
//const PREF_FILE: &str = "../resources/QuickKeys.pref";
const PREF_FILE: &str = "/home/ubuntu/Desktop/QuickKeys.pref";

/*#[cfg(target_os = "linux")]
const PREF_FILE: &str = "~/.QuickKeys.pref"; */

lazy_static! {
    static ref PREFS: Mutex<preferences::Preferences> = Mutex::new(preferences::Preferences::new());
}

fn main() {
    //let mut profiles: Vec<profile::Profile> = Vec::new();
    //profiles.push(profile::Profile::new());
    //let mut pref = preferences::Preferences::new();
    
    //let mut devices: Vec<qkdev::QKDev> = Vec::new();
    /*let mut devices: Vec<qkdev::QKDev> = PREFS.lock().unwrap().devices().iter().map(|d| qkdev::QKDev::new_from(d)).collect();
    println!("DEVICES FROM PREFS: {:?}", devices);
    
    if let Ok(ports) = serialport::available_ports() {
        let port_names: Vec<&str> = ports.iter().map(|p| &*p.port_name).collect();
        //let port_names: Vec<std::string::String> = ports.iter().map(|p| format!("{:?} by {:?} on {}", p.product, p.manufacturer, &*p.port_name)).collect();
        println!("Available serial ports");
        for p in port_names {
            println!("{:?}", p);
        }
        println!("");
    }
    
    /* Initial default ports for every OS */
    /*#[cfg(target_os = "linux")]
    //let mut qk = qkdev::QKDev::new("/dev/ttyUSB0");
    devices.push(qkdev::QKDev::new("/dev/ttyUSB0"));
    #[cfg(target_os = "windows")]
    //let qk = qkdev::QKDev::new("COM4");
    devices.push(qkdev::QKDev::new("COM4"));
    #[cfg(target_os = "macos")]
    //let qk = qkdev::QKDev::new("");
    devices.push(qkdev::QKDev::new(""));*/
    
    let _e = editor::EditorWindow::new();
    
    /*println!("{:?}", pref);
    devices[0].set_symbol(&mut pref, 0, "test");
    println!("{:?}", pref);*/
    
    for mut qk in &mut devices {
        qk.stop();
    }
    
    PREFS.lock().unwrap().reset_devices(&mut devices);
    PREFS.lock().unwrap().write_prefs();
    
    //println!("{:?}", PREFS.profiles());*/
    
    /*println!("{:?}", PREFS.lock().unwrap().profiles());
    let mut qk = qkdev::QKDev::new("/dev/ttyUSB0");
    qk.set_symbol(0, "test");
    println!("{:?}", qk);
    println!("{:?}", PREFS.lock().unwrap().profiles());*/
    //println!("{:?}", PREFS.lock().unwrap());
    cli::cli();
}
