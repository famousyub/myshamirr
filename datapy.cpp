
#include<iostream>

#include<string>


using namespace std ;


void findAndReplaceAll(std::string & data, std::string toSearch, std::string replaceStr)
{
    // Get the first occurrence
    size_t pos = data.find(toSearch);
    // Repeat till end is reached
    while( pos != std::string::npos)
    {
        // Replace this occurrence of Sub String
        data.replace(pos, toSearch.size(), replaceStr);
        // Get the next occurrence from the current position
        pos =data.find(toSearch, pos + replaceStr.size());
    }
}

int main(int argc , const  char *argv[])
{

     if(argc > 3){

         string s = string(argv[1]);
         string s1 = string(argv[2]);
         string s2 = string(argv[3]);
         findAndReplaceAll(s,s1,s2);

         cout << " "  <<  s <<" " <<endl ;
         return 1 ;

     }
  cout<<" args  wanted 3 "  <<endl ;
  return 0;

}