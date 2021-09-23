from typing import List

class Solution:
    def main():
        fp = open("input.txt", "r")
        height = fp.readlines()
        M = max(height)
        left = height[0]
        leftidx = 0
        rain = 0;
        for i in range(len(height)-1):
            right = height[i+1]
            print(right)
            if right <= M and left <= right:
                for j in height[leftidx:i]:
                    print(j)
                    rain = rain + height[j] - left
        print(rain)
    if __name__ == "__main__":
        main()