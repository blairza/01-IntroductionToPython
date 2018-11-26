"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zane Blair.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(20)

stalin = rg.SimpleTurtle()
stalin.pen = rg.Pen('white',10)
stalin.left(90)
stalin.forward(100)
stalin.right(90)
stalin.pen = rg.Pen('red',10)

napoleon = rg.SimpleTurtle()
napoleon.pen = rg.Pen('white',10)
napoleon.left(90)
napoleon.forward(100)
napoleon.right(90)

napoleon.pen = rg.Pen('blue',10)
napoleon.right(180)

stalin.speed = 10
napoleon.speed = 10

for k in range(36):
    stalin.forward(20)
    napoleon.forward(20)
    stalin.right(5)
    napoleon.left(5)

stalin.forward(20)
napoleon.forward(20)

window.close_on_mouse_click()