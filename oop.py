class Angle(object):
    def __init__(self, degrees, arcmins, arcsecs):
        # Constructor
        self.degrees = degrees + arcmins // 60 + arcsecs // 3600
        self.arcmins = arcmins % 60 + arcsecs // 60
        self.arcsecs = arcsecs % 60

    @classmethod
    def from_decimal(cls, x):
        # allows to build an object from a decimal angle value
        # (i.e. 10.5 degrees should give 10°30').
        degrees = int(x)
        arcmins = int((x - degrees) * 60)
        arcsecs = ((x - degrees) * 60 - arcmins) * 60
        return cls(degrees, arcmins, arcsecs)

    def __add__(self, other):
        # allows to add two corners to a new corner
        deg_new = self.degrees + other.degrees
        amin_new = self.arcmins + other.arcmins
        asec_new = self.arcsecs + other.arcsecs
        return Angle(deg_new, amin_new, asec_new)

    def __sub__(self, other):
        # lets you subtract two corners to a new corner
        deg_new = self.degrees - other.degrees
        amin_new = self.arcmins - other.arcmins
        asec_new = self.arcsecs - other.arcsecs
        return Angle(deg_new, amin_new, asec_new)

    def __neg__(self):
        # to get negative angle
        deg_new = -self.degrees
        amin_new = -self.arcmins
        asec_new = -self.arcsecs
        return Angle(deg_new, amin_new, asec_new)

    def show(self):
        # print the current value of degrees, arcminutes and arcseconds
        print("(%i, %i, %1.1f)" % (self.degrees, self.arcmins, self.arcsecs))
        
    def decimal(self):
        # to get the decimal value of the angle (10°30' → 10.5)
        x = self.degrees + self.arcmins / 60 + self.arcsecs / 3600
        return x

''' Задача о высоте верхней кульминации: 
программа принимает на вход широту и склонение звезды, а на выход дает высоту 
верхней кульминации этой звезды. Все вычисления углов в программе должны выполняться 
при помощи объектов класса Angle. '''

inp = input('Введите D, если хотите ввести значения в десятичной записи; введите A, \
если хотите ввести углы, минуты и секунды: ')

if inp == 'D':
    phi = float(input('Введите широту: '))
    dec = float(input('Введите склонение: '))
# FIX
    h_SZ = 90 - phi + dec # calculating the height of the upper culmination South of Zenith
    h_NZ = 90 - dec + phi # calculating the height of the upper culmination North of Zenith

    print('Высота верхей кульминации к Югу от Зенита: %1.1f' % h_SZ, ' or ', end=' ')
    Angle.from_decimal(h_SZ).show()
    print('Высота верхей кульминации к Северу от Зенита: %1.1f' % h_NZ, ' or ', end=' ')
    Angle.from_decimal(h_NZ).show()

elif inp == 'A':
    print('Широта')
    phi = Angle(int(input('Введите градусы: ')), int(input('Введите минуты: ')), float(input('Введите секунды: ')))
    print('Склонение')
    dec = Angle(int(input('Введите градусы: ')), int(input('Введите минуты: ')), float(input('Введите секунды: ')))

    tmp = phi - dec # eq: phi.__sub__(dec)
    halfpi = Angle.from_decimal(90)
    h_SZ = halfpi - tmp
    h_NZ = halfpi + tmp # eq: halfpi.__add__(tmp)

    print('Высота верхей кульминации к Югу от Зенита: %1.1f' % h_SZ.decimal(), ' or ', end=' ')
    h_SZ.show()
    print('Высота верхей кульминации к Северу от Зенита: %1.1f' % h_NZ.decimal(), ' or ', end=' ')
    h_NZ.show()

else:
    print('Попробуйте еще раз...')
