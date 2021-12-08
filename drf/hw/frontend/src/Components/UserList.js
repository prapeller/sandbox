const UserItem = ({user}) => {
    return(
        <tr>
            <td>{user.username}</td>
            <td>{user.email}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.is_staff}</td>
            <td>{user.is_superuser}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>Username</th>
            <th>Email</th>
            <th>First name</th>
            <th>Last name</th>
            <th>Is Staff</th>
            <th>Is Superuser</th>
            {users.map((u) => <UserItem user={u}/>)}
        </table>
    )
}

export default UserList;