#include <iostream>
#include <fstream>
#include <unordered_map>
#include <stdexcept>
#include <string>
#include <vector>
#include "points.hpp"



int main(void){
    std::string file_name = "input";
    std::ifstream file;
    file.open(file_name,std::ios::in);

    if(!file.is_open()){
        throw std::runtime_error("Could not open file!");
    }

    std::string line;
    std::unordered_map<char,std::vector<int[2]>> node_map;
    std::unordered_map<char,std::vector<int[2]>>* line_nodes;
    
    int y = 0;
    while(std::getline(file,line)){
            line_nodes = find_points(line, y);
            merge_mappings(&node_map,line_nodes);
            y++;
    }
    file.close();

    int max_length = y;
    int max_width = line.length();
    
    int unique_node_count = find_n_antinodes(&node_map);

    std::cout << "Part 1: " << std::to_string(unique_node_count) << " unique nodes." << std::endl;
    
    return 0;
}

