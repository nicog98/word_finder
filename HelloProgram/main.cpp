#include <iostream>
#include <fstream>
#include <istream>

using std::cout;
using std::endl;
using std::string;

/*
Main function writing to a file
int main() {
    //cout << "Hello, World!" << endl;
    int favoritenumber = 1729;
    cout << "result when writing to console: " << favoritenumber << endl;
    std::ofstream outputFile("out.txt");
    outputFile << "Result when writing to file: " << favoritenumber << endl;
    return 0;
}
*/


Function that shows passing streams by reference
void writeToStream(std::ostream& anyOutputStream, int favoriteNumber) {
    anyOutputStream << "Writing to stream: " << favoriteNumber << endl;
}

int main() {
    int favoriteNumber = 1729;
    writeToStream(cout, favoriteNumber);
    return 0;
}

