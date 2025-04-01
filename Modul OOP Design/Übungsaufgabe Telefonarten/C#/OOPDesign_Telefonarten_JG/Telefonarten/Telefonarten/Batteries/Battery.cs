namespace Telefonarten.Batteries
{
    public abstract class Battery
    {
        public int Level { get; set; }

        public Battery(int level)
        {
            Level = level;
        }

        public int GetLevel()
        {
            return Level;
        }

        public abstract bool Charge();

    }
}
