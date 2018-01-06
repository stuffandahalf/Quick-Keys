extern crate serialport;
extern crate enigo;

mod quickkeys;
mod profile;
//mod qklib;

const KEYS: usize = 6;

fn main() {
    //let profiles: Vec<profile::Profile> = Vec::new();
    
    if let Ok(ports) = serialport::available_ports() {
        for p in ports {
            println!("{:?}", p);
        }
    }
    
    /* Initial default ports for every OS */
    #[cfg(target_os = "linux")]
    let qkdev = quickkeys::QuickKeys::new_on("/dev/ttyUSB0");
    #[cfg(target_os = "windows")]
    let qkdev = quickkeys::QuickKeys::new_on("COM4");
    #[cfg(target_os = "macos")]
    let qkdev = quickkeys::QuickKeys::new_on("");
    
    qkdev.main_script();
}
