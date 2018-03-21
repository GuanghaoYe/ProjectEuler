//This sourcecode is under GPLv3
//yeguanghao
#include <bits/stdc++.h>
#define rep(name,start,end,step) for(int name=start;name<=end;name+=step)
using namespace std;
#define Pn(x) printf("%d\n",x)
#define Ps(x) printf("%d ",x)
#ifdef _WIN32
#define Pln(x) printf("%I64d\n",x)
#define Pls(x) printf("%I6d ",x)
#else
#define Pln(x) printf("%lld\n",x)
#define Pls(x) printf("%lld ",x)
#endif
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define PROB
inline void R(int &x) {
	x=0; int f=1; char ch=getchar();
	while(ch<'0'||ch>'9') {if(ch=='-')f=-1; ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
	x*=f;
}

void Redirect() {
#ifndef DEBUG
	freopen(PROB".in","r",stdin);
	freopen(PROB".out","w",stdout);
#endif
}

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
int a[2005][2005];
const int n = 1001;
int cnt = 0;
int main() {
	int layers = (n+1) / 2;
	pii pos = mp(layers,layers);
	a[pos.fi][pos.se] = ++cnt;
	for(int i=2;i<=layers;++i) {
		pos.se+=1;
		a[pos.fi][pos.se] = ++cnt;
		while(pos.fi+1<layers+i) {
			pos.fi+=1;
			a[pos.fi][pos.se] = ++cnt;
		}
		while(pos.se-1>layers-i) {
			pos.se-=1;
			a[pos.fi][pos.se] = ++cnt;
		}
		while(pos.fi-1>layers-i) {
			pos.fi-=1;
			a[pos.fi][pos.se] = ++cnt;
		}
		while(pos.se+1<layers+i) {
			pos.se+=1;
			a[pos.fi][pos.se] = ++cnt;
		}
	}
	ll ans = 0;
	for(int i=1;i<=n;++i) {
		ans+=a[i][i];
	}
	for(int i=1;i<=n;++i) {
		ans+=a[i][n+1-i];
	}
	cout<<ans-1<<endl;
}


