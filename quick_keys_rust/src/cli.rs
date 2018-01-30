use PREFS;
use qkdev::QKDev;

pub fn cli() {
    let mut devices: Vec<QKDev> = PREFS.lock()
                                       .unwrap()
                                       .devices()
                                       .clone()
                                       .iter()
                                       .map(|d| QKDev::new_from(d))
                                       .collect();
    main_menu(&mut devices);
    for mut qk in &mut devices {
        qk.stop();
    }
}

fn print_main_menu() {
    println!("1. Lists devices");
    println!("2. Switch to device");
    println!("3. Add device");
    println!("4. Remove device");
    println!("5. Exit");
}

fn main_menu(devices: &mut Vec<QKDev>) {
    let mut choice: i32;
    while {
        print_main_menu();
        scan!("{}", choice);
        //println!("{}", choice);
        match choice {
            1 => list_devices(devices),
            //2 => device_menu(),
            //3 => add_device(),
            //4 => remove_device(),
            5 => println!("Exit"),
            _ => println!("Invalid option selected"),
        }
        
        /* do-while condition */
        choice != 5
    } {}
    //while next input isnt EXIT
        //check for another input
        //run appropriate function
}

fn list_devices(devices: &Vec<QKDev>) {
    let device_names: Vec<&str> = devices.iter().map(|d| d.device().port()).collect();
    println!("ID\tPort");
    for i in 0..device_names.len() {
        println!("{}\t{}", i, device_names[i]);
    }
    println!("");
}
