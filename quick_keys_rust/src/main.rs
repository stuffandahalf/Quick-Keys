extern crate serialport;
extern crate enigo;

mod quickkeys;
mod profile;
//mod qklib;

const KEYS: usize = 6;

fn main() {
    //let profiles: Vec<profile::Profile> = Vec::new();
    let qkdev = quickkeys::QuickKeys::new();
    //let qkdev = quickkeys::QuickKeys::new_from("COM4");
    //let qkdev = quickkeys::QuickKeys::new_from("/dev/ttyUSB0");
    qkdev.main_script();
}
