"""
 Run the shell and import your models

"""
from .models import Dojo, Ninja
print("diggles")
# Query: Create 3 new dojos
d1 = Dojo(name='CoderDojo Silicon Beach', city="Los Angeles", state="California")
d1.save()
print(d1)
print(d1.id)
d2 = Dojo(name='CoderDojo', city="San Francisco", state="California")
d2.save()
d3 = Dojo(name='CoderDojo Silicon Valley', city="Sunnyvale", state="California")
d3.save()

# Query: Delete the 3 dojos you just created
d1.delete()
d2.delete()
d3.delete()

# Query: Create 3 more dojos
d1 = Dojo(name='CoderDojo Silicon Beach', city="Los Angeles", state="California")
d1.save()
d2 = Dojo(name='CoderDojo', city="San Francisco", state="California")
d2.save()
d3 = Dojo(name='CoderDojo Silicon Valley', city="Sunnyvale", state="California")
d3.save()

# Query: Create 3 ninjas that belong to the first dojo
n1 = Ninja(dojo_id=d1, first_name='joe', last_name='smith')
n1.save()
n2 = Ninja(dojo_id=d1, first_name='james', last_name='smith')
n2.save()
n3 = Ninja(dojo_id=d1, first_name='david', last_name='smith')
n3.save()

# Query: Create 3 ninjas that belong to the second dojo
n4 = Ninja(dojo_id=d2, first_name='joe', last_name='garcia')
n4.save()
n5 = Ninja(dojo_id=d2, first_name='james', last_name='garcia')
n5.save()
n6 = Ninja(dojo_id=d2, first_name='david', last_name='garcia')
n6.save()

# Query: Create 3 ninjas that belong to the third dojo
n7 = Ninja(dojo_id=d3, first_name='joe', last_name='lee')
n7.save()
n8 = Ninja(dojo_id=d3, first_name='james', last_name='lee')
n8.save()
n9 = Ninja(dojo_id=d3, first_name='david', last_name='lee')
n9.save()

# Query: Retrieve all the ninjas from the first dojo
r = d1.ninjas
print(r)

# Query: Retrieve all the ninjas from the last dojo
r = d2.ninjas
print(r)

# Query: Retrieve the last ninja's dojo
r = d3.ninjas
print(r)


# Add a new text field called "desc" to your Dojo class
# Create and run the migration files to update the table in your database. If needed, provide a default value of
# "old dojo"
# Query: Create a new dojo
d4 = Dojo(name='CoderDojo Silicon Beach', city="Los Angeles", state="California", desc="Bits of sand everywhere")
d4.save()
# Submit your .txt file that contains all the queries you ran in the shell







