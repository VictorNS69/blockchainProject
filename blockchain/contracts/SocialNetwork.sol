pragma solidity 0.5.2;

contract SocialNetwork {
    bytes32 [] private usersID;
    mapping(bytes32 => string) users;

    function getUsers() public view returns (bytes32 [] memory _users){
        return usersID;
    }
    
    function getUser(bytes32 _user) public view returns (string memory _value){
        return users[_user];
    }
    
    event addUserEvent(string _user, uint256 _timestamp);
    event removeUserEvent(string _user, uint256 _timestamp);
    event sendMessageEvent(string _user1, string _user2, string _message, uint256 _timestamp);
    
    function getBytes(string memory _string) public pure returns (bytes32 _bytes32) {
        return keccak256(abi.encodePacked(_string));
    }
    
    function addUser(string memory _userString) public returns (bytes32 _bytes32) {
        bytes32 userBytes = getBytes(_userString);
        require(bytes(users[userBytes]).length == 0, "This user is already in the system");
        users[userBytes] = _userString;
        usersID.push(userBytes);
        emit addUserEvent(_userString, block.timestamp);
        return userBytes;
    }
    
    function removeUser(string memory _userString) public {
        bytes32 userBytes = getBytes(_userString);
        require(bytes(users[userBytes]).length != 0, "This user is not in the system");
        delete users[userBytes];
        for (uint i = 0; i < usersID.length; i++){
            if (usersID[usersID.length-1] == userBytes){
                usersID.length--;
                emit removeUserEvent(_userString, block.timestamp);
                return;
            }
            else if(usersID[i] == userBytes){
                for (uint j = i; j < usersID.length-1; j++){
                    usersID[j] = usersID[j+1];
                }
                usersID.length--;            
                emit removeUserEvent(_userString, block.timestamp);
            }
        }
    }
    
    function sendMessage(string memory _user1, string memory _user2, string memory _message) public{
        bytes32 user1Bytes = getBytes(_user1);
        bytes32 user2Bytes = getBytes(_user2);
        require(bytes(users[user1Bytes]).length != 0, "The user 1 is not in the system");
        require(bytes(users[user2Bytes]).length != 0, "The user 2 is not in the system");
        require(bytes(_message).length > 0);
        emit sendMessageEvent(_user1, _user2, _message, block.timestamp);
    }
}
