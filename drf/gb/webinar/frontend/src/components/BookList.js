const BookItem = ({book, deleteBook}) => {
    return(
        <tr>
            <td>{book.name}</td>
            <td>{book.authors}</td>
            <td><button onClick={()=>deleteBook(book.id)} type={'button'}>Delete</button></td>
        </tr>
    )
}

const BookList = ({books, deleteBook}) => {
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Authors
            </th>
            {books.map((b) => <BookItem book={b} deleteBook={deleteBook}/>)}
        </table>
    )
}

export default BookList;