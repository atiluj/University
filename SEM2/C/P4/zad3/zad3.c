#include <stdlib.h> 
#include <stdio.h>
#include <stdbool.h>
int main(){
    int n, x;
    char znak, cos;

    scanf("%d", &n);
    int ** tab = (int **)malloc(n * sizeof(int *));
    scanf("%c", &cos);

    for(int i = 0; i < n; i++)
    {
        scanf(" %d", &x);
        tab[i] = (int *)malloc((x+1) * sizeof(int));
        tab[i][0] = x;

        for(int j = 1; j < tab[i][0] + 1; j++){
            scanf(" %d", &x);
            tab[i][j] = x;
        }
    }

    scanf(" %c", &znak);

    while(znak != 'k'){

        switch(znak){
        case 'z':{
            int i, j;
            scanf("%d ", &i);
            scanf(" %d", &j);

            int * pom;
            pom = tab[i];
            tab[i] = tab[j];
            tab[j] = pom;

            break;
        }

        case 'o':{
            int i;
            scanf(" %d", &i);

            int o = tab[i][0];
            int * pom = (int *)malloc((o+1) * sizeof(int));
            pom[0]= tab[i][0];

            for(int k = 1; k < tab[i][0] + 1; k++){
                pom[k] = tab[i][o];
                o--;
            }

            for(int k = 0; k < pom[0] + 1; k++)
                tab[i][k] = pom[k];

            free(pom);
            break;
        }

        case 'p':
        {
            int i, k, l, pom;
            scanf(" %d ", &i);
            scanf(" %d ", &k);
            scanf(" %d", &l);

            pom = tab[i][k+1];
            tab[i][k+1] = tab[i][l+1];
            tab[i][l+1] = pom;
            break;
        }
        default:
                break;
        }
        scanf(" %c", &znak);
    }

    for(int i = 0; i < n; i++){
        for(int j = 1; j < tab[i][0] + 1; j++){
            printf("%d ", tab[i][j]);
        }
        printf("\n");
    }

    free(tab);
    return 0;
}
