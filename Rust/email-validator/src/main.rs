extern crate regex;
extern crate colored;
use std::io;
use regex::Regex;
use colored::*;

fn main() {
    println!("Enter your E-mail Address : ");
    let mut mail =  String::new();
    io::stdin().read_line(&mut mail).expect("Provide Valid Mail ID !");
    let chunks: Vec<_> = mail.split('@').collect();
    let mut count : u32 = 0;
    let mut pre;
    let mut post;
    for s in chunks{
        if count==2 {
            println!("{}","Invalid Mail ID".red());
            return
        }
        if count==0 {
            pre = s;
            let mut pre_check : bool;
            let pre_regex = Regex::new(r"^[A-Za-z]+").unwrap();
            pre_check = pre_regex.is_match(pre);
           if pre_check == false {
               println!("{}","Email Address Must start with a character word only !".red());
               return
           }
        }else{
             post = s;
             let domains: Vec<_> = post.split('.').collect();
             for domain in domains{
                 let post_regex = Regex::new(r"^[a-z]+$|\n$").unwrap();
                 let post_check = post_regex.is_match(domain);
                 if post_check == false{
                     println!("{}","The Domain name is not allowed !".red());
                     return
                 }
             }
        }
        count += 1;
    }
    println!("{}","The Email Address Provided is available".green());
}
