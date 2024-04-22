#include <stdio.h>

#define MAX_VILLAGES 1400
#define INF 999999

double ary[MAX_VILLAGES][MAX_VILLAGES];
int completed[MAX_VILLAGES] = {0};
int n, num_villages;
int cost = 0;
int start_village_gts1 = 0;
int start_villages[MAX_VILLAGES];
int min_costs[MAX_VILLAGES];

void docfile_gts2(FILE *f, double ary[MAX_VILLAGES][MAX_VILLAGES], int &n, int start_villages[], int &num_villages);
int least_gts2(int c)
{
    int i, nc = INF;
    int min = INF, kmin, min_index = INF;

    for (i = 0; i < n; i++)
    {
        if ((ary[c][i] != 0) && (completed[i] == 0))
        {
            if (ary[c][i] < min || (ary[c][i] == min && i < min_index))
            {
                min = ary[c][i];
                kmin = ary[c][i];
                nc = i;
                min_index = i;
            }
        }
    }

    if (min != INF)
    {
        return nc;
    }

    return INF;
}


void mincost_GTS2(int city, int start_village_index)
{
    int i, ncity;

    completed[city] = 1;

    ncity = least_gts2(city);

    if (ncity == INF)
    {
        ncity = start_villages[start_village_index];
        min_costs[start_village_index] += ary[city][ncity];
        completed[city] = 0;
        return;
    }

    min_costs[start_village_index] += ary[city][ncity];
    mincost_GTS2(ncity, start_village_index);
}

int main()
{
    FILE *f;
    int i, j;

    int option;

    docfile_gts2(f, ary, n, start_villages, num_villages);

    for (i = 0; i < num_villages; i++)
    {
        for (j = 0; j < n; j++)
        {
            completed[j] = 0;
        }
        mincost_GTS2(start_villages[i], i);
    }

    for (i = 0; i < num_villages; i++)
    {
        printf("Chi phi nho nhat tai dinh %d la %d\n", start_villages[i] + 1, min_costs[i]);
    }
    int min = min_costs[0];
    // Tim phan tu nho nhat trong mang min_costs
    for (i = 1; i < num_villages; i++)
    {
        if (min_costs[i] < min)
        {
            min = min_costs[i];
        }
    }

    printf("\nHanh trinh tot nhat co chi phi la: %d\n", min);

    return 0;
}

void docfile_gts2(FILE *f, double ary[][MAX_VILLAGES], int &n, int start_villages[], int &num_villages)
{
    f = fopen("D:\\NewPython\\ant-colony-tsp\\data\\nrw1379_matrix.txt", "rt");
   
    // Đọc giá trị n từ dòng đầu tiên
    fscanf(f, "%d", &n);

    // Tạo danh sách các làng khởi đầu từ 1 đến n
    num_villages = n;
    for (int i = 0; i < num_villages; i++)
    {
        start_villages[i] = i;
    }

    // Đọc ma trận chi phí vào mảng ary
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            fscanf(f, "%lf", &ary[i][j]);
        }
    }

    fclose(f);
}
