############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
                
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', True, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', True, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', True, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print '{name} pairs with'.format(name=melon.name)
        for pair in melon.pairings:
            print '- {}'.format(pair)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    codes = {}

    for melon in melon_types:
        codes[melon.code] = melon

    return codes

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, picker):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.picker = picker
        # self.name = name

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3

    # Needs __init__ and is_sellable methods

# def make_melons(melon_types):
#     """Returns a list of Melon objects."""

#     melon1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila', 1)
#     melon2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila', 2)
#     melon3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila', 3)
#     melon4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila', 4)
#     melon5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael', 5)
#     melon6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael', 6)
#     melon7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael', 7)
#     melon8 = Melon(melon_types['musk'], 6, 7, 4, 'Michael', 8)
#     melon9 = Melon(melon_types['yw'], 7, 10, 3, 'Sheila', 9)

#     melons = [melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9]

#     return melons


# def get_sellability_report(melons):
#     """Given a list of melon object, prints whether each one is sellable."""

#     for melon in melons:
#         print 'Melon {}'.format(melon.name)
#         print '{} harvested this melon'.format(melon.picker)
#         print 'Harvested from Field {}'.format(melon.field)
#         if melon.is_sellable():
#             print 'Melon is sellable'
#         else:
#             print 'Melon is not sellable'


# codes = make_melon_type_lookup(make_melon_types())
# all_melons = make_melons(codes)
# get_sellability_report(all_melons)


def make_melon(melon_info, melon_types):
    return Melon(melon_types[melon_info[5]], melon_info[1], melon_info[3], melon_info[-1], melon_info[-4])


def make_melons_from_file(filename):

    melon_list = []

    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            melon_info = line.split()
            melon_list.append(make_melon(melon_info, melon_types))

    return melon_list

melon_types = make_melon_type_lookup(make_melon_types())
melon_list = make_melons_from_file('harvest_log.txt')

# test
print melon_list[0].color_rating
print melon_list[0].melon_type.code
print melon_list[0].melon_type.is_seedless