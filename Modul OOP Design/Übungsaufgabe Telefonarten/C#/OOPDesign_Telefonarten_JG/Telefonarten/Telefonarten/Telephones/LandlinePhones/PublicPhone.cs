namespace Telefonarten.Telephones.LandlinePhones
{
    public class PublicPhone : StationaryLandlinePhone
    {
        private readonly int _costPerTime;

        public PublicPhone(int volume, string location, int costPerTime) : base(volume, location)
        {
            _costPerTime = costPerTime;
        }
    }
}
