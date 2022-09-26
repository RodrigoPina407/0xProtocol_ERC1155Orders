import web3

#get Goerli provider
provider = web3.HTTPProvider("provider_url");
client = web3.Web3(provider);

buyERC1155_1 = '0xe3e2695f60416c7311c9dd921692dca18107cda593b905857b1e890accb50465'
buyERC1155_2 = '0x53c5dd4ef393e802885d1827f7d95dc9103111b606022cea1f45881f8db02f0d'
sellERC1155_1 = '0x92ff940334ac7ba1e1b5faa23a9a1dc4f45f2d8529fd6e2e6e3bc647d1c603e2'
contractBuyOrder = '0x6034ee8be639279d510885c24e33895c964826edcfb5abd7bfd3b14cfdf2bd97'

print(client.eth.get_transaction_receipt(sellERC1155_1))