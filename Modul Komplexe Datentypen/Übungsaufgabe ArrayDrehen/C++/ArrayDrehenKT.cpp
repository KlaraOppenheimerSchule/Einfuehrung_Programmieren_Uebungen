// SchoolStuff.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <random>
#include <algorithm> 
#include <array>

int main()
{
	/*
		Create an array with the numbers from 0 to 9, then create 
		a second array and assign the contents of the first array 
		to it in reverse order. The following example is intended 
		to simulate this: 
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] → [9, 8, 7, 6, 5, 4, 3, 2, 1, 0].
	*/

	const std::vector<int> vecNumbers = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	std::vector<int> vecReversedNumbers = { };

	std::cout << "Not reversed array:\n";

	for (const int i : vecNumbers)
	{
		const bool bEndOfVec = (i == vecNumbers.size() - 1); 
		std::cout << i << (bEndOfVec ? "\n" : "\t");
	}

	std::cout << "Do you want to reverse the array? (y / n)\n";

	char szInput;
	std::cin >> szInput;

	if (szInput == 'y' || szInput == 'Y')
	{
		vecReversedNumbers = vecNumbers;
		std::reverse(std::begin(vecReversedNumbers), std::end(vecReversedNumbers));

		std::cout << "Reversed array:\n";
		for (const int i : vecReversedNumbers)
			std::cout << i << "\t";
	}

	return 0;
}