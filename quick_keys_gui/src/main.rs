extern crate gtk;
extern crate quick_keys_core;

use quick_keys_core::QKCore;

fn main() {
    //println!("Hello, world!");
    let core = QKCore::new("~/Desktop/quickkeys.conf");
    println!("{:?}", core);
}
