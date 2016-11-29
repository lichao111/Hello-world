#include <string>
#include <iostream>
using namespace std;
typedef struct ListNode{
	int val;
	ListNode* next;
}ListNode;
extern int k=9;
int main(){
	constexpr int i=9;
	int s[i]={1,2,3,4,5,6,7,8,9};
	for(auto it:s){
		std::cout<<it<<std::endl;
	}
	std::cout<<"-------"<<std::endl;
	std::string a("Iamsdfffffffffflicihao");
	std::cout<<sizeof(a)<<std::endl;
	char h[3]="Ia";
	std::cout<<sizeof(h)<<std::endl;
	cout<<"+++++++++++++++++"<<endl;
	ListNode List;
	List.val=0;
	ListNode er;
	er.val=1;
	er.next=&List;
	cout<<er.val<<" "<<er.next->val<<endl;
	short u;
	cout<<sizeof(u)<<endl;
	int p(8);
	cout<<p<<endl;
//	extern int k(9);
	//cout<<k<<endl;
	return 0;
}
