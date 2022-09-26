import web3
import os
import json
from eth_account.messages import encode_defunct
import eth_abi
from eth_utils import keccak

from typing import NamedTuple, Tuple



class ERC1155Order(NamedTuple):
    direction: int
    maker: str
    taker: str
    expiry: int
    nonce: int
    erc20Token: str
    erc20TokenAmount: int
    fees: any
    erc1155Token: str
    erc1155TokenId: int
    erc1155TokenProperties: any
    erc1155TokenAmount: int
    
    
def getERC1155OrderHash(_order):
    
    order_hash = contract.functions.getERC1155OrderHash(_order).call()
    
    return order_hash
    
def signOrderHash(order_hash, private_key):
    pk = web3.Web3.toBytes(hexstr = private_key)
    message = encode_defunct(order_hash)
    signed_order = client.eth.account.sign_message(message, private_key= pk)
    
    return (
        signed_order.v,
        '0x' + signed_order.r.to_bytes(length=32, byteorder='big').hex(),
        '0x' + signed_order.s.to_bytes(length=32, byteorder='big').hex()
    )


def createERC1155Order(order, pk):

    order_dict = {
        'direction': order.direction, 
        'maker': order.maker,
        'taker': order.taker,
        'expiry': order.expiry, 
        'nonce':order.nonce,
        'erc20Token':order.erc20Token, 
        'erc20TokenAmount': order.erc20TokenAmount, 
        'fees': order.fees, 
        'erc1155Token': order.erc1155Token, 
        'erc1155TokenId': order.erc1155TokenId,
        'erc1155TokenProperties': order.erc1155TokenProperties, 
        'erc1155TokenAmount': order.erc1155TokenAmount
        }
      
    order_hash = getERC1155OrderHash(order_dict)
    (v,r,s) = signOrderHash(order_hash, pk)
    
    signature_dict = {'signatureType': 3, 'r': r, 's': s, 'v': v}
    order_dict['signature'] = signature_dict
    
    return { 'order': order_dict }

if __name__ == '__main__':

    #get Goerli provider
    provider = web3.HTTPProvider("PROVIDER_URL");
    client = web3.Web3(provider);
    
    #Exchange Proxy address for Goerli
    EP_address = '0xF91bB752490473B8342a3E964E855b9f9a2A668e'
    
    #load ABI
    f = open('abi.json')
    abi = json.load(f)
    contract = client.eth.contract(address = EP_address, abi = abi)

    maker = client.toChecksumAddress('0x68ae1B82F4A463Ea8d2Ca3c0Dc9cCe39411B4719')    
    erc20Token = client.toChecksumAddress('0xdc31ee1784292379fbb2964b3b9c4124d8f89c60')
    erc1155Token = client.toChecksumAddress('0xfc37b8f25b57bff5c1b6df2d76485079bdc133cf')
    nonce = 110201411100000000000000000010000000002345888550322622858142265866466113455848   
    zero_address = client.toChecksumAddress('0x0000000000000000000000000000000000000000')
    
    
    order = ERC1155Order(direction = 0, maker = maker, taker = zero_address, expiry = 2524604400, nonce = nonce, erc20Token = erc20Token, erc20TokenAmount= 3000000000000000000 ,fees = [], erc1155Token = erc1155Token, erc1155TokenId = 1665619200, erc1155TokenProperties = [], erc1155TokenAmount = 3000000000000000000)
    
    pk = '0x<private_key>'
    print(createERC1155Order(order, pk))








