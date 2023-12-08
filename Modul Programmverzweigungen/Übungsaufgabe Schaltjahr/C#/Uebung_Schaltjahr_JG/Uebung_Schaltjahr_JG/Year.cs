namespace Uebung_Schaltjahr_JG
{
    public class Year
    {
        public int? InputYear { get; set; }
        public string? InputYearString { get; set; }
        public bool? IsLeapYear { get; set; }
        public string? Output { get; set; }

        public Year(string? inputYearString)
        {
            switch (CheckInput(inputYearString))
            {
                case null:
                    Output = "Please enter a valid Year.";
                    break;
                default:
                    InputYearString = inputYearString;
                    break;
            }

            InputYear = ConvertString();
            IsLeapYear = CheckLeapYear();
        }

        private string? CheckInput(string? inputYearString)
        {
            if (string.IsNullOrEmpty(inputYearString))
            {
                return null;
            }
            return inputYearString;
        }

        private bool CheckLeapYear()
        {
            if (Output == null)
            {
                if (InputYear % 4 == 0 && InputYear % 100 != 0 || InputYear % 400 == 0)
                {
                    Output = $"The year {InputYear} is a leap year.";
                    return true;
                }
                Output = $"The year {InputYear} is not a leap year.";
                return false;
            }
            return false;
        }

        private int? ConvertString()
        {
            switch (int.TryParse(InputYearString, out int inputYear))
            {
                case true:
                    return inputYear;
                case false:
                    Output = "Please enter a valid Year.";
                    return null;
            }
        }
    }
}
