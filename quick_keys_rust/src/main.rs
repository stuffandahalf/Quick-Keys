extern crate serialport;
extern crate enigo;
extern crate gtk;
//extern crate xml_lib;
//extern crate serde;
//extern crate serde_json;

//mod quickkeystest;
mod profile;
mod quickkeys;
mod preferences;
mod qkdev;
//mod qklib;
mod editor;

const KEYS: usize = 6;
const PREF_FILE: &str = "QuickKeys.pref";

use std::thread;
use std::sync::mpsc;
use std::time;

fn main() {
    /*let mut profiles: Vec<profile::Profile> = Vec::new();
    profiles.push(profile::Profile::new());
    
    let mut devices: Vec<qkdev::QKDev> = Vec::new();
    
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
    #[cfg(target_os = "linux")]
    //let mut qk = qkdev::QKDev::new("/dev/ttyUSB0");
    devices.push(qkdev::QKDev::new("/dev/ttyUSB0"));
    #[cfg(target_os = "windows")]
    //let qk = qkdev::QKDev::new("COM4");
    devices.push(qkdev::QKDev::new("COM4"));
    #[cfg(target_os = "macos")]
    //let qk = qkdev::QKDev::new("");
    devices.push(qkdev::QKDev::new(""));
    
    let e = editor::EditorWindow::new();
    gtk::main();
    
    for mut qk in &mut devices {
        qk.stop();
    }*/
    //xml_lib::xml::test();
    let pref = preferences::Preferences::new();
    println!("{:?}", pref);
}
