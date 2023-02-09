from web3 import Web3
from django.utils import dateformat, formats


def attribute_dict_to_dict(dict_to_parse):
    # convert any 'AttributeDict' type found to 'dict'
    parsed_dict = dict(dict_to_parse)
    for key, val in parsed_dict.items():
        # check for nested dict structures to iterate through
        if 'dict' in str(type(val)).lower():
            parsed_dict[key] = attribute_dict_to_dict(val)
        # convert 'HexBytes' type to 'str'
        elif 'HexBytes' in str(type(val)):
            parsed_dict[key] = val.hex()
    return parsed_dict


def certificate_to_dictionary(certificate):
    # convert any certificate object to 'dict'
    dictionary = {
        'name': certificate.name,
        'surname': certificate.surname,
        'date_of_birth': dateformat.format(certificate.date_of_birth, formats.get_format('DATE_FORMAT')),
        'grade': certificate.grade,
        'subject': certificate.subject,
        'date_of_creation': dateformat.format(certificate.date_of_creation, formats.get_format('DATE_FORMAT')),
    }
    return dictionary


def get_transaction_by_hash(transaction_hash):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/c83796f78d1a468593d02c4e8c9b2e3e'))
    transaction = attribute_dict_to_dict(w3.eth.get_transaction(transaction_hash))
    return transaction


def send_transaction(message, address_to, address_from, private_key, amount):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/c83796f78d1a468593d02c4e8c9b2e3e'))
    address = '0x00583328725E92B2e9E45a0c96058c533B6aB76d'
    private_key = '0x0bd7acb0531d3cb2d4595475b3ef5f9027c4c1f0420e591cb2c1a0243c4b6a79'
    nonce = w3.eth.getTransactionCount(address)
    gas_price = w3.eth.gasPrice
    value = w3.toWei(amount, 'ether')
    signed_tx = w3.eth.account.signTransaction(dict(
        nonce=nonce,
        gasPrice=gas_price,
        gas=100000,
        to=address_to,
        value=value,
        data=message.encode('utf-8'),
    ), private_key)
    tx = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_id = w3.toHex(tx)
    return tx_id


