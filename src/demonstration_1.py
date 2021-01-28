"""
An `image` is represented by a 2-D array of integers, each integer representing
the pixel value of the image (from 0 to 65535).
​
Given a coordinate `(sr, sc)` representing the starting pixel (row and column)
of the flood fill, and a pixel value `newColor`, "flood fill" the image.
​
To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those pixels (also
with the same color as the starting pixel), and so on. Replace the color of all
of the aforementioned pixels with the newColor.
​
At the end, return the modified image.
​
Example 1:
​
```plaintext
Input:
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
​
sr = 1, sc = 1, newColor = 2
Output: [
    [2,2,2],
    [2,2,0],
    [2,0,1]
]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels
connected by a path of the same color as the starting pixel are colored with
the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally
connected to the starting pixel.
```
​
Notes:
​
- The length of `image` and `image[0]` will be in the range `[1, 50]`.
- The given starting pixel will satisfy `0 <= sr < image.length` and
`0 <= sc < image[0].length`.
- The value of each color in `image[i][j]` and `newColor` will be an integer in
`[0, 65535]`.
"""
def flood_fill(image, sr, sc, new_color):
    """
    Inputs:
    image -> List[List[int]]
    sr -> int
    sc -> int
    new_color -> int
​
    Output:
    List[List[int]]
    """
    # we'll need to check the boundaries of our image 
    # keep track of the total number of rows and columns in our 2D array 
    # we need to keep track of the initial color located at the starting point 
    starting_color = image[sr][sc]
    # it doesn't actually matter which traversal method we use since the order
    # in which we perform the flood fill doesn't matter 
    bft(image, starting_color, new_color, sr, sc)
​
    return image 
​
from collections import deque
​
def bft(image, starting_color, new_color, r, c):
    rows = len(image)
    cols = len(image[0])
​
    queue = deque()
    queue.append((r, c)) 
    
    while len(queue) > 0:
        # destructure the coordinates 
        curr_r, curr_c = queue.popleft()
        # paint the starting pixel with the new color 
        image[curr_r][curr_c] = new_color
​
        # north 
        if curr_r - 1 >= 0 and image[curr_r-1][curr_c] == starting_color:
            queue.append((curr_r-1, curr_c))
        # south 
        if curr_r + 1 < rows and image[curr_r+1][curr_c] == starting_color:
            queue.append((curr_r+1, curr_c))
        # east 
        if curr_c + 1 < cols and image[curr_r][curr_c+1] == starting_color:
            queue.append((curr_r, curr_c+1))
        # west 
        if curr_c - 1 >= 0 and image[curr_r][curr_c-1] == starting_color:
            queue.append((curr_r, curr_c-1))
​
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
]
​
print(flood_fill(image, 1, 1, 2))
