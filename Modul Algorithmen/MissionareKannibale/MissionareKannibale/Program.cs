using MissionareKannibale;

MCState currentState = new MCState(3, 3, true);

void DisplaySolution(List<MCState> path)
{
	if (path.Count == 0)
	{
		return;
	}
	
	var oldState = path[0];
	Console.WriteLine(oldState);
	 // todo - Ausgabe formatierne? 

    for (int i = 1; i < path.Count; i++)
    {
		if (currentState._boat)
		{
			Console.WriteLine($"{oldState._eastM - currentState._eastM} Missionare und {oldState._eastC - currentState._eastC} Kannibalen vom Ostufer zum Westufer transportiert.");
		}
		else
		{
			Console.WriteLine($"{oldState._westM - currentState._westM} Missionare und {oldState._westC - currentState._westC} Kannibalen vom Westufer zum Ostufer transportiert.");
		}
		Console.WriteLine(currentState);
		oldState = currentState;
    }


List<MCState> Successors()
{
    List<MCState> successors = [];
	if (currentState._boat)
	{
		if (currentState._westM > 1)
		{
			successors.Add(new MCState(currentState._westM - 2,currentState._westC, !currentState._boat));
		}
		if (currentState._westM > 0)
		{
			successors.Add(new MCState(currentState._westM - 1, currentState._westC, !currentState._boat));
		}
		if (currentState._westC > 1)
		{
			successors.Add(new MCState(currentState._westM, currentState._westC - 2, !currentState._boat));
		}
		if (currentState._westC > 0)
		{
			successors.Add(new MCState(currentState._westM, currentState._westC - 1, !currentState._boat));
		}
		if (currentState._westC > 0 && currentState._westM > 0)
		{
			successors.Add(new MCState(currentState._westM - 1, currentState._westC - 1, !currentState._boat));
		}
	}
	else
	{
        if (currentState._eastM > 1)
        {
            successors.Add(new MCState(currentState._westM + 2, currentState._westC, !currentState._boat));
        }
        if (currentState._eastM > 0)
        {
            successors.Add(new MCState(currentState._westM + 1, currentState._westC, !currentState._boat));
        }
        if (currentState._eastC > 1)
        {
            successors.Add(new MCState(currentState._westM, currentState._westC + 2, !currentState._boat));
        }
        if (currentState._eastC > 0)
        {
            successors.Add(new MCState(currentState._westM, currentState._westC + 1, !currentState._boat));
        }
        if (currentState._eastC > 0 && currentState._eastM > 0)
        {
            successors.Add(new MCState(currentState._westM + 1, currentState._westC + 1, !currentState._boat));
        }
    }
    return successors.Where(x => x.IsLegal()).ToList();
}