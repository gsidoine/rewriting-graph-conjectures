#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){
 ifstream ff(argv[1]);int m,p;ff>>m>>p;vector<uint64_t> pm(p);for(auto&v:pm)ff>>v;
 ifstream gg(argv[2]);int n=20;vector<pair<int,int>> edges;int u,v;while(gg>>u>>v)edges.push_back({u,v});
 if((int)edges.size()!=m)throw runtime_error("edges");
 uint64_t counts=0;int found=0;int any0=0;map<int,long long> hist;
 for(int a=0;a<p;a++)for(int b=a;b<p;b++)for(int c=b;c<p;c++)for(int d=c;d<p;d++)for(int e=d;e<p;e++)for(int f=e;f<p;f++){
  int ids[6]={a,b,c,d,e,f};int mult[30]={};int q=0;
  for(int k=0;k<6;k++)for(int ed=0;ed<m;ed++)mult[ed]+=((pm[ids[k]]>>ed)&1);
  for(int j=0;j<m;j++)q+=(mult[j]-2)*(mult[j]-2);
  if(q!=6)continue;
  counts++;
  int minimum=6;
  for(int i=0;i<6;i++)for(int j=i+1;j<6;j++){
   int rem[30]={};bool feasible=true;
   for(int ed=0;ed<m;ed++){rem[ed]=2-mult[ed]+((pm[ids[i]]>>ed)&1)+((pm[ids[j]]>>ed)&1);if(rem[ed]<0)feasible=false;}
   if(!feasible)continue;
   vector<int> color(20,-1);bool bip=true;
   for(int root=0;root<20 && bip;root++)if(color[root]<0){
    color[root]=0;queue<int> Q;Q.push(root);
    while(!Q.empty()&&bip){int x=Q.front();Q.pop();for(int ed=0;ed<m;ed++){
      if(rem[ed]==0)continue;int y=-1;
      if(edges[ed].first==x)y=edges[ed].second;
      else if(edges[ed].second==x)y=edges[ed].first;
      if(y<0)continue;
      if(color[y]<0){color[y]=1-color[x];Q.push(y);}
      else if(color[y]==color[x]){bip=false;break;}
    }}
   }
   if(bip)minimum=2;
  }
  hist[minimum]++;
  if(minimum==6 && found<5){cout<<"Q6 no pair completion ids ";for(int x:ids)cout<<x<<" ";cout<<"\n";found++;}
 }
 cerr<<"Q6 total="<<counts<<" kappa2possible="<<hist[2]<<" no_kappa2="<<hist[6]<<"\n";
}
