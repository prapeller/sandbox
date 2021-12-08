const UserItem = ({user}) => {
    return(
        <tr>
            <td>{user.id}</td>
            <td>{user.username}</td>
            <td>{user.date_joined}</td>
            <td>{user.last_login}</td>
            <td>{user.email}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{`${user.is_staff}`}</td>
            <td>{`${user.is_superuser}`}</td>
            <td>{user.groups}</td>
            <td>{user.user_permissions}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table>
            <th>Id</th>
            <th>Username</th>
            <th>Date Joined</th>
            <th>Last login</th>
            <th>Email</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Is staff</th>
            <th>Is superuser</th>
            <th>Groups</th>
            <th>Permissions</th>
            {users.map((u) => <UserItem user={u}/>)}
        </table>
    )
}

export default UserList;