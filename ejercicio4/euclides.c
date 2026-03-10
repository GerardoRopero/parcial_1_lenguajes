#include <stdio.h>
#include <time.h>

int mcd(int a, int b) {
    if (b == 0)
        return a;
    return mcd(b, a % b);
}

int main() {
    int a = 123456789, b = 987654321;
    int resultado;

    clock_t inicio = clock();

    for (int i = 0; i < 10000000; i++) {
        resultado = mcd(a, b);
    }

    clock_t fin = clock();

    double tiempo = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("MCD: %d\n", resultado);
    printf("Tiempo: %f segundos\n", tiempo);

    return 0;
}
