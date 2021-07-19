esta_chuvendo = True

print("Hoje está " + ("ensolarado.", "chovendo.")[esta_chuvendo])
print("Hoje está " + ("chovendo." if esta_chuvendo else "ensolarado"))
