from secp256k1 import lib as secp256k1
from secp256k1 import ffi
import random
import os

SIGHASH_ALL           = 0x00000001
SIGHASH_NONE          = 0x00000002
SIGHASH_SINGLE        = 0x00000003
SIGHASH_ANYONECANPAY  = 0x00000080
MAX_INT_PRIVATE_KEY   = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

MAINNET_ADDRESS_BYTE_PREFIX = b'\x00'
TESTNET_ADDRESS_BYTE_PREFIX = b'\x6f'
MAINNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\x05'
TESTNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\xc4'
MAINNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x00\x02\x03'
TESTNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x00\x14\x02'

MAINNET_ADDRESS_PREFIX = '1'
TESTNET_ADDRESS_PREFIX = 'm'
TESTNET_ADDRESS_PREFIX_2 = 'n'
MAINNET_SCRIPT_ADDRESS_PREFIX = '3'
TESTNET_SCRIPT_ADDRESS_PREFIX = '2'

MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '5'
MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'K'
MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX_2 = 'L'
TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '9'
TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'c'

ADDRESS_PREFIX_LIST = (MAINNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX_2,
                       MAINNET_SCRIPT_ADDRESS_PREFIX,
                       TESTNET_SCRIPT_ADDRESS_PREFIX)

PRIVATE_KEY_PREFIX_LIST = (MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX,
                           MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX_2,
                           TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX)

MAINNET_PRIVATE_KEY_BYTE_PREFIX = b'\x80'
TESTNET_PRIVATE_KEY_BYTE_PREFIX = b'\xef'

MAINNET_SEGWIT_ADDRESS_PREFIX = 'bc'
TESTNET_SEGWIT_ADDRESS_PREFIX = 'tb'


EC_COMPRESSED = secp256k1.SECP256K1_EC_COMPRESSED
EC_UNCOMPRESSED = secp256k1.SECP256K1_EC_UNCOMPRESSED

FLAG_SIGN = secp256k1.SECP256K1_CONTEXT_SIGN
FLAG_VERIFY = secp256k1.SECP256K1_CONTEXT_VERIFY
ALL_FLAGS = FLAG_SIGN | FLAG_VERIFY
NO_FLAGS = secp256k1.SECP256K1_CONTEXT_NONE

HAS_RECOVERABLE = hasattr(secp256k1, 'secp256k1_ecdsa_sign_recoverable')
HAS_SCHNORR = hasattr(secp256k1, 'secp256k1_schnorr_sign')
HAS_ECDH = hasattr(secp256k1, 'secp256k1_ecdh')

ECDSA_CONTEXT_SIGN = secp256k1.secp256k1_context_create(FLAG_SIGN)
ECDSA_CONTEXT_VERIFY = secp256k1.secp256k1_context_create(FLAG_VERIFY)
ECDSA_CONTEXT_ALL = secp256k1.secp256k1_context_create(ALL_FLAGS)
secp256k1.secp256k1_context_randomize(ECDSA_CONTEXT_SIGN,
                                      random.SystemRandom().randint(0,MAX_INT_PRIVATE_KEY).to_bytes(32,byteorder="big"))

SCRIPT_TYPES = { "P2PKH":        0,
                 "P2SH" :        1,
                 "PUBKEY":       2,
                 "NULL_DATA":    3,
                 "MULTISIG":     4,
                 "P2WPKH":       5,
                 "P2WSH":        6,
                 "NON_STANDART": 7
                }

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
BIP0039_DIR = os.path.normpath(os.path.join(ROOT_DIR, 'bip-0039'))
