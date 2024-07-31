#include<iostream>
#include<fstream>
#include<string>
#include<vector>

bool does_contain(int a1, int a2, int b1, int b2) {
	if((a2-a1)-(b2-b1) >= 0){
		if(a1 > b1){
			return false;
		}
		if(a2 < b2){
			return false;
		}
		return true;
	} else {
		if(a1 < b1){
			return false;
		}
		if(a2 > b2){
			return false;
		}
		return true;
	}
}

std::vector<std::string> split_string(std::string line, std::string delimiter) {
	std::vector<std::string> result;

	size_t pos, last = 0;

	while( (pos = line.find(delimiter,last)) != std::string::npos ){
		result.push_back(line.substr(last,line.size() - pos));
		last = pos + delimiter.size();
	}
	return result;
}

std::vector<std::string> split_string(std::vector<std::string> line, std::string delimiter) {
	std::vector<std::string> result;

	size_t pos, last;
	for(auto data : line){
		last = 0;
		pos = 0;
		while( (pos = data.find(delimiter,last)) != std::string::npos ){
			result.push_back(data.substr(last,data.size() - pos));
			last = pos + delimiter.size();
		}
	}
	return result;
}

int main(){

	std::string file_path = "input.txt";

	std::ifstream file(file_path);

	int a1,a2,b1,b2,total;

	std::string line;
	std::vector<std::string> tolkens,int_strings;
	std::vector<int> nums;

	bool containment;

	while(file){
		std::getline(file, line);
		if(line.size() == 0) break;
		std::cout << line << " -> ";
		tolkens = split_string(line,",");
		
		for(auto t:tolkens){
			std::cout << t << ", ";
		}
		int_strings = split_string(tolkens,"-");
		
		std::cout << " -> ";

		for(auto t:int_strings){
			std::cout << t << ", ";
		}
		std::cout << "\n";

		for(auto s: tolkens){
			nums.push_back(std::stoi(s));
		}
		
		containment = does_contain(nums[0], nums[1], nums[2], nums[3]);

		if(containment){
			total++;
		}
		nums.clear();
		tolkens.clear();
	}

	std::cout << "Part 1: " << total << "\n";
	
	return 0;
}
