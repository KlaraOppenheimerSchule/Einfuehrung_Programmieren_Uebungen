namespace Telefonarten.Telephones
{
    public abstract class Telephone
    {
        protected int Volume { get; set; }

        public Telephone(int volume)
        {
            Volume = volume;
        }
    }
}
