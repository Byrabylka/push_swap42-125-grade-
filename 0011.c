#include <stdio.h>

int count(int k, int n)
{
    int s = 0;
    if (n < 0)
        return 0;
    if (n <= 1)
        return 1;
    for (int i = 1, i <= k, i++)
        s += count(k, n - i);
    return s;
}
    
int main()
{
    int k,n;
    scanf("%d %d", k, n);
    printf("%d", count(k, n));
}