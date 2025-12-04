use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

fn main() {
    let file_path = Path::new("../input.txt");
    
    // Open the file, handling potential errors
    let file = File::open(file_path).unwrap();
    let reader = BufReader::new(file);

    let mut result: i32 = 0;
    let mut line_number: i32 = 0;

    // Iterate over each line in the file
    for line_result in reader.lines() {
        let mut first_digit: char = '0';
        let mut first_index: usize = 0;
        let mut second_digit: char = '0';

        let line = line_result.unwrap(); // Handle or propagate errors during line reading

        // iterate over the line (battery bank)
        // find the first max
        for (i, n) in line.chars().enumerate() {
            let cur_digit_option = n.to_digit(10);

            match cur_digit_option {
                Some(digit) => {

                    // you cannot select the last element
                    if i == line.len() - 1 {
                        break;
                    }

                    if digit == 9 {
                        first_digit = '9';
                        first_index = i;
                        break;
                    } else if first_digit.to_digit(10).unwrap() < digit {
                        first_digit = std::char::from_digit(digit, 10).unwrap();
                        first_index = i;
                    }
                },
                None => {
                    println!("Error converting given number to a digit.");
                }
            }
        }

        for c in line.chars().skip(first_index + 1) {
            let cur_digit_option = c.to_digit(10);

            match cur_digit_option {
                Some(digit) => {
                    if digit == 9  {
                        second_digit = '9';
                        break;
                    } else if second_digit.to_digit(10).unwrap() < digit {
                        second_digit = std::char::from_digit(digit, 10).unwrap();
                    }
                }, 
                None => {
                    println!("Error converting second given character to integer.");
                }
            }
        }

        let combined_string = format!("{}{}", first_digit, second_digit);

        let max_voltage: i32 = combined_string.parse().unwrap();
        line_number+=1;
        println!("{}", line_number);
        print!("Current max_voltage: {}\n", max_voltage);

        result += max_voltage;
        println!("Current result: {}", result);


    }

    println!("Result: {}", result);

}
