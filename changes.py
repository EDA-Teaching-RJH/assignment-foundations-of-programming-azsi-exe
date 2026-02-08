# Line 13 = now it will stop printing once it hits 5, instead of an infinite loop. [WRONG, adjustment below (Line 16).]
# Line 16 (additional line made) = adds one to loading variable. once it hits 5, it will stop the loop.
# Line 29 = missing '='.
# Line 33 =  only 4 options (starting from 0), therefore changing this to length of the actual list would fix any errors.
# Line 34 = prints divison as well.
# Line 43 + 45 (additional line made) =  if only the name list is updated, it causes the lists to be different lengths, causing an error when viewing as it relies on the lists being parallel (pulling data for 7th crew member: n[6] + r[6] + d[6] would only be possible if lists were updated correctly).
# Line 53 - 60 = creating if statement prevents crash if the name entered does not exist in the list.
# Line 67 = "commander" not defined as a rank. it separates rank into 2 seprate values, as it is checking "Commander" by itself, not as a rank.
# Line 69 =  count is an int, not str, therefore a comma is used. otherwise + would be used.
# Line 100 = () at the end, in order to call function.
# Line 126 = empty line deleted
# Fixing line 43 + 45, allows all three lists to grow in parallel. Line 55-57 uses the same positioning removing a crew member as adding a crew member (Line 44-45), so no crew member is removed incorrectly or breaks.