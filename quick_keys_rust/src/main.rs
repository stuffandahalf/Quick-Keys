extern crate serialport;
extern crate enigo;

mod quickkeys;
mod profile;
mod qklib;

const KEYS: usize = 6;

fn main() {
    println!("Hello, world!");
    //qklib::serial_test();
    //qklib::enigo_test();
    //let mut test = profile::Profile::new();
    //println!("{}", test.get_name());
    //println!("{:?}", test.get_symbols());
    //qklib::emit_string(test.get_symbols(0));
    let test = quickkeys::QuickKeys::new();
    //println!("{:?}", test.get_profile().get_name());
    println!("{}". test.get_profile().get_symbol(0));
    //let test2 = profile::Profile::new();
    //println!("{}", test2.get_symbol(0));
}
