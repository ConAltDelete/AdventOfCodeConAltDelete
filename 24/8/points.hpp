#include <string>
#include <vector>
#include <set>
#include <unordered_map>

class board_info {
    public:
        int width;
        int hight;

        bool ApplyRules(int point[2]){
            return (point[0]>0 && point[0] < width) && (point[1]>=0 && point[1] < hight);
        }
};


void collaps_maps(std::set<int[2]>* , std::unordered_map<char,std::vector<int[2]>>* );
std::unordered_map<char,std::vector<int[2]>>* find_points(std::string , int );
void print_hello(std::string);
int find_n_antinodes(std::unordered_map<char,std::vector<int[2]>>* );
void find_antinodes( int (*)[4], int [2], int [2]);
int find_antinodes( board_info , int (*)[4], int [2], int [2]);
void merge_mappings(std::unordered_map<char,std::vector<int[2]>>* ,std::unordered_map<char,std::vector<int[2]>>* );