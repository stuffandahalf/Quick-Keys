//use PREF_FILE;
use preferences::Preferences;
use qkdev::QKDev;

//pub fn load_prefs() -> Preferences

pub fn set_symbol(device: &mut QKDev, prefs: &mut Preferences, sym: &str, index: usize) {
    let mut prof = prefs.find_profile(device.device().profile().name());
    prof.set_symbol(index, sym);
    device.device().set_profile(prof);
}
