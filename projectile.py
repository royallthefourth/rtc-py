from datastructures import Tuple


class Projectile:
    position: Tuple
    velocity: Tuple

    def __init__(self, position: Tuple, velocity: Tuple):
        self.position = position
        self.velocity = velocity

class Environment:
    gravity: Tuple
    wind: Tuple

    def __init__(self, gravity: Tuple, wind: Tuple):
        self.gravity = gravity
        self.wind = wind

def tick(e: Environment, p: Projectile) -> Projectile:
    pos = p.position + p.velocity
    vel = p.velocity + e.gravity + e.wind
    return Projectile(pos, vel)

def main():
    print("hello")

if __name__ == "__main__":
    main()
