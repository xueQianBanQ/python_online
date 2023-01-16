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
//	//开辟一个空间
//	int* p = new int(10);
//	cout << *p << endl;
//	//返回开辟的空间
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
//	//引用必须初始化
//	//引用之后就不可以发生改变了
//	cout << a <<" "<< b << endl;
//	b = 100;
//	cout << a << " " << b << endl;
//	return 0;
//}


//#include <iostream>
//using namespace std;
////值传递
//void mySwap1(int a, int b)
//{
//	int temp = a;
//	a = b;
//	b = temp;
//}
////地址传递
//void mySwap2(int* a, int* b)
//{
//	int temp = *a;
//	*a = *b;
//	*b = temp;
//}
////引用传递
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

/////////////////////////////////引用做函数返回值

//1. 不能返回局部变量引用
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

//2. 可以返回静态变量引用 , 且可以作为左值
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

//////////////////////////////////////引用的实质(指针常量)
//#include <iostream>
//using namespace std;
//int main()
//{
//	int a = 10;
//	int& ref = a; ///   相当于系统帮你做了 int * const ref = &a      ref不可以修改地址， 但可以修改值
//	return 0;
//}


////////////常量引用
//#include <iostream>
//int main()
//{
//	const int& ref = 10;// 相当于系统给你做了  int temp = 10; const int& ref = tmep;
//	//ref = 20;不可以被修改
//	return 0;
//}


//////函数默认值
//#include <iostream>
//using namespace std;
////1.从第一个设置默认值的参数往后，都必须需要是默认值
//int Add(int a, int b, int c = 10)
//{
//	return a + b + c;
//}
////2. 声明和调用只能有一个设置默认值， 不然编译器不知道哪是一个是真的 
//int main()
//{
//	cout << Add(10, 10) << endl;
//	return 0;
//}



////函数重载
//#include <iostream>
//using namespace std;
////1.在同一个作用域下
////2.函数名相同
////3.参数不一样
////
//void func(int a)
//{
//	cout << "func(int a) 的调用" << endl;
//}
//void func()
//{
//	cout << "func 的调用" << endl;
//}
//int main()
//{
//	func(10);
//	return 0;
//}