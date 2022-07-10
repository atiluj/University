#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>

using namespace std;

int n, m;

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
    cin >> n >> m;
    
    uf_init();
    int group_size, first, next, result;

    for(int i = 0; i < m; i++){
        cin>>group_size;

        if(group_size == 1) cin>>first;
        if(group_size <= 1) continue;

        cin>>first;
        for (int j = 1; j < group_size; j++) {
            cin>>next;

            int g1 = uf_find(first);
            int g2 = uf_find(next);
            if (g1 != g2) uf_union(g1, g2);
        }
    } 
        
    for(int i = 1; i < n+1; i++){
        result = uf_size[uf_find(i)];
        cout<<result<<" ";
    }
    cout<<endl;

  return 0;
}