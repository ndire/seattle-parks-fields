from dataclasses import dataclass

@dataclass
class Field():
    key: str
    id: str
    lighted: bool = False
    turf: bool = False
    #bases: list[int] = [60]


FIELDS = [
    # Dahl
    Field('Dahl1', '1725', False, False),
    Field('Dahl2', '1652', True, False),
    Field('Dahl3', '1727', False, False),
    Field('Dahl4', '1728', False, False),

    # Magnuson
    Field('Mag8', '444', False, True),
    Field('Mag9', '445', True, True),
    
    # Lower Woodland
    Field('LW1', '391', False, False),
    Field('LW3', '2415', False, False),
    Field('LW4', '2412', False, False),
    Field('LW5', '2413', False, False),
    Field('LW6', '2414', False, False),
    
    # Loyal Heights
    Field('LH1', '1799', False, True),
    Field('LH2', '1801', False, True),
    
    # Maple Leaf
    Field('Maple1', '1700', False, False),
    Field('Maple2', '1764', False, False),
    
    # Washington Park
    Field('Wash1', '2052', False, False),
    Field('Wash2', '2051', False, False),
]