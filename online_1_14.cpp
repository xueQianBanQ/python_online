#define _CRT_SECURE_NO_WARNINGS 1
//#include <iostream>
//using namespace std;
//int main()
//{
//	int a = 10;
//	int b = 10;
//	cout << &a << endl;
//	cout << (int)&b << endl;
//	return 0;
//}

//#include <iostream>
//using namespace std;
//int main()
//{
//	//����һ���ռ�
//	int* p = new int(10);
//	cout << *p << endl;
//	//���ؿ��ٵĿռ�
//	delete p;
//
//	return 0;
//}

//#include <iostream>
//using namespace std;
//int main()
//{
//	int* arr = new int[10];
//	int i = 0;
//	for (i = 0; i < 10; i++)
//	{
//		arr[i] = i + 1;
//	}
//	for (i = 0; i < 10; i++)
//	{
//		cout << *(arr + i) << endl;
//	}
//	delete[] arr;
//}

//#include <iostream>
//using namespace std;
//int main()
//{
//	int a = 10;
//	int& b = a;
//	//���ñ����ʼ��
//	//����֮��Ͳ����Է����ı���
//	cout << a <<" "<< b << endl;
//	b = 100;
//	cout << a << " " << b << endl;
//	return 0;
//}


//#include <iostream>
//using namespace std;
////ֵ����
//void mySwap1(int a, int b)
//{
//	int temp = a;
//	a = b;
//	b = temp;
//}
////��ַ����
//void mySwap2(int* a, int* b)
//{
//	int temp = *a;
//	*a = *b;
//	*b = temp;
//}
////���ô���
//void mySwap3(int& a, int& b)
//{
//	int temp = a;
//	a = b;
//	b = temp;
//}
//
//int main()
//{
//	int a = 10;
//	int b = 20;
//	mySwap1(a, b);
//	cout << "a = " << a << endl;
//	cout << "b = " << b << endl;
//	cout << endl;
//	mySwap2(&a, &b);
//	cout << "a = " << a << endl;
//	cout << "b = " << b << endl;
//	cout << endl;
//	mySwap3(a, b);
//	cout << "a = " << a << endl;
//	cout << "b = " << b << endl;
//	return 0;
//}

/////////////////////////////////��������������ֵ

//1. ���ܷ��ؾֲ���������
/*
#include <iostream>
using namespace std;
int& test1(void)
{
	int a = 10;
	return a;
}
int main()
{
	int& ref = test1();
	cout << "ref = " << ref << endl;
	return 0;
}
*/

//2. ���Է��ؾ�̬�������� , �ҿ�����Ϊ��ֵ
/*
#include <iostream>
using namespace std;
int& test2(void)
{
	static int a = 10;
	return a;
}
int main()
{
	int& ref = test2();
	cout << "ref = " << ref << endl;
	test2() = 1000;
	cout << "ref = " << ref << endl;
	return 0;
}
*/

//////////////////////////////////////���õ�ʵ��(ָ�볣��)
//#include <iostream>
//using namespace std;
//int main()
//{
//	int a = 10;
//	int& ref = a; ///   �൱��ϵͳ�������� int * const ref = &a      ref�������޸ĵ�ַ�� �������޸�ֵ
//	return 0;
//}


////////////��������
//#include <iostream>
//int main()
//{
//	const int& ref = 10;// �൱��ϵͳ��������  int temp = 10; const int& ref = tmep;
//	//ref = 20;�����Ա��޸�
//	return 0;
//}


//////����Ĭ��ֵ
//#include <iostream>
//using namespace std;
////1.�ӵ�һ������Ĭ��ֵ�Ĳ������󣬶�������Ҫ��Ĭ��ֵ
//int Add(int a, int b, int c = 10)
//{
//	return a + b + c;
//}
////2. �����͵���ֻ����һ������Ĭ��ֵ�� ��Ȼ��������֪������һ������� 
//int main()
//{
//	cout << Add(10, 10) << endl;
//	return 0;
//}



////��������
//#include <iostream>
//using namespace std;
////1.��ͬһ����������
////2.��������ͬ
////3.������һ��
////
//void func(int a)
//{
//	cout << "func(int a) �ĵ���" << endl;
//}
//void func()
//{
//	cout << "func �ĵ���" << endl;
//}
//int main()
//{
//	func(10);
//	return 0;
//}