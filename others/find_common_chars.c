#include <stdio.h>

int table[30] = {0};

void index_it(char in, int ad) ;
void find(const char* a, int an, const char* b, int bn) {

    int i = 0;
    for (i = 0; i < an; i++)
        index_it(a[i], 1);

    for (i = 0; i < bn; i++)
        index_it(b[i], 2);

}

void index_it(char in, int ad) {
    if (in != ' ')
        if((table[in - 'a'] == 0 || table[in - 'a'] == 2 ) && ad == 1)
            table[in - 'a'] += ad;
        else {
            if(table[in - 'a'] == 1 && ad == 2)
                table[in - 'a'] += ad;
        }
        else {}
}

int main(void) {

    char* a = "helro hello kaka";
    char* b = "foobar hi";

    find(a, 16, b, 9);
    int i= 0;
    for (i = 0;i < 30; i++)
        if(table[i] == 3)
            printf("%c ", i+'a');
    return 0;
}
