#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>

std::vector<std::string> split_string(std::string line, char delim) {
	size_t pos = 0, last = 0;

	std::vector<std::string> result;

	while(pos != std::string::npos){
		pos = line.find(delim,last);
		result.push_back(line.substr(last,pos - last));
		last = pos + 1;
	}
	//result.push_back(line.substr(last,line.size()-last));
	return result;
} 

template<typename T>
void print_vector(std::vector<T> vec){
	std::cout << "{";
	for(auto i = vec.begin(); i != vec.end(); i++){
		std::cout << *i << ", ";
	}
	std::cout << "}";
}

int main() {
	std::map<int,std::vector<char>> create = {
		{1,std::vector<char>{'W','B','D','N','C','F','J'}},
		{2,std::vector<char>{'P','Z','V','Q','L','S','T'}},
		{3,std::vector<char>{'P','Z','B','G','J','T'}},
		{4,std::vector<char>{'D','T','L','J','Z','B','H','C'}},
		{5,std::vector<char>{'G','V','B','J','S'}},
		{6,std::vector<char>{'P','S','Q'}},
		{7,std::vector<char>{'B','V','D','F','L','M','P','N'}},
		{8,std::vector<char>{'P','S','M','F','B','D','L','R'}},
		{9,std::vector<char>{'V','D','T','R'}},
	};

	std::ifstream file("input.txt");

	std::vector<std::string> command;
	std::vector<char> dock;

	int size, c1,c2, i;
	char bay;

	std::string line;

	while(file){
		std::getline(file, line);
		if(line.size() == 0) break;
		command = split_string(line, ' ');

		size = std::stoi(command[1]);
		c1 = std::stoi(command[3]);
		c2 = std::stoi(command[5]);
		
		std::cout << "Commands: " << size << " " << c1 << " " << c2 << "\n";
		std::cout << "Before: ";
		print_vector(create[c1]);
		std::cout << " -> ";
		print_vector(create[c2]);
		for(i = 0; i < size; i++){
			bay = create[c1].back();
			create[c1].pop_back();
			create[c2].push_back(bay);
		}
		std::cout << "\nAfter: ";
		print_vector(create[c1]);
		std::cout << " -> ";
		print_vector(create[c2]);
		std::cout << std::endl;

	}

	std::cout << "Part 1: ";
	for(auto s : create){
		std::cout << "crate " << s.first << ": ";
		for(auto c = s.second.begin(); c != s.second.end(); c++){
			std::cout << *c;
		}
		std::cout << "\n";
	}
	std::cout << "\n";

	return 0;
}
