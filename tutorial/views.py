from pyramid.view import (
    view_config,
    view_defaults
    )

from gpiozero import OutputDevice, PWMOutputDevice, LED, Servo
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.22')
factory2 = PiGPIOFactory(host='192.168.0.21')

en_1 = PWMOutputDevice(12, pin_factory=factory)
en_2 = PWMOutputDevice(26, pin_factory=factory)
motor_in1 = OutputDevice(13,  pin_factory = factory)
motor_in2 = OutputDevice(21,  pin_factory = factory)
motor_in3 = OutputDevice(17,  pin_factory = factory)
motor_in4 = OutputDevice(27,  pin_factory = factory)

pin1 = OutputDevice(7,  pin_factory = factory2)
pin2 = OutputDevice(8,  pin_factory = factory2)
pin3 = OutputDevice(9,  pin_factory = factory2)
pin4 = OutputDevice(10,  pin_factory = factory2)

#Define the eyes
linus_eye = LED(16, pin_factory=factory)
torvalds_eye = LED(25, pin_factory=factory2)

#Define the servos
servo_one = Servo(22, pin_factory=factory)
servo_two = Servo(23, pin_factory=factory)

@view_defaults(renderer='dual.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request
    @view_config(route_name='dualrobot')
    def home(self):
        return {}
    @view_config(route_name='forward')
    def forwards(self):
        pin1.off()
        pin2.on()
        pin3.on()
        pin4.off()
        return {}
    @view_config(route_name='backward')
    def backwards(self):
        pin1.on()
        pin2.off()
        pin3.off()
        pin4.on()
        return {}
    @view_config(route_name='left')
    def left(self):
        pin1.on()
        pin2.off()
        pin3.on()
        pin4.off()
        return {}
    @view_config(route_name='right')
    def right(self):
        pin1.off()
        pin2.on()
        pin3.off()
        pin4.on()
        return {}
    @view_config(route_name='stop')
    def stop(self):
        pin1.off()
        pin2.off()
        pin3.off()
        pin4.off()
        return {}
    @view_config(route_name='torvaldseye')
    def torvaldson(self):
        torvalds_eye.on()
        return {}
    @view_config(route_name='torvaldsoff')
    def torvaldsoff(self):
        torvalds_eye.off()
        return {}
    @view_config(route_name='directionone')
    def north(self):
        motor_in1.on()
        motor_in2.off()
        motor_in3.on()
        motor_in4.off()
        return {}
    @view_config(route_name='directiontwo')
    def south(self):
        motor_in1.off()
        motor_in2.on()
        motor_in3.off()
        motor_in4.on()
        return {}
    @view_config(route_name='directionthree')
    def west(self):
        motor_in1.on()
        motor_in2.off()
        motor_in3.off()
        motor_in4.on()
        return {}
    @view_config(route_name='directionfour')
    def east(self):
        motor_in1.off()
        motor_in2.on()
        motor_in3.on()
        motor_in4.off()
        return {}
    @view_config(route_name='stoptwo')
    def stoptwo(self):
        motor_in1.off()
        motor_in2.off()
        motor_in3.off()
        motor_in4.off()
        return {}
    @view_config(route_name='linuseye')
    def eyeon(self):
        linus_eye.on()
        return {}
    @view_config(route_name='linusoff')
    def eyeoff(self):
        linus_eye.off()
        return {}
    @view_config(route_name='min')
    def servoMin(self):
        servo_one.min()
        return {}
    @view_config(route_name='mid')
    def servoMid(self):
        servo_one.mid()
        return {}
    @view_config(route_name='max')
    def servoMax(self):
        servo_one.max()
        return {}
    @view_config(route_name='min2')
    def servoMin2(self):
        servo_two.min()
        return {}
    @view_config(route_name='mid2')
    def servoMid2(self):
        servo_two.mid()
        return {}
    @view_config(route_name='max2')
    def servoMax2(self):
        servo_two.max()
        return {}
    @view_config(route_name='thirty')
    def thirty(self):
        en_1.value = 0.3
        return {}
    @view_config(route_name='fifty')
    def fifty(self):
        en_1.value = 0.5
        return {}
    @view_config(route_name='full')
    def full(self):
        en_1.value = 1
        return {}
    @view_config(route_name='thirty2')
    def thirty2(self):
        en_2.value = 0.3
        return {}
    @view_config(route_name='fifty2')
    def fifty2(self):
        en_2.value = 0.5
        return {}
    @view_config(route_name='full2')
    def full2(self):
        en_2.value = 1
        return {}