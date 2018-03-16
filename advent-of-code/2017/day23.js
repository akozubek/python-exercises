b = 93;
c = b;
if a != 0 {
  b = b*100+100000;
  c = b+17000;
}
while (b != c) {
  f = 1;
  for(d = 2; d <= b; d++) {
    for(e = 2; e <= b; e++) {
      if d*e-b== 0 {
        f = 0;
      }
    }
  }
  if (f == 0) {
    h = h+1;
  }
  b = b+17;
}
