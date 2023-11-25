#pragma once

class Plane {
	int m_nCode;
	int m_nFuel;
	bool m_bInAir;
	int m_nTimeToFinish;

public:
	Plane(int nCode, int nFuel = 50);
	~Plane();

	bool IsCrashed() const;
	bool IsFinished() const;
	void ProcessTick();
	void Print() const;

	void SetTimeToFinish(int time);
	int GetTimeToFinish() const;
};
