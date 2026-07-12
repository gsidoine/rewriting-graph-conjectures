#include <bits/stdc++.h>
using namespace std;
long long C[50][10];
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 for(int n=0;n<50;n++){C[n][0]=1;for(int k=1;k<10;k++)C[n][k]=(n?C[n-1][k-1]+C[n-1][k]:0);}
 int m,p;cin>>m>>p;vector<uint64_t> pm(p);for(auto &x:pm)cin>>x;int N=p+5;int S=C[N][6];cerr<<"states "<<S<<"\n";
 vector<uint64_t> packed(S);vector<uint16_t> qval(S);vector<int> targets;
 auto rank_state=[&](array<int,6> s){long long r=0;for(int i=0;i<6;i++)r+=C[s[i]+i][i+1];return (int)r;};
 long long cnt=0;
 for(int a=0;a<p;a++)for(int b=a;b<p;b++)for(int c=b;c<p;c++)for(int d=c;d<p;d++)for(int e=d;e<p;e++)for(int f=e;f<p;f++){
   array<int,6>s={a,b,c,d,e,f};int r=rank_state(s);uint64_t pack=a|((uint64_t)b<<6)|((uint64_t)c<<12)|((uint64_t)d<<18)|((uint64_t)e<<24)|((uint64_t)f<<30);packed[r]=pack;
   uint8_t mult[64]={0};for(int x:s){uint64_t w=pm[x];while(w){int z=__builtin_ctzll(w);w&=w-1;mult[z]++;}}
   int Q=0;for(int z=0;z<m;z++){int dd=(int)mult[z]-2;Q+=dd*dd;}qval[r]=Q;if(Q==0)targets.push_back(r);cnt++;
 }
 cerr<<"enum "<<cnt<<" targets "<<targets.size()<<"\n";
 vector<uint8_t> seen(S);vector<int> que;que.reserve(S);for(int r:targets){seen[r]=1;que.push_back(r);} 
 auto decode=[&](uint64_t pack){array<int,6>s;for(int i=0;i<6;i++)s[i]=(pack>>(6*i))&63;return s;};
 for(size_t qi=0;qi<que.size();qi++){
   int cr=que[qi];auto s=decode(packed[cr]);int cv=qval[cr];
   for(int pos=0;pos<6;pos++){
     array<int,5> base;for(int i=0,j=0;i<6;i++)if(i!=pos)base[j++]=s[i];
     for(int x=0;x<p;x++){
       array<int,6> ns;int i=0,j=0;bool ins=false;while(i<6){if(!ins && (j==5 || x<=base[j])){ns[i++]=x;ins=true;}else ns[i++]=base[j++];}
       int nr=rank_state(ns);if(!seen[nr]&&qval[nr]>=cv){seen[nr]=1;que.push_back(nr);} 
     }
   }
 }
 int un=S-que.size();cout<<"reached "<<que.size()<<" unresolved "<<un<<"\n";map<int,int> hist;for(int i=0;i<S;i++)if(!seen[i])hist[qval[i]]++;for(auto [q,k]:hist)cout<<q<<' '<<k<<"\n";
}
