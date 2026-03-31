class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        prev_car_time = 0

        for p,s in sorted(zip(position,speed),reverse=True):
            time = (target-p)/s
            if time > prev_car_time:
                fleet+=1
                prev_car_time = time
        return fleet
