#include <iostream>
#include <string.h>
#include <string>
#include <cstring>
#include <fstream>
#include <map>

int score_calc(char P2, char P1){
	std::map<char,char> conv = {
		std::pair<char,char>('X','A'),
		std::pair<char,char>('Y','B'),
		std::pair<char,char>('Z','C')
	};
	std::map<char,char> rule = {
		std::pair<char,char>('A','C'),
		std::pair<char,char>('B','A'),
		std::pair<char,char>('C','B')
	};
	std::map<char,int> score = {
		std::pair<char,int>('A',1),
		std::pair<char,int>('B',2),
		std::pair<char,int>('C',3)
	};

	int val1,val2;

	val2 = score[P2];
	val1 = score[conv[P1]];
	if(val1 == val2){
		val1 += 3;
	} else if (P2 == rule[conv[P1]]){
		val1 += 6;
	}

	return val1;
}

int inv_clac(char P2, char P1){
	std::map<char,char> conv = {
		std::pair<char,char>('A','X'),
		std::pair<char,char>('B','Y'),
		std::pair<char,char>('C','Z')
	};
	std::map<char,char> rule = {
		std::pair<char,char>('A','C'),
		std::pair<char,char>('B','A'),
		std::pair<char,char>('C','B')
	};
	std::map<char,char> inv_rule = {
		std::pair<char,char>('C','A'),
		std::pair<char,char>('A','B'),
		std::pair<char,char>('B','C')
	};
	
	char new_letter;

	switch (P1) {
		case 'X':
			new_letter = rule[P2];
			break;
		case 'Y':
			new_letter = P2;
			break;
		case 'Z':
			new_letter = inv_rule[P2];
			break;
		default:
			std::cout << "Error: " << P1 << "\n";
	};
	
	return score_calc(P2, conv[new_letter]);
}

int main(){
	std::string input_path = "./input.txt";

	std::ifstream file(input_path);

	int total = 0;
	int total2 = 0;
	int score;

	std::string line;
	char* tolk;
	char* saveptr;

	while(file){
		std::getline(file,line);
		if(line.size() == 0){
			break;
		}
		score = score_calc(line[0],line[2]);
		total += score;
		total2 += inv_clac(line[0], line[2]);
	}
	std::cout << "Part 1: " << total << "\n";
	std::cout << "Part 2: " << total2 << "\n";
}
