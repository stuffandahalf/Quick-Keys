extern crate serialport;
extern crate enigo;

mod quickkeys;
mod profile;
//mod qklib;

const KEYS: usize = 6;

fn main() {
    //let profiles: Vec<profile::Profile> = Vec::new();
    let qkdev = quickkeys::QuickKeys::new();
    qkdev.main_script();
}
