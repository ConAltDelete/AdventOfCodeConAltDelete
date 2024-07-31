#include <fstream>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

int main() {
	std::string input_file = "input.txt";

	std::ifstream file(input_file);

	std::vector<int> calories;

	std::vector<std::vector<int>> elfs;

	std::string line;

	bool elf = false;

	while(file){
		std::getline(file,line);
		if(elf && (line == "")){
			elfs.push_back(calories);
			calories.clear();
			elf = false;
		} else if (!elf && (line != "")) {
			elf = true;
			calories.push_back(std::stoi(line));
		} else if (elf && (line != "")) {
			calories.push_back(std::stoi(line));
		}
	}
	

	std::vector<int> elf_sums;
	int elf_sum;
	for(auto elf : elfs){
		elf_sum = 0;
		for(auto cal : elf) {
			elf_sum += cal;
		}
		elf_sums.push_back(elf_sum);
	}

	std::sort(elf_sums.begin(), elf_sums.end());

	std::cout << "Part 1: " << elf_sums.back() << "\n";

	int k = 3;
	int sum = 0;

	for(auto i = elf_sums.rbegin(); i < elf_sums.rend(); i++){
		std::cout << "Current numbers:\n";
		if(k > 0){
			std::cout << *i << "\n";
			sum += *i;
			k--;
		} else {
			break;
		}
	} 
	std::cout << "Part 2: " << sum <<"\n";
}
