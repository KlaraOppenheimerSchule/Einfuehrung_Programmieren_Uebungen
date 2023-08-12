class wm:
    wm = ["Brasilien", "Italien", "Deutschland", "Uruguay", "Argentinien", "England", "Frankreich", "Spanien"], ["1958,1962,1970,1994,2002", "1934,1938,1962,2006", "1954,1974,1990,2014", "1930,1950", "1978,1986", "1966", "1998", "2010"]

    def Ausgabe(self):
        for i in range(len(self.wm[1])):
            print(self.wm[0][i],self.wm[1][i])

wm = wm()
wm.Ausgabe()