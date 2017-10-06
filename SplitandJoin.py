# link: https://www.hackerrank.com/challenges/python-string-split-and-join
def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

line=str(raw_input())
print split_and_join(line)
