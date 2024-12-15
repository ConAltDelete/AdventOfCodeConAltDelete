#include "points.hpp"
#include <iostream>
#include <unordered_map>
#include <set>
#include <vector>

int find_n_antinodes(std::unordered_map<char,std::vector<int[2]>>* mapping){
    std::set<int[2]> occupied_map; // nodes already exisiting
    std::set<int[2]> used_map = std::set<int[2]>(); // antinodes discoved

    collaps_maps(&occupied_map, mapping);

    std::vector<int[2]> current_points;
    int buff[4];

    int total_count = 0;

    for(auto& C : *mapping){
        current_points = C.second;
        for(int i = 0; i < current_points.size(); i++){
            for(int j = 0; j < i; j++){
                find_antinodes(&buff,current_points[i],current_points[j]);
                if((occupied_map.find({buff[0],buff[1]}) == occupied_map.end())&&(used_map.find({buff[0],buff[1]}) == used_map.end())){
                    total_count++;
                    used_map.insert({buff[0],buff[1]});
                }
                if((occupied_map.find({buff[2],buff[3]}) == occupied_map.end())&&(used_map.find({buff[2],buff[3]}) == used_map.end())){
                    total_count++;
                    used_map.insert({buff[2],buff[3]});
                }
            }
        }
    }
    return total_count;
}

void collaps_maps(std::set<int[2]>* target_map, std::unordered_map<char,std::vector<int[2]>>* collection_map){
    // merges a mapping to a vector stored to a taget set

    for(auto& el : *collection_map){
        for(auto& nodes : el.second){
            target_map->insert(nodes);
        }
    }
}

void find_antinodes( int (*buffer)[4], int pointA[2], int pointB[2]){
    // strategi: ikke regn lengde, regn vektor pga lengde blir irrasjonel.
    *buffer[0] = 2*pointB[0] - pointA[0];
    *buffer[1] = 2*pointB[1] - pointA[1];
    *buffer[2] = 2*pointA[0] - pointB[0];
    *buffer[3] = 2*pointA[1] - pointB[1];
}

int find_antinodes( board_info rules, int (*buffer)[4], int pointA[2], int pointB[2]){
    // strategi: ikke regn lengde, regn vektor pga lengde blir irrasjonel.
    // problemflag (int) indicates wether or not the first coordiante falls outside of bounds or the second one
    *buffer[0] = 2*pointB[0] - pointA[0];
    *buffer[1] = 2*pointB[1] - pointA[1];
    *buffer[2] = 2*pointA[0] - pointB[0];
    *buffer[3] = 2*pointA[1] - pointB[1];

    int problemFlag = 0;

    int p1[2] = {*buffer[0],*buffer[1]};
    int p2[2] = {*buffer[2],*buffer[3]};

    if(!rules.ApplyRules(p1)){
        problemFlag += 0b01;
    }
    if(!rules.ApplyRules(p2)){
        problemFlag += 0b10;
    }
    return problemFlag;
}

void merge_mappings(std::unordered_map<char,std::vector<int[2]>>* target_map,std::unordered_map<char,std::vector<int[2]>>* mapB){
    /*
    * Merges two mappings such that entries in mapB gets inserted into target_map.
    * - there are no overlapping keys, then the maps are combined
    * - if there are overlapping keys, then the vectors get combined.
    */

   for(auto& [key,element] : *mapB){
        if(target_map->find(key) != target_map->end()){
            target_map[key].merge(mapB[key]);
        } else {
            target_map->insert_or_assign(key,element); 
        }
   }
}

std::unordered_map<char,std::vector<int[2]>>* find_points(std::string line, int offset_y){
    /*
    * Looks through a scanned line of characters and finds the coordinates of characters.
    * Applies an offset to y coords if line is part of a greater grid.
    *! Assumes there are no special characters other than Alphabet characters!
    */
    std::unordered_map<char,std::vector<int[2]>> line_mapping;
    int found_coord[2];
    for(int i = 0; i < line.length(); i++){
        if((line[i] != '.')&&(line_mapping.find(line[i]) != line_mapping.end())){
            found_coord = {i,offset_y};
            line_mapping[line[i]].push_back(
                found_coord
            );
        }
    }
    return &line_mapping;
}

void print_hello(std::string name){
    std::cout << "Hello " << name << ", how are you?" << std::endl;
}