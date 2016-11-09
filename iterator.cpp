#include <iostream>
#include <vector>
int main(){
	std::vector<int> a;
	for(int i=0;i<7;++i){
		a.push_back(i);
	}
	a.push_back(100);
	std::vector<int>::iterator it;
	it =a.begin()+7;
	std::cout<<std::endl<<*it<<std::endl;
	std::cout<<*(a.end()-1)<<std::endl;
	int i=3&0x1;//转换成二进制以后只保留最后一位，而最后一位决定了一个数是奇数还是偶数！！
	std::cout<<i<<std::endl;
	return 0;
	
}
