# https://leetcode.com/problems/design-underground-system/
# 1396. Design Underground System


class UndergroundSystem:
    def __init__(self) -> None:
        self.passenger_checkin = dict[int, tuple[str, int]]()
        self.station_times = dict[tuple[str, str], tuple[float, int]]()

    def checkIn(self, id: int, station_name: str, t: int) -> None:  # noqa: N802
        self.passenger_checkin[id] = station_name, t

    def checkOut(self, id: int, station_name: str, t: int) -> None:  # noqa: N802
        start_station, start_time = self.passenger_checkin[id]
        trip_time = t - start_time
        avg_time, trips = self.station_times.get((start_station, station_name), (0, 0))

        avg_time = (avg_time * trips + trip_time) / (trips + 1)
        trips += 1
        self.station_times[(start_station, station_name)] = avg_time, trips

    def getAverageTime(  # noqa: N802
        self, start_station: str, end_station: str
    ) -> float:
        return self.station_times[(start_station, end_station)][0]


EPS = 10**-5
underground_system = UndergroundSystem()
underground_system.checkIn(45, "Leyton", 3)
underground_system.checkIn(32, "Paradise", 8)
underground_system.checkIn(27, "Leyton", 10)
# Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
underground_system.checkOut(45, "Waterloo", 15)
# Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
underground_system.checkOut(27, "Waterloo", 20)
# Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
underground_system.checkOut(32, "Cambridge", 22)
# One trip "Paradise" -> "Cambridge", (14) / 1 = 14
assert abs(underground_system.getAverageTime("Paradise", "Cambridge") - 14) <= EPS
# Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
assert abs(underground_system.getAverageTime("Leyton", "Waterloo") - 11) <= EPS
underground_system.checkIn(10, "Leyton", 24)
assert abs(underground_system.getAverageTime("Leyton", "Waterloo") - 11) <= EPS
# Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
underground_system.checkOut(10, "Waterloo", 38)
# Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
assert abs(underground_system.getAverageTime("Leyton", "Waterloo") - 12) <= EPS

underground_system = UndergroundSystem()
underground_system.checkIn(10, "Leyton", 3)
# Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
underground_system.checkOut(10, "Paradise", 8)
# (5) / 1 = 5
assert abs(underground_system.getAverageTime("Leyton", "Paradise") - 5) <= EPS
underground_system.checkIn(5, "Leyton", 10)
# Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
underground_system.checkOut(5, "Paradise", 16)
# (5 + 6) / 2 = 5.5
assert abs(underground_system.getAverageTime("Leyton", "Paradise") - 5.5) <= EPS
underground_system.checkIn(2, "Leyton", 21)
# Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
underground_system.checkOut(2, "Paradise", 30)
# (5 + 6 + 9) / 3 = 6.66667
assert abs(underground_system.getAverageTime("Leyton", "Paradise") - 6.66667) <= EPS
