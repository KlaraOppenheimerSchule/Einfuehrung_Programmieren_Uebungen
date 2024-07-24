namespace Telefonarten.Batteries
{
    public class NickelCadmiumBattery : Battery
    {
        public NickelCadmiumBattery(int level) : base(level)
        {
            
        }

        public override bool Charge()
        {
            while (Level < 100)
            {
                Task.Delay(1000);
                Level++;
                if (Level == 100)
                {
                    return true;
                }
                else return false;
            }

            return true;
        }
    }
}
