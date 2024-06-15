import cmath

user_input = complex(input())

r = abs(complex(user_input.real, user_input.imag))
phase_a = cmath.phase(complex(user_input.real, user_input.imag))

print(r)
print(phase_a)
