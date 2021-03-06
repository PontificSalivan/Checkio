def sun_angle(time):
    ours = ''
    minutes = ''

    if time[0] == '0':

        if int(time[1]) < 6: # если время меньше 06 солнце не видно
            return "I don't see the sun!"

        ours = int(''.join(time[1:2]))
        minutes = int(''.join(time[3:]))
        return ((ours-6)*60 + minutes)*0.25

    # проверка на время больше 18, или время равное 18, но минуты уже больше 00
    elif int(time[:2]) > 18 or (int(time[:2]) == 18 and  int(time[4]) > 0) or (int(time[:2]) == 18 and int(time[3]) > 0):
        return "I don't see the sun!"

    ours = int(''.join(time[:2]))
    minutes = int(''.join(time[3:]))
    return ((ours-6)*60 + minutes)*0.25

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")