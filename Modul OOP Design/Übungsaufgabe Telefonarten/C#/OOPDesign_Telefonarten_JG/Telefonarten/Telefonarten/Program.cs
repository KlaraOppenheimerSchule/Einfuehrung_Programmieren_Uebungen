using Telefonarten.Batteries;
using Telefonarten.Telephones.Cellphones;
using Telefonarten.Telephones.LandlinePhones;

var cell1 = new CellphoneWithoutTouchscreen(volume: 0, keys: 42, battery: new NickelCadmiumBattery(level: 52));
var cell2 = new CellphoneWithTouchscreen(volume: 66, keys: 42, battery: new LithiumIonBattery(level: 52), diagonal: 41.5);
var landline1 = new StationaryLandlinePhone(volume: 52, location: "Wuerzburg");
var landline2 = new WirelessLandlinePhone(volume: 32, location: "Heustreu", range: 100, battery: new NickelMetalHydrideBattery(level: 52));
var publicPhone = new PublicPhone(volume: 11, location: "Mainwiese Wuerzburg", costPerTime: 10);


while (cell1.Battery.GetLevel() != 100 || cell2.Battery.GetLevel() != 100 || landline2.Battery.GetLevel() != 100)
{
    cell1.Battery.Charge();
    var levelCell1 = cell1.Battery.GetLevel();
    Console.WriteLine(levelCell1);
    cell2.Battery.Charge();
    var levelCell2 = cell2.Battery.GetLevel();
    Console.WriteLine(levelCell2);
    landline2.Battery.Charge();
    var levelLandline2 = landline2.Battery.GetLevel();
    Console.WriteLine(levelLandline2);
    await Task.Delay(1000);
}