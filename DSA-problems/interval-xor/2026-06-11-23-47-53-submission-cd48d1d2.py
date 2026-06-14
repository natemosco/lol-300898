def interval_xor(a, b):
  # Ensure a starts before b
  if a[0] > b[0]:
    return interval_xor(b, a)

  a_s, a_e = a
  b_s, b_e = b

  # Group 1: a starts before b
  if a_s < b_s:
    # Case 1: No overlap
    if a_e < b_s:
      return [[a_s, a_e], [b_s, b_e]]

    # Case 2: a ends at b_s
    if a_e == b_s:
      return [[a_s, b_e]]

    # Case 3: a ends in the middle of b
    if a_e < b_e:
      return [[a_s, b_s], [a_e, b_e]]

    # Case 4: a ends at b_e
    if a_e == b_e:
      return [[a_s, b_s]]

    # Case 5: a ends after b
    if a_e > b_e:
      return [[a_s, b_s], [b_e, a_e]]

  # Group 2: a and b start at the same point

  # Case 6: a ends in the middle of b
  if a_e < b_e:
    return [[a_e, b_e]]

  # Case 7: a ends at b_e
  if a_e == b_e:
    return []

  # Case 8: a ends after b
  if a_e > b_e:
    return [[b_e, a_e]]

  raise Exception("Internal error")
