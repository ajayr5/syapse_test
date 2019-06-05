import pytest
import re
from car import Car
speed_data = {45, 50, 55, 100}
pattern = "^(\d{13})?$"


@pytest.mark.parametrize("speed_brake", speed_data)
def test_car_brake(speed_brake):
    car = Car(50)
    car.brake()
    assert car.speed == speed_brake


@pytest.mark.parametrize("speed_accelerate", speed_data)
def test_car_accelerate(speed_accelerate):
    car = Car(50)
    car.accelerate()
    assert car.speed == speed_accelerate


def test_phone():
    result = re.match(pattern, str(Car.phone))
    print("result:", result)
    assert result