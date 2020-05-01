pragma solidity 0.5.16;

contract SocialNetwork {
    uint256 [] private usersID;
    mapping(uint256 => bool) users;
    
    event addUserEvent(uint256 _user, uint256 _timestamp);
    event removeUserEvent(uint256 _user, uint256 _timestamp);
    event messageSendEvent(uint256 _user1, uint256 _user2, uint256 _timestamp);
    
    function getUsers() public view returns (uint256 [] memory _users){
        return usersID;
    }
    
    function getUser(uint256 _user) public view returns (bool _value){
        return users[_user];
    }
    
    function addUser(uint256 _user) public {
        require(!users[_user], "This user is already in the system");
        users[_user] = true;
        usersID.push(_user);
        emit addUserEvent(_user, block.timestamp);
    }
    
    function removeUser(uint256 _user) public {
        require(users[_user], "This user is not in the system");
        delete users[_user];
        for (uint i = 0; i < usersID.length; i++){
            if (usersID[usersID.length-1] == _user){
                usersID.length--;
                emit removeUserEvent(_user, block.timestamp);
                return;
            }
            else if(usersID[i] == _user){
                for (uint j = i; j < usersID.length-1; j++){
                    usersID[j] = usersID[j+1];
                }
                usersID.length--;            
                emit removeUserEvent(_user, block.timestamp);
            }
        }
    }

    function sendMessage(uint256 _user1, uint256 _user2) public{
        require(users[_user1], "The user 1 is not in the system");
        require(users[_user2], "The user 2 is not in the system");
        emit messageSendEvent(_user1, _user2, block.timestamp);
    }
}
