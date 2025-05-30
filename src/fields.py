from dataclasses import dataclass, field

@dataclass
class Field():
    key: str
    id: str
    lighted: bool = False
    turf: bool = False
    bases: list[int] = field(default_factory=list)


FIELDS = [
    # Dahl
    Field('Dahl1', '1725', False, False, [90]),
    Field('Dahl2', '1652', True, False, [60]),
    Field('Dahl3', '1727', False, False, [60]),
    Field('Dahl4', '1728', False, False, [60]),

    # Meadowbrook
    Field('MB1', '1654', False, False, [90]),
    Field('MB2', '1663', False, False, [60]),
    Field('MB3', '1664', False, False, [60]),

    # Magnuson
    Field('Mag8', '444', False, True, [90]),
    Field('Mag9', '445', True, True, [60]),
    
    # Lower Woodland
    Field('LW1', '391', True, True, [90]),
    # These supposedly have 90 
    Field('LW3', '2415', True, False, [60, 70, 80]),
    Field('LW4', '2412', True, False, [60, 80]),
    Field('LW5', '2413', True, False, [60, 80]),
    Field('LW6', '2414', True, False, [60, 70, 80]),
    
    # Loyal Heights
    Field('LH1', '1799', True, True, [90]),
    Field('LH2', '1801', True, True, [60]),

    # View Ridge
    Field('VR1', '1732', False, False, [90]),
    Field('VR2', '1738', False, False, [60]),
    
    # Maple Leaf
    Field('Maple1', '1700', False, False, [60]),
    Field('Maple2', '1764', False, False, [60]),
    
    # Washington Park
    Field('Wash1', '2052', True, True, [70, 80]),
    Field('Wash2', '2053', True, True, [60, 70]),
]

FIELD_MAP = dict((f.key, f) for f in FIELDS)