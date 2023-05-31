
# Function to find the new items. List 1 is the old items and List 2 are the new items.
def find_new_and_duplicate_items(list1, list2):
    # convert all items to lower case before creating the sets
    set1 = set(item.lower() for item in list1)
    set2 = set(item.lower() for item in list2)

    new_items = set2 - set1
    duplicate_items = set2 & set1

    return list(new_items), list(duplicate_items)

# Test the function

# Original items
list1 = ["",]

# New items
list2 = [""]

new_items, duplicate_items = find_new_and_duplicate_items(list1, list2)

print("New Items:")
for item in new_items:
    print(item)

print("\nDuplicate Items:")
for item in duplicate_items:
    print(item)

print("\nTotal number of duplicate items: ", len(duplicate_items))