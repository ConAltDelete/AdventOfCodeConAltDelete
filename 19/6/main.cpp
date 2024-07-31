#include<iostream>
#include <iterator>
#include <string>

class planet {
	public:
		std::string center;
		int degree = 0; // antall planeter den indirekte går rund
		int n_moons = 0; // antall måner
		planet** moons = nullptr; // liste av måner
		// planet(std::string name, int deg, int nmoon, planet* mo);
		int count(){
			int sum = n_moons+degree;
			for(int i = 0; i < n_moons; i++){
				sum += moons[i]->count();
			}
			return sum;
		}

		planet operator+(planet new_moon){
			planet* moon[n_moons + 1];
			for(int i = 0;i < n_moons; i++){
				moon[i] = moons[i];
			}
			moon[n_moons] = &new_moon;
			moon[n_moons]->degree += 1;
			planet updated_planet = planet{center,degree,n_moons+1,moon};
			return updated_planet;
		}
};
/*
planet::planet(std::string name, int deg, int nmoon, planet* mo){
	center = name;
	degree = deg;
	n_moons = nmoon;
	moons = mo;
};
*/
class galaxy {
	std::string name;
	planet origin;
};

void test_planet() {
	std::cout<<"entered test function\n";
	std::string test_planets[] = {
		"A", "B", "C"
	};
	planet origin;

	std::cout<<"initelized origin\n";

	origin.center = "COM";
	for(int i = 0; i<3;i++){
		origin = origin + planet{test_planets[i],0,0,nullptr};
		std::cout << "preformed add\n";
		std::cout<< "Moon name: " << test_planets[i]<<"\nnumber of planets: " << origin.degree << "\nnumber of moons: "<< origin.n_moons<<"\n";
	}
	std::cout << "moon names:\n";
	for(int i = 0; i< origin.n_moons;i++){
		planet* moon = origin.moons[i];
		std::cout << moon->center << "\n";
	}
}

int main(int narg, char** argv){
	std::cout << "starting.\n";
	test_planet();
	std::cout << "ending.\n";

	return 0;
}
