#include <sstream>
#include <iostream>
#include <fstream>
#include <vector>

enum file_type{
	FIL,
	DIREC,
	NEITHER
};

class computer {
	std::string name;
	computer* parent;
	size_t bytes = 0;
	size_t num_e = 0;
	file_type type = NEITHER;
	std::vector<computer> content;


	public:
		computer(std::string name,size_t size, file_type F){
			this->bytes = size;
			this->type = F;
			this->name = name;
		}
		size_t get_size(){
			return this->bytes;
		}
		size_t get_count(){
			return this->num_e;
		}
		size_t get_cum_byte(){
			size_t total = this->bytes;
			if(this->type != DIREC){
				return total;
			}
			for(computer c : this->content){
				total += c.get_cum_byte();
			}
			return total;
		}
		size_t get_cum_byte(size_t limit){
			size_t total = 0;
			if(this->bytes <= limit){
				total = this->bytes;
			}
			if(this->type != DIREC){
				return total;
			}
			for(computer c : this->content){
				total += c.get_cum_byte(limit);
			}
			return total;
		}
		void set_perent(computer *p){
			this->parent = p;
		}
		computer* get_perent(){
			return this->parent;
		}
		std::string get_name(){
			return this->name;
		}
		void append(computer new_c){
			this->bytes += new_c.get_size();
			this->num_e++;
			this->content.push_back(new_c);
		}
		bool get_element(std::string F, computer &ref){
			for(computer c : this->content){
				if(c.get_name() == F){
					ref = c;
					return true;
				}
			}
			return false;
		}
		computer* cd_root(){
			if(this->name == "/"){
				return this;
			}
			static computer current = *this;
			while(current.get_name() != "/"){
				current = *current.get_perent();
			}
			return &current;
		}
};

int main() {
	std::ifstream file("input.txt");
	std::stringstream line;
	std::string new_line,word;
	std::vector<std::string> tolks;

	computer my_computer("/",0,DIREC);
	computer* temp_comp;

	while(file){
		std::getline(file, new_line);
		if(new_line.size() == 0){
			continue;
		}
		line.str(new_line);
		while(line >> word){
			tolks.push_back(word);
		}

		if(tolks[0] == "$"){
			if(tolks[1] != "ls"){
				if(tolks[2] == "/"){
					my_computer = *my_computer.cd_root();
				} else {
					if(!my_computer.get_element(tolks[2], my_computer)){
						std::cout << "Failed to find \"" << tolks[2] << "\" in \"" << my_computer.get_name() << "\"\n";
					}
				}
			}
		} else if (tolks[0] == "dir") {
			temp_comp = new computer(tolks[1],0,DIREC);
			temp_comp->set_perent(&my_computer);
			my_computer.append(*temp_comp);
		} else {
			temp_comp = new computer(tolks[1],std::stoi(tolks[0]),FIL);
			temp_comp->set_perent(&my_computer);
			my_computer.append(*temp_comp);
		}

		delete temp_comp;

		tolks.clear();
		line.clear();
		new_line.clear();
	}

	my_computer = *my_computer.cd_root();

	std::cout << "Part 1: " << my_computer.get_cum_byte(100000) << "\n";

	return 0;
}
