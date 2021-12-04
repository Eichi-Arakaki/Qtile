// (Full example with detailed comments in examples/17_yaml.rs)
//
// This example demonstrates clap's building from YAML style of creating arguments which is far
// more clean, but takes a very small performance hit compared to the other two methods.
#[macro_use]
extern crate clap;
use clap::App;

fn main() {
    // The YAML file is found relative to the current file, similar to how modules are found
    let yaml = load_yaml!("./cli.yml");
    let matches = App::from_yaml(yaml).get_matches();

    match matches.value_of("eww") {
        Some(i) => println!("asd"),
        _ => println!("a")
    }
}