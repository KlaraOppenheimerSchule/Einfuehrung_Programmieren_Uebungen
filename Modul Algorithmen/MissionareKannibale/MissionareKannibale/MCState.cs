
namespace MissionareKannibale
{
    internal class MCState
    {
        public int _maxNummer = 3;
        public int _westM;
        public int _westC;
        public int _eastM;
        public int _eastC;
        public bool _boat;

        public MCState(int missionaries, int cannibals, bool boat)
        {
            _westM = missionaries;
            _westC = cannibals;
            _eastM = _maxNummer - missionaries;
            _eastC = _maxNummer - cannibals;
            _boat = boat;
        }

        private bool GoalTest()
        {
            if (_eastC == _maxNummer && _eastM == _maxNummer && IsLegal())
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        public bool IsLegal()
        {
            if ((_westM < _westC && _westM > 0) || (_eastM < _eastC && _eastM > 0))
            {
                return false;
            }
            else
            {
                return true;
            }
        }
    }
}

