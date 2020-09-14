# Getting Ready for Physics Class

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# 1
def f_to_c(f_temp):
  c_temp = (f_temp-32)*5/9

  return c_temp

# 2
f100_in_celsius = 100
print(f_to_c(f100_in_celsius))

# 3
def c_to_f(c_temp):
  f_temp = c_temp*(9/5)+32

  return f_temp

# 4
c0_in_fahrenheit = 0
print(c_to_f(c0_in_fahrenheit))

# 5
def get_force(mass, acceleration):
  return mass*acceleration

# 6
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# 7
print(f"The GE train supplies {train_force} Newtons of force.")

# 8
def get_energy(mass, c = 3*10**8): 
  return mass*(c**2)

# 9
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)

# 10
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# 11
def get_work(mass, acceleration, distance):
  get_force = mass*acceleration
  return get_force*distance

# 12
train_work = get_work(train_mass, train_acceleration, train_distance)

# 13
print("The GE train does " + str(train_work) + " Joules of work over "+ str(train_distance) + " meters.")