class Station {
    protected stationsID: number;

    constructor(stationsID: number) {
        this.stationsID = stationsID;
    }
}

class Wetterstation extends Station {
    private messstation: Messstation;
    private stationData: {
        previousTemp: number[];
        previousMoist: number[];
        previousPress: number[];
    };
    private data: {
        temp: number,
        airmoist: number,
        airpress: number
    };

    constructor(stationsID: number) {
        super(stationsID);
        this.messstation = new Messstation();
        this.data = { temp: 0, airmoist: 0, airpress: 0 };
        this.stationData = {
            previousTemp: [],
            previousMoist: [],
            previousPress: []
        };
    }

    run(): void {
        let sensorData = this.messstation.run();

        this.data.temp = sensorData.temp;
        this.data.airmoist = sensorData.airmoist;
        this.data.airpress = sensorData.airpress;

        this.stationData.previousTemp.push(this.data.temp);
        this.stationData.previousMoist.push(this.data.airmoist);
        this.stationData.previousPress.push(this.data.airpress);
    }

    showData(): void {
        console.log(`
            Stations ID: ${this.stationsID},
            Current temperature is: ${this.data.temp}, current air moisture is: ${this.data.airmoist}, current air pressure is: ${this.data.airpress}
            previous data: temp:${this.stationData.previousTemp}, moist: ${this.stationData.previousMoist}, pressure: ${this.stationData.previousPress}
            `);
    }
}

class Messstation {
    private microcontroller: Microcontoller;
    private display: Display;

    constructor() {
        const sensor = new Sensor();
        this.display = new Display();
        this.microcontroller = new Microcontoller(sensor);
    }

    run(): { temp: number, airmoist: number, airpress: number } {
        const data = this.microcontroller.getDataFromSensor();
        this.microcontroller.connectDisplay(this.display);
        this.microcontroller.startDisplay();

        return data;
    }

    addDisplay(display: Display) {
        this.microcontroller.connectDisplay(display);
    }
}

class Microcontoller {
    private sensor: Sensor;
    private display: Display;
    protected data: {
        temp: number,
        airpress: number,
        airmoist: number
    };

    constructor(sensor: Sensor) {
        this.sensor = sensor;
        this.data = { temp: 0, airpress: 0, airmoist: 0 }
    }

    getDataFromSensor(): { temp: number, airpress: number, airmoist: number } {
        this.data.temp = this.sensor.getTemp();
        this.data.airpress = this.sensor.getPressure();
        this.data.airmoist = this.sensor.getMoisture();

        return this.data;
    }

    connectDisplay(display: Display) {
        this.display = display;
    }

    startDisplay() {
        if (this.display) {
            this.display.showContent(this.data.temp);
        } else {
            console.log('Please connect a display first');
        }
    }
}

class Display {
    showContent(content): void {
        console.log(`Current temperature is ${content}`);
    }
}

class Sensor {
    getTemp(): number {
        return Math.floor(Math.random() * (60 - (-40) + 1)) + (-40);
    }

    getMoisture(): number {
        return Math.floor(Math.random() * (60 - (-40) + 1)) + (-40);
    }

    getPressure(): number {
        return Math.floor(Math.random() * (60 - (-40) + 1)) + (-40);
    }

}

const test1 = new Wetterstation(1);

setInterval(() => {
    test1.run();
    test1.showData();
}, 2000);
