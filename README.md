# 0xProtocol_ERC1155Orders
 
 ## create_order.py
  Allows to create `Buy` or `Sell` ERC1155 orders. The order's hash is calculated using the getERC1155OrderHash(). Calculating the order's hash off-chain would improve performance because it would prevent multiple calls to the Exchange Proxy in the case of creating multiple orders.
  
  ### [Order]: 
  
  ```json
  {
    "order": {
        "direction": 0,
        "erc1155Token": "0xFC37b8F25B57bff5C1b6DF2D76485079BdC133cf",
        "erc1155TokenAmount": 3000000000000000000,
        "erc1155TokenId": 1665619200,
        "erc1155TokenProperties": [],
        "erc20Token": "0xdc31Ee1784292379Fbb2964b3B9C4124D8F89C60",
        "erc20TokenAmount": 3000000000000000000,
        "expiry": 2524604400,
        "fees": [],
        "maker": "0x68ae1B82F4A463Ea8d2Ca3c0Dc9cCe39411B4719",
        "nonce": 110201411100000000000000000010000000002345888550322622858142265866466113455848,
        "signature": {
            "r": "0x1d1b3c345e16c1b02d4c26033f1bfc6aed429f965898f4ea25d008ef648f0fdb",
            "s": "0x2f5fa8aa28a6ab1937cf71d640ba7dfb8b9dcbe91d0d5c42ec73d8057adf40e0",
            "signatureType": 3,
            "v": 28
        },
        "taker": "0x0000000000000000000000000000000000000000"
    }
}

```


  
  
### [OrderHash]: 
```
  b'\xb8\xe1\xe9\x8e\xb2\x94\xa5\xabw\xc1\x98\x8b\xe0\x84e\xa3\x03\xf0I\xb2\xc6\x91\x04x\x15\xab2\x01l\x88\x012'
```
  

## fill_ordersERC1155.py
 Allows to fill `Buy` or `Sell` ERC1155 orders
 
## Tx_Receipts.py
 Contains the transaction hashes of test transactions and code view the transaction's receipts
 
## Contract.sol
 Simple Solidity contract to fill a `Buy` ERC1155 order
