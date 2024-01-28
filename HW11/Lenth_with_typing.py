class Lenth:

   metric: dict[str, float] = {
       "mm": 0.001,
       "cm": 0.01,
       "m": 1,
       "km": 1000,
       "in": 0.0254,
       "ft": 0.3048,
       "yd": 0.9144,
       "mi": 1609.344,
   }

   def __init__(self, value: float, unit: str = "m") -> None:
       self.value: float = value
       self.unit: str = unit

   def convertToMeters(self) -> float:
       return self.value * self.metric[self.unit]

   def __add__(self, other: "Lenth") -> "Lenth":
       length_meter = self.convertToMeters() + other.convertToMeters()
       return Lenth(length_meter / self.metric[self.unit], self.unit)

   def __sub__(self, other: "Lenth") -> "Lenth":
       length_meter = self.convertToMeters() - other.convertToMeters()
       return Lenth(length_meter / self.metric[self.unit], self.unit)

   def __str__(self) -> str:
       return f"{self.convertToMeters():.2f} m"


distance1 = Lenth(5, "yd")
distance2 = Lenth(5, "ft")
distance3 = distance1+distance2
print(distance3.value, distance3.unit)
print(distance1+distance2)