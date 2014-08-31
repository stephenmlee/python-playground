name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inches_to_cm = 1 / 0.39370
lbs_to_kg = 0.453592


print "Let's talk about %s." % name
print "He's %.2f cm tall." % (height * inches_to_cm)
print "He's %.2f kg heavy." % (weight * lbs_to_kg)
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# %r format character
print "This is what percent r does: %r" % age

# Round examples
print "Rounding 1.51 %f" % round(1.51)
