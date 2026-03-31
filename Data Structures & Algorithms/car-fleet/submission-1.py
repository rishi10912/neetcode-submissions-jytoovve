class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        prev_time = 0

        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s

            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets
