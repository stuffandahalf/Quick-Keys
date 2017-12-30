extern crate serialport;

mod quickkeys;
mod profile;
mod qklib;

fn main() {
    //println!("Hello, world!");
    qklib::serial_test();
}
