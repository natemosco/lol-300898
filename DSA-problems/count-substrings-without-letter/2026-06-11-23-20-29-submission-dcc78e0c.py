# Wrong Answer: Submission produced output that did not match the expected output.
def count_substrings_without_letter(s):
  sections = s.split('a')
  total = 0
  for section in sections:
    n = len(section)
    total += n * (n + 1) // 2
  return 1
