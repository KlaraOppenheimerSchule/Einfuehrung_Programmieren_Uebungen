"""Unittest Modules for Classes"""
import unittest
import telefonklassen
import akkuklassen

class TestTelefonClasses(unittest.TestCase):
    """Unittest Class to test Telefon Classes"""

    def test_stationar(self):
        """Test for Class Stationar"""
        x = telefonklassen.Stationar(1, "Wohnzimmer")
        self.assertEqual(x.get_lautstarke(), 1)
        self.assertEqual(x.get_standort(), "Wohnzimmer")

    def test_offentlich(self):
        """Test for Class Offentlich"""
        x = telefonklassen.Offentlich(1, "Wohnzimmer", 20)
        self.assertEqual(x.get_lautstarke(), 1)
        self.assertEqual(x.get_standort(), "Wohnzimmer")
        self.assertEqual(x.get_preis(), 20)

    def test_nonstationar(self):
        """Test for Class nonstationar"""
        y = akkuklassen.LithiumIon(40)
        x = telefonklassen.NonStationar(1, "Wohnzimmer", 10, y)
        self.assertEqual(x.get_lautstarke(), 1)
        self.assertEqual(x.get_standort(), "Wohnzimmer")
        self.assertEqual(x.get_reichweite(), 10)
        self.assertEqual(x.get_akku(), y)

    def test_mobil(self):
        """Test for Class nonstationar"""
        y = akkuklassen.LithiumIon(40)
        x = telefonklassen.Mobil(1, 12, y)
        self.assertEqual(x.get_lautstarke(), 1)
        self.assertEqual(x.get_anzahl_tasten(), 12)
        self.assertEqual(x.get_akku(), y)

    def test_smartphone(self):
        """Test for Class nonstationar"""
        y = akkuklassen.LithiumIon(40)
        x = telefonklassen.Smartphone(1, 12, y, 6.5)
        self.assertEqual(x.get_lautstarke(), 1)
        self.assertEqual(x.get_anzahl_tasten(), 12)
        self.assertEqual(x.get_akku(), y)
        self.assertEqual(x.get_diagonale(), 6.5)

class TestAkkuClasses(unittest.TestCase):
    """Unittest Class to test akku Classes"""
    def test_lithiumion(self):
        """Test for Class LithiumIon"""
        y = akkuklassen.LithiumIon(40)
        self.assertEqual(y.get_ladestand(), 40)
        self.assertTrue(y.aufladen())

    def test_nickelmetallhydrid(self):
        """Test for Class NickelMetallhydrid"""
        y = akkuklassen.LithiumIon(40)
        self.assertEqual(y.get_ladestand(), 40)
        self.assertTrue(y.aufladen())

    def test_nickelkadium(self):
        """Test for Class NickelKadium"""
        y = akkuklassen.LithiumIon(40)
        self.assertEqual(y.get_ladestand(), 40)
        self.assertTrue(y.aufladen())

if __name__ == '__main__':
    unittest.main()
