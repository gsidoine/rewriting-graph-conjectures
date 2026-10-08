// Standalone C++17 finite verifier of the minimum weighted obstruction
// to direct three-coordinate exact repair (without an edge of multiplicity 6).
// Vertices of cubic graph locally partition six matching labels into three
// edge sets, possibly empty. Each left-side vertex contributes energy
// sum (|S|-2)^2 to global Q, and blocks triples I failing |I∩S|>=|S|-2.
// Enumerate 3^6 labeled partitions, deduplicate by blocking masks, then
// shortest-path DP over 2^20 masks. No external graph/solver library.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <limits>
#include <map>
#include <vector>
using namespace std;
constexpr int ALL=(1<<20)-1;
int main() {
  vector<int> triples;
  for(int i=0;i<64;i++) if (__builtin_popcount((unsigned)i)==3) triples.push_back(i);
  assert(triples.size()==20);
  map<int,int> minimum;
  for(int assign=0;assign<729;assign++){
    int x=assign,grp[3]={0,0,0};
    for(int color=0;color<6;color++){int k=x%3; x/=3; grp[k]|=1<<color;}
    int cost=0,blocking=0,maxmult=0;
    for(int k=0;k<3;k++){
      int m=__builtin_popcount((unsigned)grp[k]);
      cost+=(m-2)*(m-2);maxmult=max(maxmult,m);
    }
    if(maxmult==6) continue;
    for(int j=0;j<20;j++)for(int k=0;k<3;k++){
      int m=__builtin_popcount((unsigned)grp[k]);
      if(__builtin_popcount((unsigned)(triples[j]&grp[k]))<m-2) {
        blocking|=1<<j;break;
      }
    }
    if(!blocking)continue;
    if(!minimum.count(blocking) || minimum[blocking]>cost)minimum[blocking]=cost;
  }
  vector<pair<int,int>> types;
  for(auto [mask,cost]:minimum){assert(cost>0);types.push_back({mask,cost});}
  vector<short> dist(ALL+1,32767);
  dist[0]=0;
  // In a block-subset DP, adding a block always only adds set bits, hence
  // the mask strictly increases. Therefore numeric mask order is topological.
  for(int state=0;state<=ALL;state++){
    if(dist[state]==32767)continue;
    for(auto [mask,cost]:types){
      int y=state|mask;
      if(y!=state && dist[y]>dist[state]+cost)dist[y]=dist[state]+cost;
    }
  }
  cout<<"partition_patterns=122 deduplicated_blocking_types="<<types.size()<<"\n";
  cout<<"minimum_Q_for_triplet_blocker_without_m6="<<dist[ALL]<<"\n";
  assert(dist[ALL]==34);
  cout<<"PASS\n";
}
