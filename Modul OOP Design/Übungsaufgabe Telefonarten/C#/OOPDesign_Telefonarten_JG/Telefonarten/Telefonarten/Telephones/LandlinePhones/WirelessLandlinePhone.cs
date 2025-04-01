using Telefonarten.Batteries;

namespace Telefonarten.Telephones.LandlinePhones
{
    public class WirelessLandlinePhone : LandlinePhone
    {
        protected int Range { get; set; }

        public Battery Battery { get; set; }

        public WirelessLandlinePhone(int volume, string location, int range, Battery battery) : base(volume, location)
        {
            Range = range;
            Battery = battery;
        }
    }
}
