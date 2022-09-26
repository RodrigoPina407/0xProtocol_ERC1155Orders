import web3
import os
import json
from eth_account.messages import encode_defunct
import eth_abi
from eth_utils import keccak

 
def fillBuyERC1155Order(_order, _buyer, _amount, _v,_r, _s, _pk): 
    pk = web3.Web3.toBytes(hexstr = _pk)
    
    _r = bytes.fromhex(_r[2:])
    _s = bytes.fromhex(_s[2:])
    
        
    order_tuple = '(uint8,address,address,uint256,uint256,address,uint256,(address,uint256,bytes)[],address,uint256,(address,bytes)[],uint128)'
    signature_tuple = '(uint8,uint8,bytes32,bytes32)'
    
    buy_function_definition = f'buyERC1155({order_tuple},{signature_tuple},uint128,bytes)'
    
    buy_function_signature = web3.Web3.keccak(text= buy_function_definition).hex()[:10]
    
    encodes = [
        order_tuple,
        signature_tuple,
        'uint128',
        'bytes'
    ]
    encoded_args = eth_abi.encode_abi(encodes, [[
        _order['direction'],
        _order['maker'],
        _order['taker'],
        _order['expiry'],
        _order['nonce'],
        _order['erc20Token'],
        _order['erc20TokenAmount'],
        [list(l.values()) for l in _order['fees']],
        _order['erc1155Token'],
        _order['erc1155TokenId'],
        [list(l.values()) for l in _order['erc1155TokenProperties']],
        _order['erc1155TokenAmount']
    ], [3, _v, _r, _s], _amount,b''])
    
    calldata = buy_function_signature + encoded_args.hex()
    
    tx = {
            "from": _buyer,
            "to": client.toChecksumAddress(EP_address),
            "data": calldata,
            "gasPrice": int(10 * 1e9),
            "gas": 500_000,
            "nonce": client.eth.getTransactionCount(_buyer),
        }
    signed = client.eth.account.sign_transaction(tx, pk)
    fill_tx = client.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = client.eth.waitForTransactionReceipt(fill_tx)
    print(f"Fill transaction succeded: {fill_tx.hex()}")
    
    return tx_receipt
  

def fillSellERC1155Order(_order, _seller, _tokenId, _amount, _v,_r, _s, _pk): 
    pk = web3.Web3.toBytes(hexstr = _pk)
    
    _r = bytes.fromhex(_r[2:])
    _s = bytes.fromhex(_s[2:])
    
    order_tuple = '(uint8,address,address,uint256,uint256,address,uint256,(address,uint256,bytes)[],address,uint256,(address,bytes)[],uint128)'
    signature_tuple = '(uint8,uint8,bytes32,bytes32)'
    
    sell_function_definition = f'sellERC1155({order_tuple},{signature_tuple},uint256,uint128,bool,bytes)'
    
    sell_function_signature = web3.Web3.keccak(text= sell_function_definition).hex()[:10]
  
    encodes = [
        order_tuple,
        signature_tuple,
        'uint256',
        'uint128',
        'bool',
        'bytes'
    ]
    encoded_args = eth_abi.encode_abi(encodes, [[
        _order['direction'],
        _order['maker'],
        _order['taker'],
        _order['expiry'],
        _order['nonce'],
        _order['erc20Token'],
        _order['erc20TokenAmount'],
        [list(l.values()) for l in _order['fees']],
        _order['erc1155Token'],
        _order['erc1155TokenId'],
        [list(l.values()) for l in _order['erc1155TokenProperties']],
        _order['erc1155TokenAmount']
    ], [3, _v, _r, _s], _tokenId, _amount, False, b''])
    
    calldata = sell_function_signature + encoded_args.hex()
    
    tx = {
            "from": _seller,
            "to": client.toChecksumAddress(EP_address),
            "data": calldata,
            "gasPrice": int(10 * 1e9),
            "gas": 500_000,
            "nonce": client.eth.getTransactionCount(_seller),
        }
    signed = client.eth.account.sign_transaction(tx, pk)
    fill_tx = client.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = client.eth.waitForTransactionReceipt(fill_tx)
    print(f"Fill transaction succeded: {fill_tx.hex()}")
    
    return tx_receipt
    

  
