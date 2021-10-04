
# paint a house exercise
class House:
  # constructor
  def __init__(self, wall_area):
    # attributes
    self.wall_area = wall_area

  # methods
  def paint_needed(self, wall_area):
    paint_amount = wall_area * 2.5
    return paint_amount



class Paint:
  def __init__(self, buckets, color):
      self.buckets = buckets
      self.color = color
  
  def total_price(self):
    if self.color == "white".lower():
      return self.buckets * 1.99
    else:
      return self.buckets * 2.19

    


# intantiate an house object

villa_1 = House(10)
villa_1_area = villa_1.wall_area

# call paint_needed method
villa_1_paint = villa_1.paint_needed(villa_1_area)
print(villa_1_paint)

# instantiate paint_1 obj
paint_1 = Paint(color="white", buckets=4)

paint_1_cost = Paint.total_price(paint_1)
print(paint_1_cost)
