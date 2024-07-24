namespace Telefonarten.Telephones.LandlinePhones
{
    public abstract class LandlinePhone : Telephone
    {
        protected string Location { get; set; }

        public LandlinePhone(int volume, string location) : base(volume)
        {
            Location = location;
        }
    }
}