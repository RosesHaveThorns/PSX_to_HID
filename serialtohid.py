import serial
import vgamepad as vg

soft_gamepad = vg.VDS4Gamepad()

with serial.Serial("COM17", baudrate=57600) as arduino:
    print("opened arduino com port")

    while True:
        dat = str(arduino.readline())[2:-5]
        vals = dat.split(',')
        print(vals)

        start = int(vals[0][0])
        select = int(vals[0][1])
        up = int(vals[0][2])
        right = int(vals[0][3])
        down = int(vals[0][4])
        left = int(vals[0][5])
        l3 = int(vals[0][6])
        r3 = int(vals[0][7])
        l2 = int(vals[0][8])
        r2 = int(vals[0][9])
        l1 = int(vals[0][10])
        r1 = int(vals[0][11])
        triangle = int(vals[0][12])
        circle = int(vals[0][13])
        square = int(vals[0][14])
        cross = int(vals[0][15])

        # buttons

        if (start):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHARE)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHARE)

        if (select):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)

        if (l3):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_LEFT)

        if (r3):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_THUMB_RIGHT)

        if (l2):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)

        if (r2):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)

        if (triangle):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)

        if (circle):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)

        if (square):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)

        if (cross):
            soft_gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        else:
            soft_gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)

        # directional pad

        if (up):
            d = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH
        elif (right):
            d = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST
        elif (down):
            d = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH 
        elif (left):
            d = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST 
        else:
            d = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE 

        soft_gamepad.directional_pad(direction=d)

        # triggers
        
        if (not l1):
            soft_gamepad.left_trigger(value=0)
        else:
            soft_gamepad.left_trigger(value=255)
        if (not r1):
            soft_gamepad.right_trigger(value=0)
        else:
            soft_gamepad.right_trigger(value=255)

        # joysticks

        soft_gamepad.left_joystick(x_value=int(vals[-3]), y_value=int(vals[-4]))  # value between 0 and 255
        soft_gamepad.right_joystick(x_value=int(vals[-1]), y_value=int(vals[-2]))  # value between 0 and 255


        soft_gamepad.update()