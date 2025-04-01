using Telefonarten.Batteries;

namespace Telefonarten.Telephones.Cellphones
{
    public class CellphoneWithTouchscreen : Cellphone
    {
        private readonly double _diagonal;

        public CellphoneWithTouchscreen(int volume, int keys, Battery battery, double diagonal) : base(volume, keys, battery)
        {
            _diagonal = diagonal;
        }
    }
}
