from typing import List

from .data import get_sequela_list, get_sequela_data
from .base_template_builder import modelable_entity_attrs, gbd_record_attrs
from .util import make_import, make_module_docstring, make_record, to_id, SPACING, TAB
from .globals import ID_TYPES

IMPORTABLES_DEFINED = ('Sequela', 'Healthstate', 'sequelae')


def get_base_types():
    sequela_attrs = [('name', 'str'),
                      ('kind', 'str'),
                      ('gbd_id', ID_TYPES.S_ID),
                      ('dismod_id', ID_TYPES.ME_ID)]
    sequela_attrs += [('healthstate', 'Healthstate'),]
    return {
        'Healthstate': {
            'attrs': (('name', 'str'),
                      ('kind', 'str'),
                      ('gbd_id', ID_TYPES.HS_ID),),
            'superclass': ('ModelableEntity', modelable_entity_attrs),
            'docstring': 'Container for healthstate GBD ids and metadata.',
        },
        'Sequela': {
            'attrs': tuple(sequela_attrs),
            'superclass': ('ModelableEntity', modelable_entity_attrs),
            'docstring': 'Container for sequela GBD ids and metadata.'
        },
        'Sequelae': {
            'attrs': tuple([(name, 'Sequela') for name in get_sequela_list()]),
            'superclass': ('GbdRecord', gbd_record_attrs),
            'docstring': 'Container for GBD sequelae.',
        },
    }


def make_sequela(name: str, sid: float, mei_id: float,
                 hs_name: str, hsid: float) -> str:
    hs_name = 'UNKNOWN' if hs_name == 'nan' else f"'{hs_name}'"
    out = ""
    out += TAB + f"'{name}': Sequela(\n"
    out += TAB*2 + f"name='{name}',\n"
    out += TAB * 2 + f"kind='sequela',\n"
    out += TAB*2 + f"gbd_id={to_id(sid, ID_TYPES.S_ID)},\n"
    out += TAB*2 + f"dismod_id={to_id(mei_id, ID_TYPES.ME_ID)},\n"
    out += TAB*2 + f"healthstate=Healthstate(\n"

    out += TAB*3 + f"name={hs_name},\n"
    out += TAB*3 + f"kind='healthstate',\n"
    out += TAB*3 + f"gbd_id={to_id(hsid, ID_TYPES.HS_ID)},\n"
    out += TAB*2 + f"),\n"
    out += TAB + f"),\n"
    return out


def make_sequelae(sequela_list: List[str]) -> str:
    out = "sequelae = Sequelae(**{\n"
    for (name, sid, mei_id, hs_name, hsid) in sequela_list:
        out += make_sequela(name, sid, mei_id, hs_name, hsid)
    out += "})\n"
    return out


def build_mapping_template() -> str:
    out = make_module_docstring('Mapping templates for GBD sequelae.', __file__)
    out += make_import('typing', ('Union',)) + '\n'
    out += make_import('.id', (ID_TYPES.S_ID, ID_TYPES.ME_ID, ID_TYPES.HS_ID))
    out += make_import('.base_template', ('ModelableEntity', 'GbdRecord'))

    for entity, info in get_base_types().items():
        out += SPACING
        out += make_record(entity, **info)
    return out


def build_mapping() -> str:
    out = make_module_docstring('Mapping of GBD sequelae.', __file__)
    out += make_import('.id', (ID_TYPES.S_ID, ID_TYPES.HS_ID, ID_TYPES.ME_ID))
    out += make_import('.sequela_template', ('Healthstate', 'Sequela', 'Sequelae')) + SPACING
    out += make_sequelae(get_sequela_data())
    return out
