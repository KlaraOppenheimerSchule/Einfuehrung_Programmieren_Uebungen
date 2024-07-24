namespace Telefonarten.Batteries
{
    public class NickelMetalHydrideBattery : Battery
    {
        public NickelMetalHydrideBattery(int level) : base(level)
        {

        }

        public override bool Charge()
        {
            while (Level < 100)
            {
                Task.Delay(500);
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
