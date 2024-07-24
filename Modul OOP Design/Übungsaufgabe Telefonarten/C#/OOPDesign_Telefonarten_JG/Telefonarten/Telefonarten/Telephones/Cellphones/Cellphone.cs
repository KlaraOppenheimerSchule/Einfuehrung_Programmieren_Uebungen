using Telefonarten.Batteries;

namespace Telefonarten.Telephones.Cellphones
{
    public abstract class Cellphone : Telephone
    {
        protected int Keys { get; set; }

        public Battery Battery { get; set; }

        public Cellphone(int volume, int keys, Battery battery) : base(volume)
        {
            Keys = keys;
            Battery = battery;
        }
    }
}
