//SPDX-License-Identifier: No License
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC20/IERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/IERC1155.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC1155/IERC1155Receiver.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

interface Structs{
     enum SignatureType {
        ILLEGAL,
        INVALID,
        EIP712,
        ETHSIGN,
        PRESIGNED
    }

    /// @dev Encoded EC signature.
    struct Signature {
        // How to validate the signature.
        SignatureType signatureType;
        // EC Signature data.
        uint8 v;
        // EC Signature data.
        bytes32 r;
        // EC Signature data.
        bytes32 s;
    }

    enum TradeDirection {
        SELL_NFT,
        BUY_NFT
    }

    struct Property {
        IPropertyValidator propertyValidator;
        bytes propertyData;
    }

    struct Fee {
        address recipient;
        uint256 amount;
        bytes feeData;
    }

    struct ERC1155Order {
        TradeDirection direction;
        address maker;
        address taker;
        uint256 expiry;
        uint256 nonce;
        address erc20Token;
        uint256 erc20TokenAmount;
        Fee[] fees;
        address erc1155Token;
        uint256 erc1155TokenId;
        Property[] erc1155TokenProperties;
        uint128 erc1155TokenAmount;
    }
}


interface ZeroEx is Structs{

        function buyERC1155(
        ERC1155Order memory sellOrder,
        Signature memory signature,
        uint128 erc1155BuyAmount,
        bytes memory callbackData) external;
        
    }

interface IPropertyValidator {

    function validateProperty(
        address tokenAddress,
        uint256 tokenId,
        bytes calldata propertyData
    )
        external
        view;
}


contract BuyERC1155 is Ownable, IERC1155Receiver, Structs{

    address public EP = 0xF91bB752490473B8342a3E964E855b9f9a2A668e;
    address public erc20Token;
    address public erc1155Token;


    function setERC20_ERC1155Pair(address _erc20, address _erc1155) 
    external 
    onlyOwner 
    {
        erc20Token = _erc20;
        erc1155Token = _erc1155;
    }

    function setApproval_ERC20_ERC115(address _spender, uint256 _erc20Amount, bool _erc1155IsApproved) 
    external
    onlyOwner
    {
        IERC20 token20 = IERC20(erc20Token);
        IERC1155 token1155 = IERC1155(erc1155Token);

        token20.approve(EP, _erc20Amount);
        token1155.setApprovalForAll(_spender, _erc1155IsApproved);
    } 


    function _buyERC1155(ERC1155Order calldata order, Signature calldata sig, uint128 amount) 
    external 
    onlyOwner
    returns(bool)  
    {
      
        ZeroEx instance = ZeroEx(EP);

        instance.buyERC1155(order, sig, amount, bytes(''));

        return true;

    }

    function supportsInterface(bytes4 interfaceId) external pure returns (bool){
        interfaceId;
        return true;
    }

    function onERC1155Received(
        address operator,
        address from,
        uint256 id,
        uint256 value,
        bytes calldata data
    ) external pure returns (bytes4){
        operator;
        from;
        id;
        value;
        data;
        return bytes4(keccak256("onERC1155Received(address,address,uint256,uint256,bytes)"));
    }

    
    function onERC1155BatchReceived(
        address operator,
        address from,
        uint256[] calldata ids,
        uint256[] calldata values,
        bytes calldata data
    ) external pure returns (bytes4){

    operator;
    from;
    ids;
    values;
    data;
    return bytes4(keccak256("onERC1155BatchReceived(address,address,uint256[],uint256[],bytes)"));

    }

}