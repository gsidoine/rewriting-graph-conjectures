#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;using LL=uint64_t;
struct Tree{U bits; array<U,6> cuts;};
int par[7];int root(int i){while(par[i]!=i){par[i]=par[par[i]];i=par[i];}return i;}
bool unite(int a,int b){a=root(a);b=root(b);if(a==b)return false;par[a]=b;return true;}
int main(int argc,char**argv){
 vector<pair<int,int>> edges;int id[7][7];memset(id,-1,sizeof id);
 for(int a=0;a<7;a++)for(int b=a+1;b<7;b++){id[a][b]=id[b][a]=edges.size();edges.emplace_back(a,b);}
 vector<Tree> trees;trees.reserve(16807);
 for(int z=0;z<16807;z++){
  int code=z,pr[5],deg[7]={1,1,1,1,1,1,1};
  for(int i=0;i<5;i++){pr[i]=code%7;code/=7;deg[pr[i]]++;}
  U bits=0;
  for(int i=0;i<5;i++){
   int leaf=0;while(deg[leaf]!=1)leaf++;
   bits|=U(1)<<id[leaf][pr[i]];deg[leaf]--;deg[pr[i]]--;
  }
  int a=-1,b=-1;for(int i=0;i<7;i++)if(deg[i]==1){if(a<0)a=i;else b=i;}
  bits|=U(1)<<id[a][b];
  Tree t; t.bits=bits;int q=0;
  for(int j=0;j<21;j++)if(bits&(U(1)<<j)){
   int comp[7];for(int k=0;k<7;k++)comp[k]=k;
   for(int k=0;k<21;k++)if(k!=j && (bits&(U(1)<<k))){int x=edges[k].first,y=edges[k].second;int xx=x;while(comp[xx]!=xx)xx=comp[xx];int yy=y;while(comp[yy]!=yy)yy=comp[yy];if(xx!=yy)comp[xx]=yy;}
   auto rt=[&](int x){while(comp[x]!=x)x=comp[x];return x;};
   U cut=0;for(int k=0;k<21;k++)if(rt(edges[k].first)!=rt(edges[k].second))cut|=U(1)<<k;
   t.cuts[q++]=cut;
  }
  if(q!=6){cerr<<"tree wrong";return 2;}
  trees.push_back(t);
 }
 static LL SAT[2][512][8];
 for(int mode=0;mode<2;mode++)for(int m=0;m<512;m++)for(int x=0;x<512;x++){
  bool yes=mode==0? ((x&m)!=0):((x&m)!=m);
  if(yes)SAT[mode][m][x/64]|=LL(1)<<(x%64);
 }
 U ALL=(U(1)<<21)-1;long long disj=0,connected=0,unsat=0; long long idx=0;
 for(auto &t:trees){
  for(auto &s:trees){
   if(t.bits&s.bits)continue;
   disj++;
   U residual=ALL^(t.bits|s.bits);
   for(int i=0;i<7;i++)par[i]=i;
   for(int j=0;j<21;j++)if(residual&(U(1)<<j))unite(edges[j].first,edges[j].second);
   bool ok=true;for(int i=1;i<7;i++)if(root(i)!=root(0)){ok=false;break;}
   if(!ok)continue;
   connected++;
   int rid[9];int w=0;for(int j=0;j<21;j++)if(residual&(U(1)<<j))rid[w++]=j;
   if(w!=9){cerr<<"R wrong";return 4;}
   LL valid[8];for(int a=0;a<8;a++)valid[a]=~LL(0);
   auto apply=[&](const Tree &tree,int mode){
    for(U cut:tree.cuts){
     int cl=0;
     for(int k=0;k<9;k++)if(cut&(U(1)<<rid[k]))cl|=1<<k;
     for(int a=0;a<8;a++)valid[a]&=SAT[mode][cl][a];
    }
   };
   apply(t,0);apply(s,1);
   bool sat=false;for(int a=0;a<8;a++)if(valid[a]){sat=true;break;}
   if(!sat){
    unsat++;cout<<"UNSAT 3-tree K7: T1="<<t.bits<<" T2="<<s.bits<<" R="<<residual<<"\n";cout.flush();
    if(argc<2)return 0;
   }
  }
  idx++;
  if(idx%4000==0)cerr<<"progress "<<idx<<"/"<<trees.size()<<" pair "<<disj<<" connected "<<connected<<" unsat "<<unsat<<"\n";
 }
 cout<<"FINAL trees="<<trees.size()<<" disjoint_pairs="<<disj<<" three_tree_packings="<<connected<<" unsatisfiable="<<unsat<<"\n";
}
