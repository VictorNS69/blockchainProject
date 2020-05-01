pragma solidity 0.5.3;

contract SocialNetwork {
    uint256 [] private usersID;
    mapping(uint256 => bool) users;
    
    event addUserEvent(uint256 _user, uint256 _timestamp);
    event removeUserEvent(uint256 _user, uint256 _timestamp);
    
    function addUser(uint256 _user) public {
        require(!users[_user], "This user is already in the system");
        users[_user] = true;
        usersID.push(_user);
        emit addUserEvent(_user, block.timestamp);
    }
    
    function removeUser(uint256 _user) public {
        require(users[_user], "This user is not in the system");
        //users[_user] = false;
        delete users[_user];
        //usersID.push(_user);
        for (uint i = 0; i < usersID.length; i++){
            if (usersID[usersID.length-1] == _user){
                delete usersID[usersID.length-1];
                usersID.length--;
                return;
            }
            else if(usersID[i] == _user){
                for (uint j = i; j < usersID.length-1; j++){
                    usersID[j] = usersID[j+1];
                }
                usersID.length--;            
                //delete usersID[usersID.length-1];
            }
        }
        
        emit removeUserEvent(_user, block.timestamp);
    }
    
    // login
    
    // logout
    
    //message (U1, U2)
    
    function getUsers() public view returns (uint256 [] memory _users){
        return usersID;
    }
    
    function getUser(uint256 _user) public view returns (bool _value){
        return users[_user];
    }
}
