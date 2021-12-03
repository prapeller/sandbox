class Road:
    _length = int()
    _width = int()

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self, one_sqr_m_weigth=25, thickness=5):
        return self._length * self._width * one_sqr_m_weigth * thickness


road = Road(20, 5000)
print(road.road_weight())
print(road.road_weight(30, 20))
