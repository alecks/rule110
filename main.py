import png, sys

(rule, width, height) = (110, 2500, 2500)
if len(sys.argv) >= 4: (rule, width, height) = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

row = [0] * (width-1) + [1]

s = bin(rule)[2:].zfill(8)
rbits = [int(x) for x in s[::-1]]

pdata = [row]

for i in range(height):
  r = row[-1:] + row + row[:1]
  row = [rbits[r[i]*4 + v*2 + r[i+2]] for (i, v) in enumerate(row)]
  pdata.append(row)

ll = [[255 - v * 255 for v in row] for row in pdata]
png.from_array(ll, 'L').save("rule%d-%dx%s.png" % (rule, width, height))
