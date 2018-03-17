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
int d[10050];
int getd(int k) {
	int cnt=0;
	for(int i=1;i*i<=k;++i) {
		if(k%i==0) {
			cnt+=i;
			cnt+= k/i;
		}
	}
	return cnt-k;
}
int main() {
	rep(i,1,9999,1) {
		getd(i);
	}
	long long ans=0;
	rep(i,1,9999,1) {
		int a=d[i];
		int b=i;
		if(a>=10000||b>=10000) continue;
		if(d[a]==d[b]) {
			ans+=a;
			ans+=b;
		}
	}
	cout<<ans<<endl;
}


