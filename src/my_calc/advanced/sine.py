import math

def calculate_sine():
    angle_degrees = int(input())
    angle_radians = math.radians(angle_degrees)
    sine_value = math.sin(angle_radians)
    return sine_value


def entrypoint_fun():
    print("This is the entrypoint function of sine.py")
    res = calculate_sine()
    return res

if __name__ == "__main__":
    k = entrypoint_fun()
    k = round(k, 2) 
    print(k)


