import {Link} from 'react-router-dom'
import {App} from "../App";

const Header = () => {
    return (
        <ul>
            {/*<li><Link to="/authors">Authors</Link></li>*/}
            {/*<li><Link to="/books">Books</Link></li>*/}
            {/*<li>*/}
            {/*    { App.is_auth() ? <button onClick={() => App.this.logout()}>Logout</button> : <Link to="/login">Login</Link>}*/}
            {/*</li>*/}
        </ul>
    )
}

export default Header