const BookItem = ({book}) => {
    return(
        <tr>
            <td>{book.name}</td>
            <td>{book.authors}</td>
        </tr>
    )
}

const BookList = ({books}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Authors
            </th>
            {books.map((b) => <BookItem book={b}/>)}
        </table>
    )
}

export default BookList;