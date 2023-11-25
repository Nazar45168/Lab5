#include "PlanesControl.h"
#include <iostream>

PlanesControl::PlanesControl(int nTimeForProcessing) : m_nTimeForProcessing(nTimeForProcessing), m_pProcessingPlane(nullptr) {}

PlanesControl::~PlanesControl() {
	if (m_pProcessingPlane) {
		delete m_pProcessingPlane;
	}
	for (Plane* p : m_Planes) {
		delete p;
	}
}

Plane* PlanesControl::PopReadyPlane() {
	if (m_pProcessingPlane && m_pProcessingPlane->IsFinished()) {
		Plane* tmpPlane = m_pProcessingPlane;
		m_pProcessingPlane = nullptr;
		return tmpPlane;
	}
	return nullptr;
}

void PlanesControl::Add(Plane* p) {
	m_Planes.push_back(p);
}

int PlanesControl::ProcessTick() {
	if (!m_pProcessingPlane && !m_Planes.empty()) {
		m_pProcessingPlane = m_Planes.front();
		m_Planes.pop_front();
		m_pProcessingPlane->SetTimeToFinish(m_nTimeForProcessing);
	}

	if (m_pProcessingPlane) {
		m_pProcessingPlane->ProcessTick();
	}

	for (Plane* p : m_Planes) {
		p->ProcessTick();
	}

	return 0; // можна повертати статус або інше значення, якщо потрібно
}

void PlanesControl::Print() {
	if (m_pProcessingPlane) {
		m_pProcessingPlane->Print();
	}
	for (Plane* p : m_Planes) {
		p->Print();
	}
}