if __name__ == '__main__':


    #get Goerli provider
    provider = web3.HTTPProvider("provider_url");
    client = web3.Web3(provider);
    
    #Exchange Proxy address for Goerli
    EP_address = '0xF91bB752490473B8342a3E964E855b9f9a2A668e'
    
    #order inputs
    maker = client.toChecksumAddress('0x6bea7d5f80ab338e11f1a98a69d81ec669f88a28')
    erc20Token = client.toChecksumAddress('0xdc31ee1784292379fbb2964b3b9c4124d8f89c60')
    erc1155Token = client.toChecksumAddress('0xfc37b8f25b57bff5c1b6df2d76485079bdc133cf')
    nonce = 110201411100000000000000000000000000000051746150322622858142265866466119123410
    zero_address = client.toChecksumAddress('0x0000000000000000000000000000000000000000')
    
    #order = {'direction':0, 'maker': maker,'taker':zero_address,'expiry': 2524604400, 'nonce':nonce,'erc20Token':erc20Token, 'erc20TokenAmount': 5000000000000000000, 'fees': [], 'erc1155Token':erc1155Token, 'erc1155TokenId':1665619200,'erc1155TokenProperties':[], 'erc1155TokenAmount':5000000000000000000}
    
    #order = {'direction':0, 'maker': client.toChecksumAddress('0x68ae1B82F4A463Ea8d2Ca3c0Dc9cCe39411B4719'),'taker':'0x0000000000000000000000000000000000000000','expiry': 2524604400, 'nonce':110201411100000000000000000000000000002345345550322622858142265866466113456456,'erc20Token':erc20Token, 'erc20TokenAmount': 4000000000000000000, 'fees': [], 'erc1155Token':erc1155Token, 'erc1155TokenId':1665619200,'erc1155TokenProperties':[], 'erc1155TokenAmount':4000000000000000000}
    
    order = {'direction':1, 'maker': client.toChecksumAddress('0x68ae1B82F4A463Ea8d2Ca3c0Dc9cCe39411B4719'),'taker':'0x0000000000000000000000000000000000000000','expiry': 2524604400, 'nonce':110201411100000000000000000010000000002345345550322622858142265866466113455848,'erc20Token':erc20Token, 'erc20TokenAmount': 3000000000000000000, 'fees': [], 'erc1155Token':erc1155Token, 'erc1155TokenId':1665619200,'erc1155TokenProperties':[], 'erc1155TokenAmount':3000000000000000000}
    
    #load ABI
    f = open('abi.json')
    abi = json.load(f)
    contract = client.eth.contract(address = EP_address, abi = abi)
    
    x = contract.functions.getERC1155OrderInfo(order).call()
    print(x)
    print('\n')
    
    taker = client.toChecksumAddress('0x7dcf9CFDFd5D5aD1DCb421c191c12DD8f9EBCd7B')
    taker_pk = '0x<private_key>'
    #v = 28
    #r = '0xa350e200db0ae714ad165191098003e836cd315b7f485cd45e471045c3c8e31f'
    #s = '0x6d5a99b6708d30f0f8ae58311448f2c65874b34b73f39d23a0957e2a95300b66'
    #fillBuyERC1155Order(order, taker, 1000000000000000000, v, r, s, taker_pk);
    
   
    v = 27
    r = '0xfc15ddc2d367a57087ed4fca453301f1c561958a6066243c99912906be055faa'
    s = '0x448177a7d5911779c117628923b18dbe5821d720e7391e45db06c4c01de789ca'
    fillSellERC1155Order(order, taker, 1665619200, 1000000000000000000, v, r, s, taker_pk);





 










