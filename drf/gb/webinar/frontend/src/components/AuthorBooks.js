import {useParams} from 'react-router-dom'

const BookItem = ({book}) => {
    return(
        <tr>
            <td>{book.name}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const AuthorBooks = ({books}) => {
    let {id} = useParams();
    let filteredBooks = books.filter((book) => book.authors.includes(parseInt(id)))

    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Authors
            </th>
            {filteredBooks.map((b) => <BookItem book={b}/>)}
        </table>
    )
}

export default AuthorBooks;