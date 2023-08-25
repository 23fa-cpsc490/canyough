#include <iostream>
#include <string>

int main() {
    std::string hear_a_joke;

    std::cout << "Hello there. Would you like to hear a dad joke? (Yes/No)\n";
    std::cin >> hear_a_joke;

    if (hear_a_joke == "Yes" || "yes") {
        std::cout << "Where do fruits go on vacation?";
        std::cout << "\n.\n.\n.\n.\n.\n.\n.\n.\n.\nPear-is!\n";
    }
    std::cout << "Have a great day! Come again soon!";

    return 0;
}