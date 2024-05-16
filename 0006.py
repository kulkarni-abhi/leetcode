  """
  Approach
  --------
  If our row is less than the numRows then we can increase it,
  so that the next character can be placed at the next row,
  but if the row is equal to the numRows - 1 then
  we should change direction and place the characters
  in the previous rows.
  """
  row = -1
  direction = "positive"
  rows = [""] * numRows

  for char in s:
    if direction is "positive":
      row += 1
    else:
      row = -1

    rows[row] += char
    if row < 1:
      direction = "positive"
    if row == numRows - 1:
      direction = "negative"
  return "".join(rows)

print(zigzag("PAYPALISHIRING", 4))
