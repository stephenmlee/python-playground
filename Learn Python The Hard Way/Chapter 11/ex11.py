print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = int(raw_input())
print "How much do you weigh",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy" % (age, height, weight)

test = raw_input("test: ")

age_height = age * height

print "Age * height = %d" % age_height