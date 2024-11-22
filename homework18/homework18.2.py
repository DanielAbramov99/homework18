# .2 מה ההבדל בין tuple ל- list ? מתי תעדיף להשתמש בכל אחד מהם?
# The difference between tuple and a list is that in list you can at any given time to change the insides of a list as well his values or even value type while in tuple you cannot change values that were given to a specific tuple from the start,
# The pros of using tuple is that tuple uses a lot less memory than all other data types.


# .3 ה- tuple הוא רשימה שלא ניתן לשנות אותה.
# הסבר מדוע הקוד הבא לא גורם לשגיאה:
#
# data_tuple = (
# {"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
# )
# data_tuple[0] ["age"] = 31
# data_tuple[0] .clear()

# The given code doesn't get error because while you cannot change insides of a tuple if you have a list or as in this code dictionary you can still make changes to values stored inside given dictionary because it doesn't change the address of the dictionary itself.
