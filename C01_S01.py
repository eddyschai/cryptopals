""" Convert Hex to base64 """

def decimal_to_ascii(input: str):
    conversion = {
        '00': 'NUL',    # Null
        '01': 'SOH',    # Start of Header
        '02': 'STX',    # Start of Text 
        '03': 'ETX',    # End of Text
        '04': 'EOT',    # End of Transmission
        '05': 'ENQ',    # Enquiry
        '06': 'ACK',    # Acknowledge
        '07': 'BEL',    # Bell
        '08': 'BS',     # Backspace
        '09': 'HT',     # Horizontal Tab
        '10': 'LF',     # Newline / Line Feed
        '11': 'VT',     # Vertical Tab
        '12': 'FF',     # Form Feed
        '13': 'CR',     # Carriage Return
        '14': 'SO',     # Shift Out
        '15': 'SI',     # Shift In
        '16': 'DLE',    # Data Link Escape
        '17': 'DC1',    # Device Control 1
        '18': 'DC2',    # Device Control 2
        '19': 'DC3',    # Device Control 3
        '20': 'DC4',    # Device Control 4
        '21': 'NAK',    # Negative Achnowledge
        '22': 'SYN',    # Synchronize
        '23': 'ETB',    # End of Transmission Block
        '24': 'CAN',    # Cancel
        '25': 'EM',     # End of Medium
        '26': 'SUB',    # Substitue
        '27': 'ESC',    # Escape
        '28': 'FS',     # File Seperator
        '29': 'GS',     # Group Seperator
        '30': 'RS',     # Record Seperator
        '31': 'US',     # Unit Seperator
        '32': 'SP',     # Space
        '33': '!',
        '34': '"',
        '35': '#',
        '36': '$',
        '37': '%',
        '38': '&',
        '39': "'",
        '40': '(',
        '41': ')',
        '42': '*',
        '43': '+',
        '44': ',',
        '45': '-',
        '46': '.',
        '47': '/',
        '48': '0',
        '49': '1',
        '50': '2',
        '51': '3',
        '52': '4',
        '53': '5',
        '54': '6',
        '55': '7',
        '56': '8',
        '57': '9',
        '58': ':',
        '59': ';',
        '60': '<',
        '61': '=',
        '62': '>',
        '63': '?',
        '64': '@',
        '65': 'A',
        '66': 'B',
        '67': 'C',
        '68': 'D',
        '69': 'E',
        '70': 'F',
        '71': 'G',
        '72': 'H',
        '73': 'I',
        '74': 'J',
        '75': 'K',
        '76': 'L',
        '77': 'M',
        '78': 'N',
        '79': 'O',
        '80': 'P',
        '81': 'Q',
        '82': 'R',
        '83': 'S',
        '84': 'T',
        '85': 'U',
        '86': 'V',
        '87': 'W',
        '88': 'X',
        '89': 'Y',
        '90': 'Z',
        '91': '[',
        '92': '\\',
        '93': ']',
        '94': '^',
        '95': '_',
        '96': '`',
        '97': 'a',
        '98': 'b',
        '99': 'c',
        '100': 'd',
        '101': 'e',
        '102': 'f',
        '103': 'g',
        '104': 'h',
        '105': 'i',
        '106': 'j',
        '107': 'k',
        '108': 'l',
        '109': 'm',
        '110': 'n',
        '111': 'o',
        '112': 'p',
        '113': 'q',
        '114': 'r',
        '115': 's',
        '116': 't',
        '117': 'u',
        '118': 'v',
        '119': 'w',
        '120': 'x',
        '121': 'y',
        '122': 'z',
        '123': '{',
        '124': '|',
        '125': '}',
        '126': '~',
        '127': 'DEL',   # Delete
    }

    output = ""
    values = input.split(' ')

    for value in values:
        output += conversion[value]

    return output

def ascii_to_decimal(input: str):
    conversion = {
         'NUL': '00',    # Null
         'SOH': '01',    # Start of Header
         'STX': '02',    # Start of Text 
         'ETX': '03',    # End of Text
         'EOT': '04',    # End of Transmission
         'ENQ': '05',    # Enquiry
         'ACK': '06',    # Acknowledge
         'BEL': '07',    # Bell
         'BS': '08',     # Backspace
         'HT': '09',     # Horizontal Tab
         'LF': '10',     # Newline / Line Feed
         'VT': '11',     # Vertical Tab
         'FF': '12',     # Form Feed
         'CR': '13',     # Carriage Return
         'SO': '14',     # Shift Out
         'SI': '15',     # Shift In
         'DLE': '16',    # Data Link Escape
         'DC1': '17',    # Device Control 1
         'DC2': '18',    # Device Control 2
         'DC3': '19',    # Device Control 3
         'DC4': '20',    # Device Control 4
         'NAK': '21',    # Negative Achnowledge
         'SYN': '22',    # Synchronize
         'ETB': '23',    # End of Transmission Block
         'CAN': '24',    # Cancel
         'EM': '25',     # End of Medium
         'SUB': '26',    # Substitue
         'ESC': '27',    # Escape
         'FS': '28',     # File Seperator
         'GS': '29',     # Group Seperator
         'RS': '30',     # Record Seperator
         'US': '31',     # Unit Seperator
         'SP': '32',     # Space
         '!': '33',
         '"': '34',
         '#': '35',
         '$': '36',
         '%': '37',
         '&': '38',
         "'": '39',
         '(': '40',
         ')': '41',
         '*': '42',
         '+': '43',
         ',': '44',
         '-': '45',
         '.': '46',
         '/': '47',
         '0': '48',
         '1': '49',
         '2': '50',
         '3': '51',
         '4': '52',
         '5': '53',
         '6': '54',
         '7': '55',
         '8': '56',
         '9': '57',
         ':': '58',
         ';': '59',
         '<': '60',
         '=': '61',
         '>': '62',
         '?': '63',
         '@': '64',
         'A': '65',
         'B': '66',
         'C': '67',
         'D': '68',
         'E': '69',
         'F': '70',
         'G': '71',
         'H': '72',
         'I': '73',
         'J': '74',
         'K': '75',
         'L': '76',
         'M': '77',
         'N': '78',
         'O': '79',
         'P': '80',
         'Q': '81',
         'R': '82',
         'S': '83',
         'T': '84',
         'U': '85',
         'V': '86',
         'W': '87',
         'X': '88',
         'Y': '89',
         'Z': '90',
         '[': '91',
         '\\': '92',
         ']': '93',
         '^': '94',
         '_': '95',
         '`': '96',
         'a': '97',
         'b': '98',
         'c': '99',
         'd': '100',
         'e': '101',
         'f': '102',
         'g': '103',
         'h': '104',
         'i': '105',
         'j': '106',
         'k': '107',
         'l': '108',
         'm': '109',
         'n': '110',
         'o': '111',
         'p': '112',
         'q': '113',
         'r': '114',
         's': '115',
         't': '116',
         'u': '117',
         'v': '118',
         'w': '119',
         'x': '120',
         'y': '121',
         'z': '122',
         '{': '123',
         '|': '124',
         '}': '125',
         '~': '126',
         'DEL': '127',   # Delete
    }

    output = ""
    return output

def hex_to_ascii(input: str):
    output = ""
    return output

def ascii_to_hex(input: str):
    output = ""
    return output

def ascii_to_base64(input: str):
    output = ""
    return output

def base64_to_ascii(input: str):
    output = ""
    return output

if __name__ == '__main__':
    print(decimal_to_ascii('101 100 100 121 115 99 104 97 105'))