# Si es un Str los suma y si es un Int los concatena
def stupid_addition(a, b):
	if type(a) == int and type(b) == int:
		return str(a) + str(b)
	else:
		if type(a) == str and type(b) == str:
			return int(a) + int(b)
		else:
			return None