from collections import deque


def accommodate_new_pets(*data):
    capacity = int(data[0])
    max_weight = float(data[1])
    pet_types = {}
    data = deque(data[2:])

    while data:

        if capacity > 0:
            curr_pet, curr_weight = data.popleft()
            if max_weight >= float(curr_weight):
                capacity -= 1
                if curr_pet not in pet_types:
                    pet_types[curr_pet] = 1
                else:
                    pet_types[curr_pet] += 1
        else:
            break
    res = ""
    if not data:
        res = f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:"
    else:
        res = "You did not manage to accommodate all pets!\nAccommodated pets:"

    return res + "\n" + "\n".join([f"{k}: {v}" for k, v in sorted(pet_types.items(), key=lambda x: x[0])])


# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))
# print(accommodate_new_pets(
#     10,
#     10.0,
#     ("cat", 5.8),
#     ("dog", 10.5),
#     ("parrot", 0.8),
#     ("cat", 3.1),
# ))
# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))

from unittest import TestCase, main


class Test(TestCase):
    def test_accommodate_pets(self):
        result = accommodate_new_pets(
            10,
            15.0,
            ("cat", 5.8),
            ("dog", 10.0),

        )

        self.assertEqual(
            result.strip(),
            """All pets are accommodated! Available capacity: 8.
Accommodated pets:
cat: 1
dog: 1""")


if __name__ == '__main__':
    main()
