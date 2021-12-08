const AuthorItem = ({author}) => {
    return(
        <tr>
            <td>{author.first_name}</td>
            <td>{author.last_name}</td>
            <td>{author.birth_year}</td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                First name
            </th>
            <th>
                Last name
            </th>
            <th>
                Birth year
            </th>
            {authors.map((author) => <AuthorItem author={author}/>)}
        </table>
    )
}

export default AuthorList;