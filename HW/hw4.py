import emoji
while True:
    class Car:
        def __init__(self ,speed, color, brand):
            self.speed = speed
            self.color = color     #атрибуты
            self.brand = brand

        def info(self):
            return f'{self.brand} {self.color} going {self.speed}km/h'

    lexus = Car(100, 'white', 'lexus' )
    print(lexus.speed, lexus.color, lexus.brand)
    user_text = input("do you like this car? ")
    if user_text == 'stop':
        print('The program was stopped')
    if user_text == "yes":
        print(emoji.emojize('you are :thumbs_up:'))
    elif user_text == "no":
        print(emoji.emojize('you are :thumbs_down:'))
    else:
        print('you have to text only (yes, no)')