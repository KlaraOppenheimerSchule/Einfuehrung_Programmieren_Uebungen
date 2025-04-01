using Telefonarten.Batteries;

namespace Telefonarten.Telephones.Cellphones
{
    public class CellphoneWithoutTouchscreen : Cellphone
    {
        public CellphoneWithoutTouchscreen(int volume, int keys, Battery battery) : base(volume, keys, battery)
        {
        }
    }
}
