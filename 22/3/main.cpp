#include<iostream>
#include<fstream>
#include<string>
#include<map>

std::map<char,int> make_dict(std::string line){
	std::map<char,int> collect;

	for(char letter: line){
		if(collect.find(letter) == collect.end()){
			collect[letter] = 1;
		} else {
			collect[letter]++;
		}
	}

	return collect;
}

char find_common(std::map<char,int> P1,std::map<char,int> P2){
	for(std::map<char,int>::iterator ptr = P1.begin(); ptr != P1.end(); ptr++){
		if(P2.find(ptr->first) != P2.end()){
			return ptr->first;
		}
	}
	return NULL;
}
char find_common(std::map<char,int> P1,std::map<char,int> P2,std::map<char,int> P3){
	for(std::map<char,int>::iterator ptr = P1.begin(); ptr != P1.end(); ptr++){
		if(P2.find(ptr->first) == P2.end()){
			continue;
		}
		if(P3.find(ptr->first) == P3.end()){
			continue;
		}
		return ptr->first;
	}
	return NULL;
}

int main(int args, char* argv[]) {
	std::string file_name = "input.txt";

	std::ifstream file(file_name);

	std::string line, line2, line3, P1, P2;
	std::map<char,int> Map1,Map2,Map3;
	char common;
	int score, total = 0, total2 = 0;

	while(file){
		std::getline(file,line);
		if(line.size() == 0 || line.size() % 2 != 0){
			break;
		}
		P1 = line.substr(0,line.size()/2);
		P2 = line.substr(line.size()/2,line.size()/2);
		Map1 = make_dict(P1);
		Map2 = make_dict(P2);
		common = find_common(Map1,Map2);
		if(common == NULL){
			std::cout << "Failed!\n";
		}
		score = int(common);
		if(score < 97){
			total += score - 64 + 26;
		} else {
			total += score - 96;
		}
		Map1 = make_dict(line);
		std::getline(file,line);
		Map2 = make_dict(line);
		std::getline(file,line);
		Map3 = make_dict(line);

		common = find_common(Map1,Map2,Map3);
		score = int(common);
		if(score < 97){
			total2 += score - 64 + 26;
		} else {
			total2 += score - 96;
		}
	}
	std::cout << "Part 1: " << total << "\n";
	std::cout << "Part 2: " << total2 << "\n";
	return 0;
}
