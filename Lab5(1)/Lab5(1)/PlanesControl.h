#pragma once
#include "Plane.h"
#include <list>

class PlanesControl {
	int m_nTimeForProcessing;
	std::list<Plane*> m_Planes;
	Plane* m_pProcessingPlane;

public:
	PlanesControl(int nTimeForProcessing = 10);
	virtual ~PlanesControl();

	Plane* PopReadyPlane();
	virtual void Add(Plane* p);
	virtual int ProcessTick();
	virtual void Print();
};
