# For-Range
  # For-Range Loops
    * Also known as:
    * "For i in range" loop
    * "For loop"
    * "Range for loop"
    * Clause: for i in range(limit):
    * Block: indented underneath clause
    * i is usually the loop variable
    * In nested for-range loops, outer loop uses i, next inner loop uses j, next inner loop uses k, and so on...
  # When are range loops used?
    * Allows you to access a list index directly
    * Allows you to perform an action an exact number of times
    * Allows you to access multiple lists at the same index
    * Nested for-loops often used to work with grids
  # What does the range function do?
    * Returns a list of numbers in order
    * Three different versions: * range(limit) * Makes a list that starts at 0 and counts to limit by 1 * Does NOT include limit * range(5) -> [0, 1, 2, 3, 4] * range(min, limit) * Makes a list that starts at min and counts to limit by 1 * range(2, 5) -> [2, 3, 4] * range(min, limit, inc) * Makes a list that starts at min and counts to limit by inc * range(0, 10, 3) -> [0, 3, 6, 9]
