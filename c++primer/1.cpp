#include <iostream>
int main(){
	std::cerr<<"hellp world!!"<<std::endl;
	std::cout<<"Enter two numbers:"<<std::endl;
	int v1=0,v2=0;
	std::cin>>v1>>v2;
	std::cout<<"the sun of "<<v1<<" and "<<v2<<" is "<<v1+v2<<std::endl;
	int value;
	int sum=0;
	while(std::cin>>value)
		sum += value;
	std::cout<<"the sum is "<<sum<<std::endl;
	return 0;
}
