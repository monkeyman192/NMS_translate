from collections import OrderedDict as odict
import json
import struct

import idc  # noqa
import idaapi  # noqa


BASE = 0x140000000
START_OFFSET = 0x140B51020


def instr_type(loc):
    """ A simple renaming of the idc function to make the code more readable"""
    return idc.print_insn_mnem(loc)


def hex_to_chars(num):
    """ Convert the hex representation of the number to a correctly ordered
    string.

    Parameters
    ----------
    val: int
        The integer representing the string. This is in reverse order.
        Ie. XXYYZZ -> chr(ZZ)chr(YY)chr(XX)

    Returns
    -------
    str
        The actual string.
    """
    # convert to an actual number
    return (chr(num & 0xFF)
            + chr((num & 0xFF00) >> 8)
            + chr((num & 0xFF0000) >> 16))


def get_jumptable_locs(loc, inner=False):
    """ Returns the locations of all locs in the jump table."""
    jt_locs = odict()
    while True:
        jt_info = idaapi.get_switch_info_ex(loc)
        if jt_info and jt_info.jumps != 0:
            loc = jt_info.jumps
            element_num = jt_info.get_jtable_size()
            element_size = jt_info.get_jtable_element_size()
            for num in range(element_num):
                table_entry = loc + num * element_size
                jump_loc = idc.GetManyBytes(table_entry, element_size)
                offset = struct.unpack('<I', jump_loc)[0] + BASE
                if inner:
                    jt_locs[chr(num + 0x61)] = offset
                else:
                    jt_locs[num] = offset
            return jt_locs
        loc = idc.next_head(loc)


def get_letter_weights(loc):
    """ Return a dictionary of letters with their weights. """
    data = odict()
    char = ''
    single_letter = False
    while True:
        if instr_type(loc) == 'mov':
            opnd0 = idc.GetOpnd(loc, 0)
            if opnd0 == 'r9b':
                # In this case we are setting r9 to be the number of choices
                # we had which looks to be used to set which of the 7 things
                # are picked??
                # Either way, we are done when this happens so return it with
                # the other data in case we need it...
                return data
            elif opnd0 == 'r8b':
                single_letter = True
            elif opnd0 == 'rcx':
                # This is for default cases I think. Return no character.
                data[''] = 1
                return data
            else:
                # get the letter value
                char = chr(idc.get_operand_value(loc, 1))
                if single_letter:
                    # In this case we only have one character
                    data[char] = 1
                    return data
        elif instr_type(loc) == 'movss':
            if idc.GetOpnd(loc, 0) == 'xmm0':
                # load a float
                float_loc = idc.get_operand_value(loc, 1)
                val = struct.unpack('<f', idc.get_bytes(float_loc, 4))[0]
                data[char] = val
        loc = idc.next_head(loc)


def map_loc(loc):
    """ Create a dictionary of the loc info. """
    # inital "entry point" locations which are directly from the jump table
    # have two `mov` commands. We ignore these.
    data = []
    chars = ''
    while True:
        if instr_type(loc) == 'mov':
            # If it is moving something into the eax register or from it we
            # ignore it and move on
            if idc.GetOpnd(loc, 0) == 'eax' or idc.GetOpnd(loc, 1) == 'eax':
                pass
            else:
                # In this case we have hit the function that returns a letter
                # based on some weight.
                return get_letter_weights(loc)
        elif instr_type(loc) == 'cmp':
            # Get the chars
            chars = hex_to_chars(idc.get_operand_value(loc, 1))
        elif instr_type(loc) in ('ja', 'jz'):
            jump_loc = idc.get_operand_value(loc, 0)
            jump_reason = instr_type(loc)
            data.append([chars, map_loc(jump_loc), jump_reason])
        elif instr_type(loc) == 'jmp':
            # we're done!
            return data
        loc = idc.next_head(loc)


if __name__ == "__main__":
    data = odict()
    main_jt_locs = get_jumptable_locs(START_OFFSET)
    for num, loc in main_jt_locs.items():
        print('mapping ' + str(num))
        print('--------------')
        data[num] = odict()
        read_loc = loc + 0xA
        jumptable_locs = get_jumptable_locs(idc.get_operand_value(read_loc, 0),
                                            True)
        for letter, loc in jumptable_locs.items():
            print('mapping ' + letter)
            data[num][letter] = map_loc(loc)
    with open('letter_map.json', 'w') as f:
        json.dump(data, f)
