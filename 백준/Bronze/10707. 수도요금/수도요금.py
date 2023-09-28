x_a = int(input());
y_b = int(input());
y_c = int(input());
y_d = int(input());
liter = int(input());

x_money = x_a * liter;
y_money = 0;
if liter <= y_c:
  y_money = y_b
elif y_c < liter:
  y_money = y_b + ((liter-y_c)*y_d)

if x_money > y_money :
  print(y_money)
else:
  print(x_money)