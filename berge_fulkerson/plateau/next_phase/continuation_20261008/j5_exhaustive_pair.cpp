#include <bits/stdc++.h>
using namespace std;
int main(int argc, char**argv){
  ifstream fi(argv[1]);int m,p;fi>>m>>p;vector<uint64_t>M(p);for(auto &x:M)fi>>x;
  vector<array<unsigned char,64>> P;
  for(int a=0;a<p;a++)for(int b=a;b<p;b++){
    array<unsigned char,64> c{};
    for(int j=0;j<m;j++)c[j]=((M[a]>>j)&1)+((M[b]>>j)&1);
    P.push_back(c);
  }
  vector<int> cache(p*p*p*p,-1);
  auto idx=[&](int a,int b,int c,int d){return ((a*p+b)*p+c)*p+d;};
  long long four=0;const auto init=chrono::steady_clock::now();
  for(int a=0;a<p;a++)for(int b=a;b<p;b++)for(int c=b;c<p;c++)for(int d=c;d<p;d++){
    int C[64]={};for(auto x:{a,b,c,d}){
        for(int j=0;j<m;j++) C[j]+=((M[x]>>j)&1);
    }
    int best=1e9;
    for(auto &v:P){int q=0;for(int j=0;j<m;j++){int t=C[j]+v[j]-2;q+=t*t;}best=min(best,q);}
    cache[idx(a,b,c,d)]=best;four++;
  }
  cerr<<"cached_four="<<four<<" elapsed_s="<<chrono::duration<double>(chrono::steady_clock::now()-init).count()<<"\n";
  long long tot=0,traps=0,q0=0;map<int,long long>trapshist;vector<int>first;
  for(int a=0;a<p;a++)for(int b=a;b<p;b++)for(int c=b;c<p;c++)for(int d=c;d<p;d++)for(int e=d;e<p;e++)for(int f=e;f<p;f++){
    int T[6]={a,b,c,d,e,f};
    int q=0;for(int j=0;j<m;j++){
        int v=-2;for(int i=0;i<6;i++)v+=(M[T[i]]>>j)&1;q+=v*v;
    }
    tot++;if(!q){q0++;continue;}
    int best=INT_MAX;
    for(int i=0;i<6;i++)for(int j=i+1;j<6;j++){
        int F[4],k=0;for(int z=0;z<6;z++)if(z!=i && z!=j)F[k++]=T[z];
        best=min(best,cache[idx(F[0],F[1],F[2],F[3])]);
    }
    if(best>=q){traps++;trapshist[q]++;if(first.empty())first.assign(T,T+6);}
  }
  cout<<"pms="<<p<<" states="<<tot<<" exact_covers="<<q0<<" positive_pair_traps="<<traps<<"\n";
  for(auto [q,n]:trapshist)cout<<"q="<<q<<" traps="<<n<<"\n";
  if(first.size()){cout<<"first_trap=";for(int x:first)cout<<x<<",";cout<<"\n";}
  cout<<"elapsed_s="<<chrono::duration<double>(chrono::steady_clock::now()-init).count()<<"\n";
}
