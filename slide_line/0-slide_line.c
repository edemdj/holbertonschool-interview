#include "slide_line.h"

void slide_left(int *line, size_t size) {
    size_t i, j = 0;

    for (i = 0; i < size; i++) {
        if (line[i] != 0) {
            if (j < i) {
                line[j] = line[i];
                line[i] = 0;
            }
            j++;
        }
    }

    for (i = 0; i < size - 1; i++) {
        if (line[i] == line[i + 1] && line[i] != 0) {
            line[i] *= 2;
            line[i + 1] = 0;
        }
    }

    j = 0;
    for (i = 0; i < size; i++) {
        if (line[i] != 0) {
            if (j < i) {
                line[j] = line[i];
                line[i] = 0;
            }
            j++;
        }
    }
}

void slide_right(int *line, size_t size) {
    size_t i, j = size - 1;

    for (i = size; i > 0; i--) {
        if (line[i - 1] != 0) {
            if (j > i - 1) {
                line[j] = line[i - 1];
                line[i - 1] = 0;
            }
            j--;
        }
    }

    for (i = size; i > 1; i--) {
        if (line[i - 1] == line[i - 2] && line[i - 1] != 0) {
            line[i - 1] *= 2;
            line[i - 2] = 0;
        }
    }

    j = size - 1;
    for (i = size; i > 0; i--) {
        if (line[i - 1] != 0) {
            if (j > i - 1) {
                line[j] = line[i - 1];
                line[i - 1] = 0;
            }
            j--;
        }
    }
}

int slide_line(int *line, size_t size, int direction) {
    if (!line || size == 0 || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT))
        return 0;

    if (direction == SLIDE_LEFT)
        slide_left(line, size);
    else
        slide_right(line, size);

    return 1;
}
