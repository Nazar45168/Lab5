#include "PlanesControl.h"
#include <iostream>

int main() {
	PlanesControl dkp(10);
	dkp.Add(new Plane(12, 15));
	dkp.Add(new Plane(13, 25));
	dkp.Add(new Plane(14, 15));
	dkp.Print();

	for (int i = 0; i < 5; i++) {
		dkp.ProcessTick();
	}

	dkp.Print();
	return 0;
}
