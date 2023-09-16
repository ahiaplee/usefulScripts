#include <iostream>
#include <filesystem>
#include <format>

void hideOrShowFolder(const std::string& directory, bool hide)
{
	using namespace std::filesystem;
	// std::filesystem::path path{ directory };

	if(!exists(directory)){
		std::cout << std::format("File {} does not exist", directory) << std::endl;
		return;
	}

	auto command = hide ? std::format("attrib +h +s {}", directory) : 
						  std::format("attrib -h -s {}", directory);

	system(command.c_str());
	std::cout << std::format("File : {} is now {}", directory, hide ? "hidden." : "unhidden") << std::endl;
}

void resetCin()
{
	std::cin.clear();
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

void getInputAndRun(int choice)
{
	std::string path;
	std::cout << "Enter file name : ";
	std::cin >> path;
	hideOrShowFolder(path, choice == 1);
	resetCin();
}

void printBadChoice()
{
	std::cout << "Please Enter valid choice" << std::endl;
	resetCin();
}

int main()
{
	bool exit = false;
	int choice;
	while(!exit){
		std::cout << "Select Mode:" << std::endl;
		std::cout << "1. Hide" << std::endl;
		std::cout << "2. Unhide" << std::endl;

		std::cin >> choice;
		if(std::cin.fail()){
			printBadChoice();
			continue;
		}

		getInputAndRun(choice);
	}
	// system("pause");
}
