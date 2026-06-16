#Unit Converter

measure = float(input("Enter measure that need's to be Converted: "))

unit1 = input("Enter your Current unit (cm , m , mm , km , miles) : ").strip()

unit2 = input("Enter unit you want to Convert into (cm , m , mm , km , miles) : ").strip()

measures = {
    ('cm','m'): 0.01,
    ('cm','mm'): 10,
    ('cm','km'): 0.00001,
    ('cm','miles'): 0.0000062137,
    ('m','cm'): 100,
    ('m','mm'): 1000,
    ('m','km'): 0.001,
    ('m','miles'): 0.000621371,
    ('mm','cm'): 0.1,
    ('mm','m'): 0.001,
    ('mm','km'): 0.000001,
    ('mm','miles'): 0.00000062137119,
    ('km','cm'): 100000,
    ('km','m'): 1000,
    ('km','mm'): 1000000,
    ('km','miles'): 0.621371,
    ('miles','cm'): 160934,
    ('miles','m'): 1609.34,
    ('miles','mm'): 1609344,
    ('miles','km'): 1.60934
}

if unit1 == unit2:
    print(measure)
else:
    measures = measures.get((unit1, unit2))
    if measures is not None:
        print(measure * measures)
    else:
        print("Invalid Unit Entered")