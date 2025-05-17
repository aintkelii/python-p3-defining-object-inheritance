#!/usr/bin/env python3

from car import Car
from vehicle import Vehicle

class TestVehicle:
    '''Class "Vehicle" in vehicle.py'''

    def test_is_class(self):
        '''is really a class.'''
        assert(object in Vehicle.__bases__)

    def test_has_wheel_size(self):
        '''instantiates with attribute "wheel_size".'''
       

    def test_has_wheel_number(self):
        '''instantiates with attribute "wheel_number".'''
        

    def test_goes_vroom(self):
        '''has a method "go()" that goes "vrrrrrrrooom!"'''
        

    def test_fills_tank(self):
        '''has a method "fill_up_tank" that returns "filling up!"'''
       

class TestCar:
    '''Class "Car" in car.py'''

    def test_is_subclass(self):
        '''is really a subclass of Vehicle.'''
        assert(Vehicle in Car.__bases__)

    def test_has_wheel_size(self):
        '''instantiates with attribute "wheel_size".'''
        

    def test_has_wheel_number(self):
        '''instantiates with attribute "wheel_number".'''
        

    def test_goes_vroom(self):
        '''has a method "go()" that goes "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"'''
       

    def test_fills_tank(self):
        '''has a method "fill_up_tank" that returns "filling up!"'''
       