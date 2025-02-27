#include <stdio.h>
#include "sandpiles.h"



void print_grid(int grid[3][3])
{
    int i, j;
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
}

void print_grid_sum(int grid1[3][3], int grid2[3][3])
{
    int i, j;
    int temp[3][3];

    /* Étape 1: Additionner grid2 à grid1 */
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            grid1[i][j] += grid2[i][j];

    /* Étape 2: Stabilisation */
    while (!is_stable(grid1))
    {
        printf("=\n");
        print_grid(grid1);

        /* Copie de la grille pour traitement */
        copy_grid(grid1, temp);

        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {
                if (temp[i][j] >= 4)
                {
                    grid1[i][j] -= 4;
                    if (i > 0) grid1[i - 1][j] += 1; /* Haut */
                    if (i < 2) grid1[i + 1][j] += 1; /* Bas */
                    if (j > 0) grid1[i][j - 1] += 1; /* Gauche */
                    if (j < 2) grid1[i][j + 1] += 1; /* Droite */
                }
            }
        }
    }
}
