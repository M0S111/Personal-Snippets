// Huffman Coding program in c++

#include <bits/stdc++.h> 
using namespace std; 
  

class HeapNode_Min { // Tree node of Huffman      
  
  public:
  
  	char d;
  	unsigned f;
  	HeapNode_Min *l, *r;
    
//Add data members here.  
 
    HeapNode_Min(char d, unsigned f = -1) 
    { 
		this->d = d;
		this->f = f ;
		this->l = NULL;
		this->r = NULL;
    } 
}; 
  
class Analyze {  // two heap nodes comparison
  
  public:
    bool operator()(HeapNode_Min* l, HeapNode_Min* r) 
    { 
        return (l->f > r->f); //Complete this statement
    } 
}; 
  
void display_Codes(HeapNode_Min* root, string s) // To print codes of huffman tree from the root. 
{   
    if (!root) 
        return; 
  
    if (root->d != '$') 
        cout << root->d << "\t: " << s << "\n";
  
    display_Codes(root->l, s + "0"); 
    display_Codes(root->r,  s + "1"); //Complete this statement by passing arguments
 
} 
  

void HCodes(char data[], int freq[], int s) // builds a Huffman Tree
{ 
    HeapNode_Min  *t,*r, *l ;  // top, right, left

  
    priority_queue<HeapNode_Min*, vector<HeapNode_Min*>, Analyze> H_min; 
  
    int a=0;
    while (a<s){H_min.push(new HeapNode_Min(data[a], freq[a])); ++a;}
    
  
    while (H_min.size() != 1) { 
  
        l = H_min.top(); H_min.pop(); 
        r = H_min.top(); H_min.pop(); 
  
        t = new HeapNode_Min('$',  r->f + l->f); 
  
        t->r = r; t->l = l; 
       
  
        H_min.push(t); 
    } 
  
    display_Codes(H_min.top(), ""); 
} 
  
int main() 
{ 
    int frequency[] = { 3, 6, 11, 14, 18, 25 };  char alphabet[] = { 'A', 'L', 'O', 'R', 'T', 'Y' };  
      int size_of = sizeof(alphabet) / sizeof(*alphabet); //Complete this statement by passing data type to both sizeof operators 
  
  cout<<"Alphabet"<<":"<<"Huffman Code\n";
  cout<<"--------------------------------\n";

   HCodes(alphabet, frequency, size_of);
   
   return 0; 
}
