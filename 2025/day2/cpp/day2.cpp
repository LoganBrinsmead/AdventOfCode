#include <iostream>
#include <fstream>
#include <algorithm>

int main() {
    std::ifstream inputFile;

    inputFile.open("../input.txt");

    // we start at 50
    // rotate to 0 if > 99, 99 if < 0
    int place = 50;

    if(!inputFile.is_open()) {
        std::cerr << "Error: could not open input file." << std::endl;
        return 1; 
    }

    std::string line;
    char direction;
    int rotations;

    // count how many 0s we arrive to
    int res = 0;

    while(inputFile >> line) {
        // strip whitespace from the string
        line.erase(remove_if(line.begin(), line.end(), isspace), line.end());


        // remove and get the direction char from the input
        direction = line.front();
        line.erase(0, 1);

        // assuming the rest of the line is an integer
        rotations = std::stoi(line);

        if(direction == 'R') {
            while(rotations > 0) {
                place += 1;

                if(place == 100) {
                    place = 0;
                }

                if(place == 0) {
                    res += 1;
                }

                rotations -= 1;
            }


        } else if(direction == 'L') {
            while(rotations > 0) {
                place -= 1;

                if (place == -1) {
                    place = 99;
                }

                if(place == 0) {
                    res += 1;
                }

                rotations -= 1;
            }
        }


    }

    std::cout << "Result: " << res << std::endl;
    return res;
}