import {Link} from 'react-router-dom'

const Header = () => {
    return(
        <ul>
            <li><Link  to="/authors">Authors</Link></li>
            <li><Link  to="/books">Books</Link></li>
        </ul>
    )
}

export default Header