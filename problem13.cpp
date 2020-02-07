#include <cmath>
#include <cstdio>
#include <string.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {

    string n;

    /* This this fucked up a lot of times
    So basically when you do string in c++ to string in c using c_str()
    it adds a null terminator to the end of the string so now you have 1
    extra character at eh end of your string. So you need to cater for that
    in any lengths you use, otherwise you'll miss out on the null terminator and
    probably get a buffer overflow. Hence the 51.
    */
    char * num = new char[51];
    int sum[100]={0};
    int t=0;
    int carry=0;
    int temp=0;
    int num_ele;
    cin >> t;
    while(t-->0){
        cin >> n;
        reverse(n.begin(),n.end());
        strcpy(num, n.c_str());
        carry=0;
        for(int i=0; i<50; i++)
        {
          num_ele = num[i]-'0';
          temp=sum[i]+num_ele+carry;
          if(temp>=10){
            carry=1;
            temp=temp%10;
          }else{
            carry=0;
          }
          sum[i]=temp;
          // std::cout << sum[i] <<" "<< num_ele << '\n';
        }
        if(carry==1){
          int j=50;
          while(sum[j]!=0 || carry!=0){
            temp=sum[j]+carry;
            if(temp>10){
              carry=1;
              temp=temp-10;
            }else{
              carry=0;
            }
            sum[j]=temp;
            j+=1;
          }
        }
    }
    string ans="";
    int check=0;
    for(int x = 99; x>=0; x--){
      if(sum[x]!=0){
        for(int k=0; k<10; k++){
          ans+=to_string(sum[x-k]);
        }
        break;
      }
    }
    std::cout << ans << '\n';
    return 0;
}
