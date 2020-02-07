#!/bin/python3

import sys


grid = []
empty_row = [0]*26
for app in range(3):
    grid.append(empty_row)
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid_t.insert(0,0)
    grid_t.insert(0,0)
    grid_t.insert(0,0)
    grid_t.extend([0,0,0])
    grid.append(grid_t)
for app in range(3):
    grid.append(empty_row)

# print(grid)
max_ans=0
for i in range(3,23):
    for j in range(3,23):
        #down
        ans1= grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
        #up
        ans2=0 #grid[i][j]*grid[i][j-1]*grid[i][j-2]*grid[i][j-3]
        #right
        ans3= grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
        #left
        ans4= 0#grid[i][j]*grid[i-1][j]*grid[i-2][j]*grid[i-3][j]
        #top right diagonal
        ans5=0 #grid[i][j]*grid[i+1][j-1]*grid[i+2][j-2]*grid[i+3][j-3]
        #top left diagonal
        ans6= 0#grid[i][j]*grid[i-1][j-1]*grid[i-2][j-3]*grid[i-3][j-3]
        #bottom right diagonal
        ans7= grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
        #bottom left diagonal
        ans8= grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
        max_ans = max(max_ans,max(ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8))
print(max_ans)
