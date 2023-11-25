#include "Plane.h"
#include <iostream>

Plane::Plane(int nCode, int nFuel) : m_nCode(nCode), m_nFuel(nFuel), m_bInAir(true), m_nTimeToFinish(-1) {}

Plane::~Plane() {}

bool Plane::IsCrashed() const {
	return m_bInAir && (m_nFuel <= 0);
}

bool Plane::IsFinished() const {
	return m_nTimeToFinish <= 0;
}

void Plane::ProcessTick() {
	if (m_bInAir) {
		m_nFuel--;
	}
	if (m_nTimeToFinish > 0) {
		m_nTimeToFinish--;
	}
}

void Plane::Print() const {
	std::cout << "#" << m_nCode << " (" << m_nFuel << ") " << (m_bInAir ? "In air" : "On ground");
	if (m_nTimeToFinish > 0) {
		std::cout << " Processing: " << m_nTimeToFinish << "m left";
	}
	std::cout << std::endl;
}

void Plane::SetTimeToFinish(int time) {
	m_nTimeToFinish = time;
}

int Plane::GetTimeToFinish() const {
	return m_nTimeToFinish;
}
