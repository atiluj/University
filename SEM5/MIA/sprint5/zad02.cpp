#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

int n, days, colors;
int f[200001];

// UnionFind
vector<int> uf_father;
vector<int> uf_size;

void uf_init() {
  uf_father = vector<int>(n + 1, -1);
  uf_size = vector<int>(n + 1, 1);
}

int uf_find(int x) {
  int root = x;
  while (uf_father[root] != -1) {
    root = uf_father[root];
  }

  while (x != root) {
    int f = uf_father[x];
    uf_father[x] = root;
    x = f;
  }

  return root;
}

void uf_union(int s1, int s2) {
  if (uf_size[s1] > uf_size[s2]) swap(s1, s2);
  uf_size[s2] += uf_size[s1];
  uf_father[s1] = s2;
}

int main() {
    cin >> n >> days >> colors;

    int p1, p2;

    for(int i = 0; i < n; i++){
        cin>>f[i];
    }

    for(int i = 0; i < days; i++){
        cin>>p1>>p2;
        uf_union(p1, p2);
    }

    uf_init();



  return 0;
}