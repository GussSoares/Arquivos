#include <iostream>
#define TAM 10

using namespace std;

int main(int argc, char const *argv[])
{

    int matriz[TAM][TAM];

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            matriz[i][j]=0;
        }
    }
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d", matriz[i][j]);
        }
        printf("\n");
    }
    return 0;
}
