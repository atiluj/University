#include <iostream>
#include <vector>

using namespace std;

vector<int> tree[10201];

int dfs(int* visited, int* colors, int vertex){
    int result = 0;
    visited[vertex] = 1;

    for(int i=0; i<tree[vertex].size(); i++){//przechodzimy po każdym sąsiedzie
        if(!visited[tree[vertex][i]]){//tylko jeśli nie został on jeszcze odwiedzony to wykonujemy
            if(colors[tree[vertex][i]]==colors[vertex])
                result += dfs(visited, colors, tree[vertex][i]);
            else
                result += 1 + dfs(visited, colors, tree[vertex][i]);
        }
    }
    return result;
}



int main(){

    int n, x;
    cin>>n;

    int colors[n+1] = {0};

    for(int i=1; i<n; i++){
        cin>>x;
        tree[x].push_back(i+1);
    }

    for(int i=1; i<n+1; i++){
        cin>>colors[i];
    }

    int visited[n+1] = {0};
    cout<<dfs(visited, colors, 1)+1<<endl;

    return 0;
}