
#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N, tarn, longjump;
	cin >> N >> tarn;

	std::vector<int> bakke;
	for (int i = 0; i < N; i++)
	{
		int a;
		cin >> a;
		bakke.push_back(a);
	}


	for (int _ = 0; _ < tarn; _++)
	{
		int x, y;
		cin >> x >> y;
		bool fin1 = false, fin2 = false;
		if (x == 0) {fin1 = true;}


		for (int i = 1; i < y+1; i++)
		{
			i = -i;
			if (!fin1)
			{
				if (x + i < 0 || bakke[(x + i)] > y + i)
				{
					// cout << "left end " << i << " " << x+i << " " << bakke[(x + i)] << endl;
					fin1 = true;
				}
			}
			i = -i;
			if (!fin2)
			{
				if (x + i >= N || bakke[x + i] > y - i)
				{
					// cout << "right end " << i << " " << x+i << " " << bakke[(x + i)] << endl;
					fin2 = true;
				}
			}
			if (fin1 && fin2)
			{
				longjump = i - 1;
				break;
			}
			longjump = i;
		}
			
		cout << longjump << endl;


	}
	// for (int i = 0; i < N; i++)
	// {
	// 	cout << bakke[i] << " ";
	// }

}
/*
10 2
3 1 1 2 3 4 2 2 1 1
1 5
4 5

10 2
1 1 1 2 3 6 2 2 1 0
3 5
4 6

12 2
1 1 1 2 3 4 2 2 1 0 0 0
3 5
4 6

*/
