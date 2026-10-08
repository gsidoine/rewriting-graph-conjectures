#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int T; if(!(cin>>T)) return 1; for(int tc=0;tc<T;tc++){int steps,seed,n,m;cin>>steps>>seed>>n>>m;vector<uint32_t> adj(n);for(int i=0,u,v;i<m;i++){cin>>u>>v;adj[u]|=1u<<v;adj[v]|=1u<<u;}
 uint32_t N=1u<<n,full=N-1;vector<uint8_t> comp(N),ec(N);for(uint32_t mask=1;mask<N;mask++){int v=__builtin_ctz(mask);uint32_t rest=mask&(mask-1);ec[mask]=ec[rest]+__builtin_popcount(adj[v]&rest);uint32_t rem=mask;int c=0;while(rem){c++;uint32_t fr=rem&-rem;rem^=fr;while(fr){uint32_t nb=0,w=fr;while(w){int x=__builtin_ctz(w);w&=w-1;nb|=adj[x];}uint32_t nx=nb&rem;rem^=nx;fr=nx;}}comp[mask]=c;}
 auto side=[&](uint32_t mask){if(!mask)return n+1;int v=__builtin_popcount(mask),c=comp[mask],e=ec[mask];return (c-1)+(e-v+c);};vector<int16_t> val(N);vector<uint32_t> targets;for(uint32_t mask=0;mask<N;mask++){val[mask]=side(mask)+side(full^mask);if(val[mask]==0)targets.push_back(mask);}vector<uint32_t> patches;for(int u=0;u<n;u++)patches.push_back(1u<<u);for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(adj[u]&(1u<<v))patches.push_back((1u<<u)|(1u<<v));
 vector<uint8_t> seen(N);vector<uint32_t> q;q.reserve(N);for(auto x:targets)if(!seen[x])seen[x]=1,q.push_back(x);for(size_t qi=0;qi<q.size();qi++){auto cur=q[qi];int cv=val[cur];for(auto p:patches){auto pre=cur^p;if(!seen[pre]&&val[pre]>=cv){seen[pre]=1;q.push_back(pre);}}}
 for(uint32_t mask=0;mask<N;mask++)if(!seen[mask])cout<<mask<<' '<<val[mask]<<'\n';
 }}
