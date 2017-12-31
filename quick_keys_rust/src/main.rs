extern crate serialport;
extern crate enigo;

mod quickkeys;
mod profile;
//mod qklib;

const KEYS: usize = 6;

fn main() {
    let qkdev = quickkeys::QuickKeys::new();
    qkdev.main_script();
}
