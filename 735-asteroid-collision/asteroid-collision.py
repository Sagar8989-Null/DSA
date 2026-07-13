class Solution(object):
    def asteroidCollision(self, asteroids):

        mono = []

        for asteroid in asteroids:

            while mono and mono[-1] > 0 and asteroid < 0 and mono[-1] < abs(asteroid):
                mono.pop()

            if mono and mono[-1] > 0 and asteroid < 0:
                if mono[-1] == abs(asteroid):
                    mono.pop()
                elif mono[-1] > abs(asteroid):
                    continue
                else:
                    mono.append(asteroid)
            else:
                mono.append(asteroid)

        return mono

                




