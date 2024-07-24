namespace Telefonarten.Batteries
{
    public class LithiumIonBattery : Battery
    {
        public LithiumIonBattery(int level) : base(level)
        {
            
        }

        public override bool Charge()
        {
            while (Level < 100)
            {
                Task.Delay(100);
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
