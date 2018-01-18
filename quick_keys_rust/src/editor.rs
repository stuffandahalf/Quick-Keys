use std::string::String;
use gtk;
use gtk::prelude::*;
use gtk::{Button, Window, WindowType};

pub struct EditorWindow {
    window: Window,
}

impl EditorWindow {
    pub fn new() -> Result<EditorWindow, String> {
        if gtk::init().is_err() {
            return Err(String::from("gtk could not be initialized"));
        }
        let mut ew = EditorWindow {
            window: Window::new(WindowType::Toplevel),
        };
        EditorWindow::win_init(&mut ew.window);
        gtk::main();
        return Ok(ew);
    }
    
    fn win_init(window: &mut Window) {
        window.set_title("QuickKeys");
        //window.
        window.show_all();
        
        window.connect_delete_event(|_, _| {
            gtk::main_quit();
            Inhibit(false)
        });
    }
}
