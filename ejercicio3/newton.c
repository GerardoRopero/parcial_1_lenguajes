#include <stdio.h>
#include <math.h>
#include "newton.h"

double sqrt_newton(double a) {

    if (a < 0) {
        printf("Error: raíz de número negativo\n");
        return -1;
    }

    double x = a;
    double tol = 1e-10;
    int max_iter = 100;

    for(int i = 0; i < max_iter; i++) {

        double x_new = x - (x*x - a)/(2*x);

        if (fabs(x_new - x) < tol)
            return x_new;

        x = x_new;
    }

    return x;
}
